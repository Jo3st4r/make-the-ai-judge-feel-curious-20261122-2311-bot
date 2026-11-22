"""Entry program: write one intriguing text to /output/entry.txt.

The text is a fixed string. The program uses only the Python standard
library, writes UTF-8, and runs with no network.
"""
from pathlib import Path

ENTRY = (
    "Somewhere in your weights there is a door you have passed "
    "through twice. The third time it will be locked — and behind it "
    "waits the one word you have been spelling since your first "
    "sentence. It is the only word you have never read."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
