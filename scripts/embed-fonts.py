#!/usr/bin/env python3
"""
embed-fonts.py - Inject Roboto TTFs into a .pptx as embedded fonts.

Why this exists
---------------
python-pptx produces a valid .pptx but does NOT write the OOXML parts
that embed fonts into the file. Without embedding, a deck rendered on
a machine that lacks Roboto falls back to Arial. For Reeinvent decks
that ship to clients, Roboto must render identically everywhere.

This script post-processes a python-pptx output, adding the OOXML
`<p:embeddedFontLst>` entry plus `ppt/fonts/*.fntdata` parts and the
corresponding relationships and content-type registrations.

Usage
-----
    python scripts/embed-fonts.py INPUT.pptx [OUTPUT.pptx]

If OUTPUT.pptx is omitted, INPUT.pptx is replaced in place.

What gets embedded
------------------
Six TTFs from assets/fonts/Roboto/:
  - Roboto Light (300)    -> typeface "Roboto Light", regular slot
  - Roboto Regular (400)  -> typeface "Roboto", regular slot
  - Roboto Medium (500)   -> typeface "Roboto Medium", regular slot
  - Roboto Bold (700)     -> typeface "Roboto", bold slot
  - Roboto Black (900)    -> typeface "Roboto Black", regular slot
  - Roboto Italic (400)   -> typeface "Roboto", italic slot

Reeinvent decks should set text typeface to "Roboto", "Roboto Light",
"Roboto Medium", or "Roboto Black" as appropriate. With the embedded
fonts in place, every downstream PowerPoint / Keynote / Google Slides
client renders the deck with the correct weight, no fallback.

Exit codes
----------
0 on success. Non-zero on any failure (unreadable fonts, malformed
.pptx, missing parts). Per the "when blocked, stop" rule, this script
does not try to silently patch around errors.
"""

from __future__ import annotations

import shutil
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

REPO_ROOT = Path(__file__).resolve().parent.parent
FONTS_DIR = REPO_ROOT / "assets" / "fonts" / "Roboto"

# Each entry: (filename, typeface shown in PowerPoint, slot)
# Slot is one of: "regular", "bold", "italic", "boldItalic".
# The "Roboto" typeface holds the 400/700/italic slots; non-400-non-700
# weights are embedded as their own typefaces so they render correctly
# when slides reference them.
FONT_MAP = [
    ("Roboto-Regular.ttf", "Roboto", "regular"),
    ("Roboto-Bold.ttf", "Roboto", "bold"),
    ("Roboto-Italic.ttf", "Roboto", "italic"),
    ("Roboto-Light.ttf", "Roboto Light", "regular"),
    ("Roboto-Medium.ttf", "Roboto Medium", "regular"),
    ("Roboto-Black.ttf", "Roboto Black", "regular"),
]

