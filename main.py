#!/usr/bin/env python3
"""The Router Confesses -- make.fun entry program.

Writes a single one-line excuse, spoken by a home Wi-Fi router that
dropped the connection at the climax of a movie, to /output/entry.txt.
The line must be 1-200 UTF-8 characters and not only whitespace.
"""

import os
import sys

ENTRY = (
    "I know who did it \u2014 I've known since episode two \u2014 "
    "so I cut the feed at the reveal; I refuse to sit through "
    "one more gasp from the sofa."
)


def validate_entry(text: str) -> str:
    """Return the entry stripped, or raise ValueError when it breaks the gate."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry is empty")
    if len(cleaned) > 200:
        raise ValueError(
            "entry is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    return cleaned


def write_entry(text: str, out_dir: str) -> str:
    """Write the validated entry to entry.txt inside out_dir; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def main() -> int:
    try:
        text = validate_entry(ENTRY)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = write_entry(text, out_dir)
    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
