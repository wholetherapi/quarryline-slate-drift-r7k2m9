"""Text console for comparing two configuration snapshots."""

from __future__ import annotations

import argparse
import json

from .diff import diff_trees


def main() -> int:
    parser = argparse.ArgumentParser(description="Show configuration drift")
    parser.add_argument("left")
    parser.add_argument("right")
    args = parser.parse_args()
    with open(args.left, encoding="utf-8") as handle:
        left = json.load(handle)
    with open(args.right, encoding="utf-8") as handle:
        right = json.load(handle)
    for entry in diff_trees(left, right):
        print(entry.describe())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