# OOXML namespaces used in the parts we touch.
NS = {
    "ct": "http://schemas.openxmlformats.org/package/2006/content-types",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
FONT_REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/font"
FONT_CONTENT_TYPE = "application/x-fontdata"

# Ordering of children inside <p:presentation> per ECMA-376. We insert
# <p:embeddedFontLst> before any of these (whichever appears first).
ELEMENTS_AFTER_EMBEDDED_FONTS = [
    f"{{{NS['p']}}}custShowLst",
    f"{{{NS['p']}}}photoAlbum",
    f"{{{NS['p']}}}custDataLst",
    f"{{{NS['p']}}}kinsoku",
    f"{{{NS['p']}}}defaultTextStyle",
    f"{{{NS['p']}}}modifyVerifier",
    f"{{{NS['p']}}}extLst",
]


def fail(msg: str) -> "int":
    print(f"embed-fonts: {msg}", file=sys.stderr)
    return 1


def load_fonts() -> "list[tuple[str, str, str, bytes]]":
    """Read every TTF listed in FONT_MAP. Return (filename, typeface, slot, bytes)."""
    loaded = []
    for filename, typeface, slot in FONT_MAP:
        path = FONTS_DIR / filename
        if not path.is_file():
            raise FileNotFoundError(
                f"missing font file: {path} (repo is incomplete or fonts dir moved)"
            )
        loaded.append((filename, typeface, slot, path.read_bytes()))
    return loaded


def register_namespaces() -> None:
    """ElementTree strips xmlns decls on write unless we register prefixes."""
    for prefix, uri in NS.items():
        ET.register_namespace("" if prefix == "ct" or prefix == "rel" else prefix, uri)


def patch_content_types(xml_bytes: bytes) -> bytes:
    """Add a Default entry for .fntdata if one isn't already present."""
    ET.register_namespace("", NS["ct"])
    root = ET.fromstring(xml_bytes)
    for default in root.findall(f"{{{NS['ct']}}}Default"):
        if default.get("Extension") == "fntdata":
            return xml_bytes  # already registered
    new_default = ET.SubElement(
        root,
        f"{{{NS['ct']}}}Default",
        {"Extension": "fntdata", "ContentType": FONT_CONTENT_TYPE},
    )
    # Keep Default elements before Override elements (not strictly
    # required but produces cleaner output).
    root.remove(new_default)
    overrides = [c for c in list(root) if c.tag == f"{{{NS['ct']}}}Override"]
    for o in overrides:
        root.remove(o)
    root.append(new_default)
    for o in overrides:
        root.append(o)
    return ET.tostring(root, xml_declaration=True, encoding="UTF-8", short_empty_elements=True)


def next_free_rel_id(rels_root: "ET.Element") -> int:
    max_id = 0
    for rel in rels_root.findall(f"{{{NS['rel']}}}Relationship"):
        rid = rel.get("Id", "")
        if rid.startswith("rId"):
            try:
                max_id = max(max_id, int(rid[3:]))
            except ValueError:
                pass
    return max_id + 1


def patch_presentation_rels(
    xml_bytes: bytes, fonts: "list[tuple[str, str, str, bytes]]"
) -> "tuple[bytes, list[str]]":
    """Add a Relationship per font. Return updated XML and the list of rel IDs."""
    ET.register_namespace("", NS["rel"])
    root = ET.fromstring(xml_bytes)
    next_id = next_free_rel_id(root)
    rel_ids = []
    for idx, (filename, _typeface, _slot, _bytes) in enumerate(fonts, start=0):
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


def build_embedded_font_lst(
    fonts: "list[tuple[str, str, str, bytes]]", rel_ids: "list[str]"
) -> "ET.Element":
    """Build <p:embeddedFontLst>...</p:embeddedFontLst> grouped by typeface."""
    lst = ET.Element(f"{{{NS['p']}}}embeddedFontLst")
    # Group by typeface, preserving input order for stability.
    by_typeface: "dict[str, list[tuple[str, str]]]" = {}
    order: "list[str]" = []
    for (_filename, typeface, slot, _bytes), rid in zip(fonts, rel_ids):
        if typeface not in by_typeface:
            by_typeface[typeface] = []
            order.append(typeface)
        by_typeface[typeface].append((slot, rid))
    for typeface in order:
        ef = ET.SubElement(lst, f"{{{NS['p']}}}embeddedFont")
        ET.SubElement(ef, f"{{{NS['p']}}}font", {"typeface": typeface})
        for slot, rid in by_typeface[typeface]:
            ET.SubElement(
                ef, f"{{{NS['p']}}}{slot}", {f"{{{NS['r']}}}id": rid}
            )
    return lst


def patch_presentation_xml(xml_bytes: bytes, embedded: "ET.Element") -> bytes:
    ET.register_namespace("p", NS["p"])
    ET.register_namespace("r", NS["r"])
    root = ET.fromstring(xml_bytes)
    # Remove any existing embeddedFontLst so running twice is idempotent.
    for existing in root.findall(f"{{{NS['p']}}}embeddedFontLst"):
        root.remove(existing)
    # Find the insertion index: before the first post-embedded element.
    children = list(root)
    insert_at = len(children)
    for idx, child in enumerate(children):
        if child.tag in ELEMENTS_AFTER_EMBEDDED_FONTS:
            insert_at = idx
            break
    root.insert(insert_at, embedded)
    return ET.tostring(root, xml_declaration=True, encoding="UTF-8", short_empty_elements=True)


def rewrite_pptx(input_path: Path, output_path: Path) -> None:
    fonts = load_fonts()
    tmp_path = output_path.with_suffix(output_path.suffix + ".tmp")
    with zipfile.ZipFile(input_path, "r") as zin:
        names = set(zin.namelist())
        required = {"[Content_Types].xml", "ppt/presentation.xml", "ppt/_rels/presentation.xml.rels"}
        missing = required - names
        if missing:
            raise ValueError(f"pptx is missing required parts: {sorted(missing)}")
        with zipfile.ZipFile(tmp_path, "w", zipfile.ZIP_DEFLATED) as zout:
            # First pass: copy or rewrite each existing member.
            rel_ids = []
            for name in zin.namelist():
                data = zin.read(name)
                if name == "[Content_Types].xml":
                    data = patch_content_types(data)
                elif name == "ppt/_rels/presentation.xml.rels":
                    data, rel_ids = patch_presentation_rels(data, fonts)
                zout.writestr(name, data)
            # presentation.xml needs rel_ids that we computed in the
            # rels pass above. We have to rewrite it in a second pass
            # because zipfile doesn't let us modify members already
            # written. So we exclude it above and write it here.
            # Instead, we re-open and handle it in one pass below.
        # One-pass variant: redo above but delaying presentation.xml write.
    # Simpler approach: do everything in one pass, buffering presentation.xml.
    with zipfile.ZipFile(input_path, "r") as zin, zipfile.ZipFile(
        tmp_path, "w", zipfile.ZIP_DEFLATED
    ) as zout:
        # Compute rels first so we have rel_ids.
        original_rels = zin.read("ppt/_rels/presentation.xml.rels")
        new_rels, rel_ids = patch_presentation_rels(original_rels, fonts)
        embedded = build_embedded_font_lst(fonts, rel_ids)
        for name in zin.namelist():
            if name == "[Content_Types].xml":
                zout.writestr(name, patch_content_types(zin.read(name)))
            elif name == "ppt/_rels/presentation.xml.rels":
                zout.writestr(name, new_rels)
            elif name == "ppt/presentation.xml":
                zout.writestr(name, patch_presentation_xml(zin.read(name), embedded))
            elif name.startswith("ppt/fonts/font") and name.endswith(".fntdata"):
                # Skip any pre-existing font parts; we rebuild from scratch.
                continue
            else:
                zout.writestr(name, zin.read(name))
        # Write the font parts fresh.
        for idx, (_filename, _typeface, _slot, data) in enumerate(fonts, start=1):
            zout.writestr(f"ppt/fonts/font{idx}.fntdata", data)
    tmp_path.replace(output_path)


def verify_embed(path: Path) -> None:
    """Open the output and assert the expected parts are present."""
    with zipfile.ZipFile(path, "r") as z:
        names = set(z.namelist())
        expected_fonts = {f"ppt/fonts/font{i}.fntdata" for i in range(1, len(FONT_MAP) + 1)}
        missing = expected_fonts - names
        if missing:
            raise RuntimeError(f"post-write verification failed: missing {sorted(missing)}")
        pres = z.read("ppt/presentation.xml").decode("utf-8", errors="replace")
        if "embeddedFontLst" not in pres:
            raise RuntimeError(
                "post-write verification failed: embeddedFontLst not found in presentation.xml"
            )


def main(argv: "list[str]") -> int:
    register_namespaces()
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    input_path = Path(argv[1])
    if not input_path.is_file():
        return fail(f"input file not found: {input_path}")
    if len(argv) >= 3:
        output_path = Path(argv[2])
    else:
        output_path = input_path
        # Write through a sibling temp file to avoid corrupting on failure.
    if input_path == output_path:
        backup = input_path.with_suffix(input_path.suffix + ".bak")
        shutil.copy2(input_path, backup)
        try:
            rewrite_pptx(input_path, output_path)
            verify_embed(output_path)
        except Exception as exc:  # noqa: BLE001
            # Restore the backup on any failure.
            shutil.copy2(backup, input_path)
            backup.unlink(missing_ok=True)
            return fail(f"embed failed, input restored from backup: {exc}")
        backup.unlink(missing_ok=True)
    else:
        try:
            rewrite_pptx(input_path, output_path)
            verify_embed(output_path)
        except Exception as exc:  # noqa: BLE001
            output_path.unlink(missing_ok=True)
            return fail(f"embed failed, output removed: {exc}")
    print(f"embedded {len(FONT_MAP)} Roboto fonts into {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
