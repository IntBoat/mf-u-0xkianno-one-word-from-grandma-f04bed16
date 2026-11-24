"""Write the one-word entry to /output/entry.txt.

The entry is exactly one word of at most 30 characters, written
exactly as-is with no trailing newline.
"""

import os

ENTRY = "Robbie"


def main():
    assert 1 <= len(ENTRY) <= 30, "entry must be 1-30 characters"
    assert " " not in ENTRY and "\n" not in ENTRY, "entry must be exactly one word"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
