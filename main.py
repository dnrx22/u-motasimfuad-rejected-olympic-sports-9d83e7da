#!/usr/bin/env python3
"""Rejected Olympic Sports — one line: a sport the Olympics rejected.

Writes a single deadpan broadcast-style line describing a made-up
Olympic event to entry.txt. Stdlib only, no network, deterministic.
"""

import os
import sys

LINE = (
    "Extreme ironing relay: four athletes iron a shirt while abseiling "
    "down a cliff \u2014 fastest wrinkle-free shirt wins."
)


def validate(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > 200:
        raise ValueError(
            f"line is {len(line)} Unicode code points, over the 200 limit"
        )
    words = line.split()
    if len(words) > 20:
        raise ValueError(f"line has {len(words)} words, over the 20 limit")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = (LINE + "\n").encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
