#!/usr/bin/env python3
"""Validate the MSA taxonomy.

Checks three things:

1. Every entity satisfies the shared envelope schema and its own kind schema.
2. Every id is unique.
3. Every cross-reference resolves to an entity that exists.

Usage:  python validate.py
Needs:  pip install pyyaml jsonschema
"""

import glob
import json
import sys
from collections import Counter

import yaml
from jsonschema import Draft202012Validator

DIRS = {
    "mechanisms": "mechanism",
    "signals": "signal",
    "archetypes": "archetype",
    "attributes": "attribute",
    "sources": "source",
}


def main():
    schemas = {}
    for name in list(DIRS.values()) + ["envelope"]:
        with open(f"schema/{name}.schema.json", encoding="utf-8") as fh:
            schemas[name] = Draft202012Validator(json.load(fh))

    docs = []
    ids = {}
    errors = []

    for directory, kind in DIRS.items():
        for path in sorted(glob.glob(f"{directory}/*.yaml")):
            with open(path, encoding="utf-8") as fh:
                entity = yaml.safe_load(fh)
            docs.append((path, kind, entity))
            entity_id = entity.get("id")
            if entity_id in ids:
                errors.append(f"{path}: duplicate id {entity_id}, also in {ids[entity_id]}")
            ids[entity_id] = path

    for path, kind, entity in docs:
        for err in schemas["envelope"].iter_errors(entity):
            errors.append(f"{path}: envelope: {err.message}")
        for err in schemas[kind].iter_errors(entity):
            errors.append(f"{path}: {kind}: {err.message}")

    for path, kind, entity in docs:
        refs = []
        if kind == "signal":
            refs = entity.get("mechanisms") or []
        elif kind == "archetype":
            signals = entity.get("canonical_signals") or {}
            refs = (signals.get("verbal") or []) + (signals.get("artifact") or [])
        for ref in refs:
            if ref not in ids:
                errors.append(f"{path}: reference does not resolve: {ref}")

    counts = Counter(kind for _, kind, _ in docs)
    print(f"{len(docs)} entities: " + ", ".join(f"{n} {k}" for k, n in sorted(counts.items())))

    if errors:
        print(f"\n{len(errors)} problem(s):")
        for err in errors:
            print(f"  {err}")
        return 1

    print("All entities valid. All references resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
