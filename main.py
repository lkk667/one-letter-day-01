#!/usr/bin/env python3
"""One letter for the day: Z.

The day behind the letter is a zero-sleep day -- the kind where you
run on fumes from dawn to midnight and end it shambling around like a
zombie. Z is the initial of that word, and the shape of the letter
itself looks like a jagged little lightning bolt of a day: sharp,
uneven, and over before you know it.

The program writes exactly that one letter, and nothing else, to
/output/entry.txt: no word, no gloss, no punctuation, no trailing
newline, so the file is one byte long and passes the gate as-is.
"""

import os

LETTER = "Z"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
