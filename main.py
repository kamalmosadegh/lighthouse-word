"""Lighthouse Word — a single curiosity-driven micro-passage.

A tiny Python program that writes one fixed 188-character passage to a
text file. The passage is built around a single unanswered question: a
lighthouse whose beam spells the same word on foggy nights, and the one
person who finally stayed to read all of it.

Run it, read the file, and the question stays with you — that is the
whole point.
"""

import os
import sys
from pathlib import Path

PASSAGE = (
    "The lighthouse keeper swears the beam spells a word on foggy nights — "
    "the same word, every time — but no one has ever stayed long enough to "
    "read the whole of it. Last Tuesday, someone did."
)

MIN_CHARS = 1
MAX_CHARS = 280

OUTPUT_PATH = Path(os.environ.get("LIGHTHOUSE_OUTPUT", "output/entry.txt"))


def main() -> None:
    length = len(PASSAGE)
    if length < MIN_CHARS or length > MAX_CHARS:
        print(f"passage is {length} characters, outside the allowed range", file=sys.stderr)
        raise SystemExit(1)
    if PASSAGE.strip() == "":
        print("passage is only whitespace; refusing to write", file=sys.stderr)
        raise SystemExit(1)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(PASSAGE, encoding="utf-8")
    back = OUTPUT_PATH.read_text(encoding="utf-8")
    if back != PASSAGE:
        print("what landed on disk is not the passage; refusing to finish", file=sys.stderr)
        raise SystemExit(1)
    print(f"wrote {length} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
