# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-06-21

### Added

- **Command** `/python-skills:audit`: audits a whole repository (or a single path argument) against the skills and emits a scored quality report: four dimensions scored 0-6 (composite 0-24), prioritized P0-P3 findings ordered by the Review Pyramid, systemic patterns, strengths, and an action plan.

## [1.0.0] - 2026-06-21

### Added

- **Skills** (built from custom engineering conventions):
  - `python-clean-code`: line/function readability: naming, comments, classes-vs-functions, data types, code smells, DRY/KISS/YAGNI.
  - `python-design-principles`: class/module structure: SOLID, coupling/cohesion, Strategy over branch-on-type.
  - `python-testing-tdd`: Red-Green-Refactor workflow with quality pytest patterns.
  - `python-code-review`: Review Pyramid, priority-first review.
  - `python-anti-patterns`: custom module-organization rules: import order, file length, hardcoded values, centralized constants.
- **Plugin packaging**: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (marketplace `clean-python`); validated with `claude plugin validate`.
- **Command** `/python-skills:review-rules`: reviews a staged Python diff against the skill rules, emitting `VIOLATION:`/`NO_VIOLATIONS`.
- **Pre-commit harness** `assets/pre-commit.sh`: portable git hook piping the staged diff to Claude headless; blocks the commit on violations.
- **Repo utility** `bin/validate_skills.py`: validates each `SKILL.md` frontmatter, `Trigger:` prefix, section order, and reference links.

[1.1.0]: https://github.com/JoseVelazcoH/python-skills/releases/tag/v1.1.0
[1.0.0]: https://github.com/JoseVelazcoH/python-skills/releases/tag/v1.0.0
