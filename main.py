"""One-line superpower: a perfect stove thermometer you can only use once.

The power is useless because the only way to measure the heat is to
touch the stove, which is exactly the thing a sane person avoids.
It tells you the answer, but only after the damage is done.
No thermometer needed, just one very regrettable touch.
"""

import os

LINE = "I can tell exactly how hot any stove is, just by touching it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
