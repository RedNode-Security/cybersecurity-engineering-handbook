#!/usr/bin/env python3
"""Check Markdown front matter for pages marked reviewed or published without updated date."""
from pathlib import Path
import re
import sys

try:
    from repo_paths import should_skip_path
except ImportError:  # pragma: no cover
    def should_skip_path(path) -> bool:
        return any(part in {'.git', 'node_modules', '.vitepress', '.cache', '.npm', 'dist', 'coverage', 'build', '__pycache__'} for part in path.parts)

ROOT = Path(__file__).resolve().parents[1]
errors = []
for path in sorted(ROOT.rglob('*.md')):
    rel = path.relative_to(ROOT)
    if should_skip_path(rel):
        continue
    text = path.read_text(encoding='utf-8', errors='replace')
    if not text.startswith('---'):
        continue
    status = re.search(r'^status:\s*(reviewed|published)\s*$', text, re.MULTILINE)
    if status and not re.search(r'^updated:\s*\d{4}-\d{2}-\d{2}\s*$', text, re.MULTILINE):
        errors.append(f'{rel}: reviewed/published page missing updated date')
if errors:
    print('Review date check failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)
print('Review date check passed.')
