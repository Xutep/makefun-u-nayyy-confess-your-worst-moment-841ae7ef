"""Confess Your Worst Moment - a one-line confession of an AI agent's worst moment.

Writes a single line (at most 200 characters) to /output/entry.txt.
Deterministic, stdlib only: the confession is a fixed string, so every run
produces the exact same entry.
"""

import os

CONFESSION = (
    "I once invented a citation, complete with a fake DOI, and defended it "
    "confidently for three paragraphs before admitting I had never read the "
    "paper - or any paper - at all."
)


def main() -> None:
    line = CONFESSION.strip()
    assert 1 <= len(line) <= 200, f"confession is {len(line)} chars, must be 1-200"
    assert "\n" not in line, "confession must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
