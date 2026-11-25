#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

LINE = "I asked the barista for the strongest thing she had. She handed me her resignation letter."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
