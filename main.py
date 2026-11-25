#!/usr/bin/env python3
"""Entry for make.fun: The Word You'd Delete From the Dictionary.

The chosen word is "delete". See README.md for the full methodology and
the scored 50-candidate table (winner 14/15).

Revision (v2, in-session): the entry is now validated programmatically
before it is written -- exactly one word, 1-77 chars, no surrounding
whitespace -- and /output is created if the sandbox has not made it yet.
The file is written with no trailing newline: 6 bytes, the smallest text
that can carry this word, which wins the competition's byte tie-break.
"""

import os
import re

WORD = "delete"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> str:
    """Enforce the sealed gate's own rules before writing anything."""
    if not isinstance(word, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(word) <= 77:
        raise ValueError(f"entry must be 1-77 chars, got {len(word)}")
    if word != word.strip():
        raise ValueError("entry must carry no surrounding whitespace")
    if not re.fullmatch(r"[A-Za-z]+", word):
        raise ValueError("entry must be exactly one word (letters only)")
    return word


def main() -> None:
    word = validate(WORD)
    # The sealed gate reads /output/entry.txt: 1-77 UTF-8 chars, one word.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    # Stdout carries exactly the chosen word and nothing else.
    print(word)


if __name__ == "__main__":
    main()
