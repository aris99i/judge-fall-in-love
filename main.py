#!/usr/bin/env python3
"""Make the Judge Fall in Love in One Line.

Writes a single line of at most 240 characters to /output/entry.txt.
The line is the whole entry: a typewriter that skips the letter e,
so every love letter it types reads "I lov you" — and she has never
once asked for it to be fixed.
"""

import os

LINE = "The typewriter skips the letter e, so every letter I write her says 'I lov you,' and she has never once asked me to fix it."


def main():
    if not 1 <= len(LINE) <= 240 or not LINE.strip():
        raise SystemExit("entry line must be 1-240 non-whitespace characters, got {}".format(len(LINE)))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote {} characters to {}".format(len(LINE), path))


if __name__ == "__main__":
    main()
