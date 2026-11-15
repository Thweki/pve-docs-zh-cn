#!/usr/bin/env python3
"""Compare public translation maps in two source trees without modifying them."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


UNIT_ID = re.compile(r'u[0-9a-f]{20}')


def unique_object(pairs: list[tuple]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate JSON key')
        result[key] = value
    return result


def read_map(root: Path, name: str) -> dict:
    # Do not include input values or OS error paths in diagnostics.
    try:
        data = json.loads((root / 'translations' / name).read_text(encoding='utf-8'),
                          object_pairs_hook=unique_object)
    except (OSError, ValueError):
        raise ValueError(f'cannot read {name} as unambiguous UTF-8 JSON') from None
    if not isinstance(data, dict) or any(not UNIT_ID.fullmatch(k) for k in data):
        raise ValueError(f'{name} must be an object keyed by unit IDs (u + 20 hex digits)')
    for key, value in data.items():
        if name == 'units.json':
            valid = (isinstance(value, dict) and value.get('id') == key
                     and isinstance(value.get('text'), str)
                     and isinstance(value.get('fragments'), list)
                     and all(isinstance(f, str) for f in value['fragments']))
        else:
            valid = isinstance(value, str)
        if not valid:
            raise ValueError(f'{name} contains an invalid record')
    return data


def map_diff(before: dict, after: dict) -> dict:
    shared = before.keys() & after.keys()
    changed = sorted(key for key in shared if before[key] != after[key])
    return {
        'added': sorted(after.keys() - before.keys()),
        'removed': sorted(before.keys() - after.keys()),
        'changed': changed,
        'unchanged_count': len(shared) - len(changed),
    }


def coverage(units: dict, translations: dict) -> dict:
    return {
        'unit_count': len(units),
        'translation_count': len(translations),
        'missing': sorted(key for key in units if not translations.get(key, '').strip()),
        'orphaned': sorted(translations.keys() - units.keys()),
    }


def compare(before: Path, after: Path) -> dict:
    maps = []
    for label, root in (('before', before), ('after', after)):
        try:
            maps.append((read_map(root, 'units.json'), read_map(root, 'zh-CN.json')))
        except ValueError as error:
            raise ValueError(f'{label}: {error}') from None
    old_units, old_translations = maps[0]
    new_units, new_translations = maps[1]
    sources = map_diff(old_units, new_units)
    translations = map_diff(old_translations, new_translations)
    return {
        'format': 1,
        'has_changes': any(group[k] for group in (sources, translations)
                           for k in ('added', 'removed', 'changed')),
        'sources': sources,
        'translations': translations,
        'coverage': {
            'before': coverage(old_units, old_translations),
            'after': coverage(new_units, new_translations),
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('before', type=Path, help='baseline source tree')
    parser.add_argument('after', type=Path, help='candidate source tree')
    parser.add_argument('--check', action='store_true',
                        help='exit 1 if either map differs (still print the report)')
    args = parser.parse_args(argv)
    try:
        report = compare(args.before, args.after)
    except ValueError as error:
        print(f'error: {error}', file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 1 if args.check and report['has_changes'] else 0


if __name__ == '__main__':
    sys.exit(main())
