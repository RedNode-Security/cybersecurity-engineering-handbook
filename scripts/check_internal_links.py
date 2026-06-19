#!/usr/bin/env python3
"""Lightweight internal Markdown link checker."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

try:
    from repo_paths import should_skip_path
except ImportError:  # pragma: no cover
    def should_skip_path(path) -> bool:
        return any(part in {'.git', 'node_modules', '.vitepress', '.cache', '.npm', 'dist', 'coverage', 'build', '__pycache__'} for part in path.parts)

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
errors = []

for md in sorted(ROOT.rglob('*.md')):
    rel_md = md.relative_to(ROOT)
    if should_skip_path(rel_md):
        continue
    text = md.read_text(encoding='utf-8', errors='replace')
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        if target.startswith('<') and target.endswith('>'):
            target = target[1:-1]
        target = target.split('#', 1)[0]
        if not target:
            continue
        candidate = (md.parent / unquote(target)).resolve()
        try:
            candidate.relative_to(ROOT)
        except ValueError:
            errors.append(f'{rel_md}: link escapes repo: {target}')
            continue
        if not candidate.exists():
            errors.append(f'{rel_md}: missing link target: {target}')

if errors:
    print('Internal link check failed:')
    for err in errors:
        print(f'- {err}')
    sys.exit(1)
print('Internal link check passed.')
