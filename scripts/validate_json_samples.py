#!/usr/bin/env python3
"""Parse every JSON file in the repository."""
from pathlib import Path
import json
import sys

try:
    from repo_paths import should_skip_path
except ImportError:  # pragma: no cover
    def should_skip_path(path) -> bool:
        return any(part in {'.git', 'node_modules', '.vitepress', '.cache', '.npm', 'dist', 'coverage', 'build', '__pycache__'} for part in path.parts)

ROOT = Path(__file__).resolve().parents[1]
errors = []
for path in sorted(ROOT.rglob('*.json')):
    rel = path.relative_to(ROOT)
    if should_skip_path(rel):
        continue
    try:
        json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{rel}: {exc}')

if errors:
    print('JSON sample validation failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)
print('JSON sample validation passed.')
