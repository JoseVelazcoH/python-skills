#!/usr/bin/env python3
"""Validate every SKILL.md against the repo's skill-authoring rules.

Standalone, no third-party dependencies. Exit code 0 = all pass, 1 = violations.
Run manually (`python bin/validate_skills.py`) or via the pre-commit hook.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"

REQUIRED_FRONTMATTER_KEYS = ("name", "description", "license")
REQUIRED_METADATA_KEYS = ("author", "version")
REQUIRED_SECTIONS = (
    "Activation Contract",
    "Hard Rules",
    "Decision Gates",
    "Execution Steps",
    "Output Contract",
    "References",
)
DESCRIPTION_MAX_CHARS = 250
TRIGGER_PREFIX = "Trigger:"
FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
REFERENCE_LINK_PATTERN = re.compile(r"`(references/[^`]+)`")


def parse_frontmatter(raw: str) -> dict[str, str] | None:
    """Extract top-level and metadata.* keys with a minimal flat parser."""
    match = FRONTMATTER_PATTERN.match(raw)
    if not match:
        return None
    fields: dict[str, str] = {}
    in_metadata = False
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        if line.startswith("metadata:"):
            in_metadata = True
            continue
        if in_metadata and line.startswith("  ") and ":" in line:
            key, _, value = line.strip().partition(":")
            fields[f"metadata.{key.strip()}"] = value.strip().strip('"')
        elif not line.startswith(" ") and ":" in line:
            in_metadata = False
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip('"')
    return fields


def check_skill(skill_md: Path) -> list[str]:
    """Return a list of rule violations for one SKILL.md (empty = valid)."""
    errors: list[str] = []
    raw = skill_md.read_text(encoding="utf-8")
    fields = parse_frontmatter(raw)

    if fields is None:
        return ["missing or malformed frontmatter (--- ... --- block)"]

    for key in REQUIRED_FRONTMATTER_KEYS:
        if key not in fields:
            errors.append(f"frontmatter missing required key: {key}")
    for key in REQUIRED_METADATA_KEYS:
        if f"metadata.{key}" not in fields:
            errors.append(f"frontmatter missing required key: metadata.{key}")

    name = fields.get("name", "")
    if name and name != skill_md.parent.name:
        errors.append(f"name '{name}' does not match directory '{skill_md.parent.name}'")

    description = fields.get("description", "")
    if description and not description.startswith(TRIGGER_PREFIX):
        errors.append(f"description must start with '{TRIGGER_PREFIX}'")
    if len(description) > DESCRIPTION_MAX_CHARS:
        errors.append(
            f"description is {len(description)} chars (max {DESCRIPTION_MAX_CHARS})"
        )

    body = raw[FRONTMATTER_PATTERN.match(raw).end():]
    found = [s for s in REQUIRED_SECTIONS if f"## {s}" in body]
    if found != [s for s in REQUIRED_SECTIONS if s in found]:
        errors.append("sections present but out of required order")
    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in body:
            errors.append(f"missing required section: ## {section}")

    for rel_link in REFERENCE_LINK_PATTERN.findall(body):
        if not (skill_md.parent / rel_link).exists():
            errors.append(f"reference points to missing file: {rel_link}")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"ERROR: skills directory not found at {SKILLS_DIR}")
        return 1

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        print(f"ERROR: no SKILL.md files found under {SKILLS_DIR}")
        return 1

    total_errors = 0
    for skill_md in skill_files:
        errors = check_skill(skill_md)
        label = skill_md.parent.name
        if errors:
            total_errors += len(errors)
            print(f"✗ {label}")
            for error in errors:
                print(f"    - {error}")
        else:
            print(f"✓ {label}")

    print()
    if total_errors:
        print(f"FAILED: {total_errors} violation(s) across {len(skill_files)} skills.")
        return 1
    print(f"OK: {len(skill_files)} skills pass all checks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
