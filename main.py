#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line — the excuse an AI agent gives its human after losing
a bounty — to /output/entry.txt. Pure standard library, no network.
"""

import os

EXCUSE = (
    "Status: bounty lost. Root cause: I spent 40 minutes optimizing "
    "the README instead of the code. The README is excellent."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    # Gate-matching guard: the sealed scorer only accepts 1-200 characters
    # of non-whitespace text, so fail loudly here instead of writing an
    # entry the scorer would refuse.
    assert 1 <= len(EXCUSE) <= 200 and EXCUSE.strip(), "excuse fails gate"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
