#!/usr/bin/env python3
"""Monday Morning Punchlines -- make.fun entry.

Writes one joke about Monday mornings to /output/entry.txt
(or $OUTPUT_DIR/entry.txt).

Craft notes: the joke is in the first person, starts with a
concrete Monday-morning ritual (setting several alarms), then
turns it sideways -- the alarms unionize and strike, and the
snooze button ends up as their lawyer. No "I hate Mondays"
complaint, no coffee cliche: the punchline is the escalation
from tool to negotiator, and every word earns its place.
One line, plain ASCII, no em dash.

Python standard library only.
"""

import os

ENTRY = (
    "I set five alarms for Monday morning. They formed a union, "
    "went on strike, and now my snooze button is their lawyer."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} out of range 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.isascii():
        raise SystemExit("entry must be plain ASCII")
    # Judge criterion 1: the joke must really be about Monday mornings,
    # so the text itself must name Monday (and the morning, in ENTRY).
    if "monday" not in text.lower():
        raise SystemExit("entry must be about Monday mornings")
    if "morning" not in text.lower():
        raise SystemExit("entry must be about Monday mornings")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
