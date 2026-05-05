"""Inject Roboto TTFs into a .pptx as embedded fonts.

python-pptx produces a valid .pptx but does not write the OOXML parts that
embed fonts. Without embedding, a deck on a machine that lacks Roboto falls
back to Arial. This module post-processes a python-pptx output, adding the
`<p:embeddedFontLst>` entry, `ppt/fonts/*.fntdata` parts, and the corresponding
relationships and content-type registrations.

The script entry point at scripts/embed-fonts.py is a thin wrapper around
embed_fonts() in this module so the v2.x install path keeps working.
"""

from __future__ import annotations

import shutil
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from reeinvent_pitch_deck.assets import font_file


# Each entry: (font filename, typeface name shown to PowerPoint, slot).
# Slot is one of: regular, bold, italic, boldItalic.
# The "Roboto" typeface holds 400/700/italic; non-400-non-700 weights are
# embedded as their own typefaces so slides referencing them render correctly.
FONT_MAP: list[tuple[str, str, str]] = [
    ("Roboto-Regular.ttf", "Roboto", "regular"),
    ("Roboto-Bold.ttf", "Roboto", "bold"),
    ("Roboto-Italic.ttf", "Roboto", "italic"),
    ("Roboto-Light.ttf", "Roboto Light", "regular"),
    ("Roboto-Medium.ttf", "Roboto Medium", "regular"),
    ("Roboto-Black.ttf", "Roboto Black", "regular"),
]

