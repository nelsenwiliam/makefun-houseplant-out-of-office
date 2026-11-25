#!/usr/bin/env python3
"""The Houseplant Out-of-Office -- make.fun bounty entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. The line is exactly 105 characters, written
with no trailing newline so the file holds exactly the reply.
Pure Python standard library, no imports beyond pathlib.
"""

from pathlib import Path

LINE = "I'm out of office — and out of water since March. If my leaves droop any further, water me, not my inbox."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
