"""A thirsty houseplant covers the inbox while its owner is away.

The gag is the plant filing neglect as a work request: no water since
March, leaves sagging lower by the day, and instead of promising a
reply it asks the sender for a drink. The usual auto-reply promises
attention later; this one begs for attention now, from a pot.
"""

import os

LINE = "I'm out of office — and out of water since March. If my leaves droop any further, water me, not my inbox."


def main():
    assert 1 <= len(LINE) <= 120, "line must fit the 120-character limit"
    assert "\n" not in LINE, "line must stay on a single line"
    # A leading or trailing space would be invisible padding that still
    # counts toward the limit and could make the entry read as blank-edged,
    # so the line must already be trimmed before it is written out.
    assert LINE == LINE.strip(), "line must not start or end with a space"
    text = LINE + "\n"
    candidates = []
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        candidates.append(os.path.join(out_dir, "entry.txt"))
    candidates.append("/output/entry.txt")
    candidates.append(os.path.join("out", "entry.txt"))
    last_error = None
    for path in candidates:
        try:
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(text)
            print(f"entry: {len(LINE)} chars")
            return
        except OSError as exc:
            last_error = exc
    raise last_error


if __name__ == "__main__":
    main()