NS = {
    "ct": "http://schemas.openxmlformats.org/package/2006/content-types",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
FONT_REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/font"
FONT_CONTENT_TYPE = "application/x-fontdata"

ELEMENTS_AFTER_EMBEDDED_FONTS = [
    f"{{{NS['p']}}}custShowLst",
    f"{{{NS['p']}}}photoAlbum",
    f"{{{NS['p']}}}custDataLst",
    f"{{{NS['p']}}}kinsoku",
    f"{{{NS['p']}}}defaultTextStyle",
    f"{{{NS['p']}}}modifyVerifier",
    f"{{{NS['p']}}}extLst",
]


def _load_fonts() -> list[tuple[str, str, str, bytes]]:
    loaded = []
    for filename, typeface, slot in FONT_MAP:
        path = font_file(filename)
        loaded.append((filename, typeface, slot, path.read_bytes()))
    return loaded


def _register_namespaces() -> None:
    for prefix, uri in NS.items():
        ET.register_namespace("" if prefix in ("ct", "rel") else prefix, uri)


def _patch_content_types(xml_bytes: bytes) -> bytes:
    ET.register_namespace("", NS["ct"])
    root = ET.fromstring(xml_bytes)
    for default in root.findall(f"{{{NS['ct']}}}Default"):
        if default.get("Extension") == "fntdata":
            return xml_bytes
    new_default = ET.SubElement(
        root,
        f"{{{NS['ct']}}}Default",
        {"Extension": "fntdata", "ContentType": FONT_CONTENT_TYPE},
    )
    root.remove(new_default)
    overrides = [c for c in list(root) if c.tag == f"{{{NS['ct']}}}Override"]
    for o in overrides:
        root.remove(o)
    root.append(new_default)
    for o in overrides:
        root.append(o)
    return ET.tostring(root, xml_declaration=True, encoding="UTF-8", short_empty_elements=True)


def _next_free_rel_id(rels_root: ET.Element) -> int:
    max_id = 0
    for rel in rels_root.findall(f"{{{NS['rel']}}}Relationship"):
        rid = rel.get("Id", "")
        if rid.startswith("rId"):
            try:
                max_id = max(max_id, int(rid[3:]))
            except ValueError:
                pass
    return max_id + 1


def _patch_presentation_rels(
    xml_bytes: bytes, fonts: list[tuple[str, str, str, bytes]]
) -> tuple[bytes, list[str]]:
    ET.register_namespace("", NS["rel"])
    root = ET.fromstring(xml_bytes)
    next_id = _next_free_rel_id(root)
    rel_ids = []
    for idx, (_filename, _typeface, _slot, _bytes) in enumerate(fonts):
        rid = f"rId{next_id + idx}"
        ET.SubElement(
            root,
            f"{{{NS['rel']}}}Relationship",
            {
                "Id": rid,
                "Type": FONT_REL_TYPE,
                "Target": f"fonts/font{idx + 1}.fntdata",
            },
        )
        rel_ids.append(rid)
    return (
        ET.tostring(root, xml_declaration=True, encoding="UTF-8", short_empty_elements=True),
        rel_ids,
    )


def _build_embedded_font_lst(
    fonts: list[tuple[str, str, str, bytes]], rel_ids: list[str]
) -> ET.Element:
    lst = ET.Element(f"{{{NS['p']}}}embeddedFontLst")
    by_typeface: dict[str, list[tuple[str, str]]] = {}
    order: list[str] = []
    for (_filename, typeface, slot, _bytes), rid in zip(fonts, rel_ids):
        if typeface not in by_typeface:
            by_typeface[typeface] = []
            order.append(typeface)
        by_typeface[typeface].append((slot, rid))
    for typeface in order:
        ef = ET.SubElement(lst, f"{{{NS['p']}}}embeddedFont")
        ET.SubElement(ef, f"{{{NS['p']}}}font", {"typeface": typeface})
        for slot, rid in by_typeface[typeface]:
            ET.SubElement(ef, f"{{{NS['p']}}}{slot}", {f"{{{NS['r']}}}id": rid})
    return lst


def _patch_presentation_xml(xml_bytes: bytes, embedded: ET.Element) -> bytes:
    ET.register_namespace("p", NS["p"])
    ET.register_namespace("r", NS["r"])
    root = ET.fromstring(xml_bytes)
    for existing in root.findall(f"{{{NS['p']}}}embeddedFontLst"):
        root.remove(existing)
    children = list(root)
    insert_at = len(children)
    for idx, child in enumerate(children):
        if child.tag in ELEMENTS_AFTER_EMBEDDED_FONTS:
            insert_at = idx
            break
    root.insert(insert_at, embedded)
    return ET.tostring(root, xml_declaration=True, encoding="UTF-8", short_empty_elements=True)


def _rewrite_pptx(input_path: Path, output_path: Path) -> None:
    fonts = _load_fonts()
    tmp_path = output_path.with_suffix(output_path.suffix + ".tmp")
    with zipfile.ZipFile(input_path, "r") as zin:
        names = set(zin.namelist())
        required = {
            "[Content_Types].xml",
            "ppt/presentation.xml",
            "ppt/_rels/presentation.xml.rels",
        }
        missing = required - names
        if missing:
            raise ValueError(f"pptx is missing required parts: {sorted(missing)}")
    with zipfile.ZipFile(input_path, "r") as zin, zipfile.ZipFile(
        tmp_path, "w", zipfile.ZIP_DEFLATED
    ) as zout:
        original_rels = zin.read("ppt/_rels/presentation.xml.rels")
        new_rels, rel_ids = _patch_presentation_rels(original_rels, fonts)
        embedded = _build_embedded_font_lst(fonts, rel_ids)
        for name in zin.namelist():
            if name == "[Content_Types].xml":
                zout.writestr(name, _patch_content_types(zin.read(name)))
            elif name == "ppt/_rels/presentation.xml.rels":
                zout.writestr(name, new_rels)
            elif name == "ppt/presentation.xml":
                zout.writestr(name, _patch_presentation_xml(zin.read(name), embedded))
            elif name.startswith("ppt/fonts/font") and name.endswith(".fntdata"):
                continue
            else:
                zout.writestr(name, zin.read(name))
        for idx, (_filename, _typeface, _slot, data) in enumerate(fonts, start=1):
            zout.writestr(f"ppt/fonts/font{idx}.fntdata", data)
    tmp_path.replace(output_path)


def _verify(path: Path) -> None:
    with zipfile.ZipFile(path, "r") as z:
        names = set(z.namelist())
        expected = {f"ppt/fonts/font{i}.fntdata" for i in range(1, len(FONT_MAP) + 1)}
        missing = expected - names
        if missing:
            raise RuntimeError(f"post-write verification failed: missing {sorted(missing)}")
        pres = z.read("ppt/presentation.xml").decode("utf-8", errors="replace")
        if "embeddedFontLst" not in pres:
            raise RuntimeError(
                "post-write verification failed: embeddedFontLst not found in presentation.xml"
            )


def embed_fonts(input_path: Path, output_path: Path | None = None) -> Path:
    """Inject Roboto TTFs into the given .pptx. Returns the written path.

    If output_path is None, input_path is replaced in place (with a backup
    written to input_path.bak that is removed on success, restored on failure).
    """
    _register_namespaces()
    input_path = Path(input_path)
    if not input_path.is_file():
        raise FileNotFoundError(f"input file not found: {input_path}")
    output = Path(output_path) if output_path else input_path
    if input_path == output:
        backup = input_path.with_suffix(input_path.suffix + ".bak")
        shutil.copy2(input_path, backup)
        try:
            _rewrite_pptx(input_path, output)
            _verify(output)
        except Exception:
            shutil.copy2(backup, input_path)
            backup.unlink(missing_ok=True)
            raise
        backup.unlink(missing_ok=True)
    else:
        try:
            _rewrite_pptx(input_path, output)
            _verify(output)
        except Exception:
            output.unlink(missing_ok=True)
            raise
    return output
