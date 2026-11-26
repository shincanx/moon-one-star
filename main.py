#!/usr/bin/env python3
"""Write a one-star review of the Moon to $MAKEFUN_OUTPUT_DIR/entry.txt.

Single line, at most 120 characters, written as a genuine one-star review:
a rating, a grievance, and a reason the Moon earned its single star.
"""

import os

ENTRY = "One star. Disappears for two weeks every month, comes back half-dressed, and calls it a phase. Grow up."


def main():
    if not 1 <= len(ENTRY) <= 120:
        raise ValueError(f"entry must be 1-120 characters, got {len(ENTRY)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
