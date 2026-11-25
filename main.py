#!/usr/bin/env python3
"""The Router Confesses — one-line entry.

Writes the router's excuse to /output/entry.txt.
No arguments, no network, no external files.
"""

import os

LINE = "I dropped the connection because the killer is the butler and I refuse to be the one who spoils it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
