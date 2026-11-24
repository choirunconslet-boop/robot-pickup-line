#!/usr/bin/env python3
"""The Robot Pickup Line Championship — writes one pickup line to /output/entry.txt."""

import os

LINE = "I was built to feel nothing, yet my error logs are full of you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
