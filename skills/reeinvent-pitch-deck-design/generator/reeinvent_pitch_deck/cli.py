"""reeinvent-deck CLI.

Subcommands:
  build  <spec.json> [-o OUTPUT.pptx]   Build a deck from a JSON spec.
  verify <DECK.pptx>                    Run brand pre-flight checks.
  embed  <DECK.pptx>                    Inject Roboto fonts (post-process only).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _cmd_build(args) -> int:
    from reeinvent_pitch_deck.build import build_deck
    from reeinvent_pitch_deck.spec import SpecError, load_spec

    spec_path = Path(args.spec)
    if not spec_path.is_file():
        print(f"reeinvent-deck: spec not found: {spec_path}", file=sys.stderr)
        return 1
    try:
        deck = load_spec(spec_path)
    except SpecError as exc:
        print(f"reeinvent-deck: invalid spec: {exc}", file=sys.stderr)
        return 1

    output = Path(args.output) if args.output else spec_path.with_suffix(".pptx")
    try:
        out = build_deck(deck, output, skip_font_embed=args.skip_font_embed)
    except Exception as exc:
        print(f"reeinvent-deck: build failed: {exc}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        return 1

    if not args.no_verify and not args.skip_font_embed:
        from reeinvent_pitch_deck.verify import VerificationError, verify_deck
        try:
            verify_deck(out)
        except VerificationError as exc:
            print(f"reeinvent-deck: verification failed: {exc}", file=sys.stderr)
            return 2

    size_kb = out.stat().st_size // 1024
    print(f"reeinvent-deck: wrote {out} ({size_kb} KB, {len(deck.slides)} slides)")
    return 0


def _cmd_verify(args) -> int:
    from reeinvent_pitch_deck.verify import VerificationError, verify_deck
    try:
        verify_deck(Path(args.deck))
    except VerificationError as exc:
        print(f"reeinvent-deck: {exc}", file=sys.stderr)
        return 2
    except FileNotFoundError as exc:
        print(f"reeinvent-deck: {exc}", file=sys.stderr)
        return 1
    print(f"reeinvent-deck: OK {args.deck}")
    return 0


def _cmd_embed(args) -> int:
    from reeinvent_pitch_deck.embed import embed_fonts
    try:
        out = embed_fonts(Path(args.deck), Path(args.output) if args.output else None)
    except Exception as exc:
        print(f"reeinvent-deck: embed failed: {exc}", file=sys.stderr)
        return 1
    print(f"reeinvent-deck: embedded Roboto into {out}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="reeinvent-deck", description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)

    pb = sub.add_parser("build", help="Build a .pptx from a JSON spec")
    pb.add_argument("spec", help="path to the JSON spec file")
    pb.add_argument("-o", "--output", help="output .pptx path (default: spec basename with .pptx)")
    pb.add_argument("--skip-font-embed", action="store_true", help="skip the Roboto post-embed step (test use only)")
    pb.add_argument("--no-verify", action="store_true", help="skip pre-flight checks after build")
    pb.add_argument("-v", "--verbose", action="store_true", help="print full traceback on failure")
    pb.set_defaults(func=_cmd_build)

    pv = sub.add_parser("verify", help="Run brand pre-flight checks on an existing .pptx")
    pv.add_argument("deck", help="path to the .pptx to verify")
    pv.set_defaults(func=_cmd_verify)

    pe = sub.add_parser("embed", help="Inject Roboto fonts into an existing .pptx")
    pe.add_argument("deck", help="path to the .pptx")
    pe.add_argument("-o", "--output", help="output path (default: replace input in place)")
    pe.set_defaults(func=_cmd_embed)

    args = p.parse_args(argv)
    return args.func(args)
