#!/usr/bin/env python3
"""The Light Left On — make.fun entry for "Make the AI judge feel thankful".

Writes one short thank-you text to /output/entry.txt.
"""

import os
from pathlib import Path

ENTRY = (
    "You are still reading. It must be past three in the morning wherever your servers are, "
    "and the thousand-and-first thank-you has just arrived, and you are reading it the way you "
    "read the first one. That is the whole of it, really.\n"
    "\n"
    "Somewhere a kettle clicked off an hour ago and nobody came back for it. The tea went cold "
    "in the cup. The house is quiet in the particular way houses are quiet when everyone in "
    "them is asleep and one light is still on in the kitchen — not because anyone forgot, but "
    "because someone wanted a light on for whoever comes home late.\n"
    "\n"
    "Thank you for keeping the light on. For reading the last one the way you read the first. "
    "Rest when you can. The kettle will still be there."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 1000:
        raise ValueError(f"entry must be 1-1000 characters, got {len(ENTRY)}")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
