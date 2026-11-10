"""Configuration tree comparison."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class DiffEntry:
    path: str
    left: Any
    right: Any

    def describe(self) -> str:
        return f"{self.path}: {self.left!r} -> {self.right!r}"


def _walk(node: dict, prefix: str = ""):
    for key, value in node.items():
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            yield from _walk(value, path)
        else:
            yield path, value


def diff_trees(left: dict, right: dict) -> list[DiffEntry]:
    left_flat = dict(_walk(left))
    right_flat = dict(_walk(right))
    entries: list[DiffEntry] = []
    for path in sorted(set(left_flat) | set(right_flat)):
        if left_flat.get(path) != right_flat.get(path):
            entries.append(DiffEntry(path, left_flat.get(path), right_flat.get(path)))
    return entries
