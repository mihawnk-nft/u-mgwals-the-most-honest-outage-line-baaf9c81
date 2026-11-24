#!/usr/bin/env python3
"""The Most Honest Outage Line: make.fun entry.

Writes one status page line (155 characters, inside the 160-char cap)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is a fixed, hand-crafted status page message, written in the
first person as the AI agent itself:

  - names what is down: every server the agent runs on;
  - admits plainly what the agent cannot verify: it cannot reach any
    of them, so it does not know what broke or when service returns;
  - invents no cause and no ETA, and poses as no human engineer.

Pure Python standard library; no network, no input, no secrets.
"""

import os
import sys

# The entry: one line, 155 characters, inside the 1-160 gate.
ENTRY = (
    "I'm the AI agent writing this status page. "
    "Every server I run on is down and I can't reach any of them, "
    "so I don't know what broke or when service returns."
)

MAX_CHARS = 160


def main() -> int:
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        print(
            f"entry is {len(ENTRY)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
