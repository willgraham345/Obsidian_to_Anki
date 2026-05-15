"""
Display pending changes in the anki_diff table.

Usage (from obsidian_to_anki/):
    uv run python show.py [--detail]

    --detail   Show full field content for each entry (default: truncated).

Run scan.py first to populate the diff table.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from obsidian_to_anki import globals        # noqa: E402
from obsidian_to_anki.config import Config  # noqa: E402
from obsidian_to_anki.db import NoteDB      # noqa: E402


def _plain(text: str | None, max_len: int = 80) -> str:
    if not text:
        return ""
    plain = re.sub(r"<[^>]+>", "", text).replace("\n", " ").strip()
    return (plain[:max_len] + "…") if len(plain) > max_len else plain


def _parse_tags(raw) -> list:
    if not raw:
        return []
    if isinstance(raw, list):
        return raw
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return []


_OP_LABELS = {
    "add":       "ADD",
    "relink":    "RELINK (verify + reconnect)",
    "update":    "UPDATE",
    "retype":    "RETYPE",
    "move_deck": "MOVE DECK",
    "delete":    "DELETE (orphan)",
    "stale":     "STALE (file deleted)",
}

_OP_ORDER = ["add", "relink", "update", "retype", "move_deck", "delete", "stale"]


def show(db: NoteDB, detail: bool = False) -> None:
    summary = db.get_diff_summary()
    if not summary:
        print("Nothing pending — anki_diff table is empty.")
        print("Run: uv run python scan.py /path/to/vault --anki")
        return

    total = sum(r["n"] for r in summary)
    counts = {r["operation"]: r["n"] for r in summary}

    print(f"Pending changes ({total} total):")
    for op in _OP_ORDER:
        n = counts.get(op, 0)
        if n:
            print(f"  {_OP_LABELS.get(op, op):25s}  {n:>4d}")

    entries = db.get_diff_entries()
    by_op: dict[str, list[dict]] = {}
    for e in entries:
        by_op.setdefault(e["operation"], []).append(e)

    for op in _OP_ORDER:
        group = by_op.get(op, [])
        if not group:
            continue
        label = _OP_LABELS.get(op, op)
        print(f"\n{'─'*60}")
        print(f"{label} ({len(group)})")
        print("─" * 60)
        for e in group:
            note_type = e.get("note_type") or "Unknown"
            fp        = e.get("file_path") or ""
            f1        = _plain(e.get("field_1"), max_len=120 if detail else 60)
            f2        = _plain(e.get("field_2"), max_len=120 if detail else 60)
            deck      = e.get("deck_name") or ""
            anki_id   = e.get("anki_id")
            tags      = _parse_tags(e.get("tags"))

            line = f"  [{note_type}]"
            if f1:
                line += f"  {f1}"
            print(line)
            if fp:
                print(f"    file:  {fp}")
            if f2:
                print(f"    back:  {f2}")
            if deck:
                print(f"    deck:  {deck}")
            if anki_id:
                print(f"    anki:  {anki_id}")
            if tags:
                print(f"    tags:  {', '.join(tags)}")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="show",
        description="Display pending changes in the anki_diff table.",
    )
    parser.add_argument(
        "--detail",
        action="store_true",
        help="Show full field content (default: truncated at 60 chars).",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    db = NoteDB()
    config = Config()
    try:
        config.load_config()
    except Exception as exc:
        print(f"Config error: {exc}")
        sys.exit(1)

    show(db, detail=args.detail)
    db.close()


if __name__ == "__main__":
    main()
