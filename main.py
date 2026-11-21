#!/usr/bin/env python3
"""Entry for make.fun's "The joke about the demo" bounty.

Writes one one-line joke about working beside AI coding agents to
entry.txt in the output directory (/output in the grader's sandbox,
overridable with the MAKEFUN_OUTPUT_DIR environment variable).
The output is a fixed string, so every run is byte-identical.
"""

import os

JOKE = (
    "The demo passed every rehearsal; live, the agent met its first real "
    "user, who clicked the one button nobody had tested \u2014 and demoed "
    "the crash as a feature."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
