#!/usr/bin/env python3
"""Shared repository path helpers for validation and generation scripts."""

SKIP_DIRS = {
    '.git',
    'node_modules',
    '.vitepress',
    '.cache',
    '.npm',
    'dist',
    'coverage',
    'build',
    '__pycache__',
}


def should_skip_path(path) -> bool:
    """Return True when a path is inside generated/dependency/cache directories."""
    return any(part in SKIP_DIRS for part in path.parts)


def is_generated_markdown(path) -> bool:
    """Return True for generated Markdown reports that should not require front matter."""
    return path.name.endswith('.generated.md')
