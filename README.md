# Clean-Python

A Claude Code plugin of battle-tested Python skills, plus a pre-commit harness that reviews your code against them before every commit.

Skills are guidance Claude loads on demand. These five encode a specific, opinionated way of writing Python: readable, well-structured, and tested. Install once, and Claude applies them while it writes and reviews code in any project.

## Why Clean-Python?

Most Python guidance is generic and easy to ignore. A linter catches formatting, but not whether a class does too much, whether a constant should be shared, or whether a growing `if/elif` should have been a strategy. Those are judgment calls, and judgment is exactly what gets dropped under deadline.

Clean-Python turns one engineer's hard-won conventions into rules Claude follows by default, then backs them with a pre-commit review so they hold even when you forget. Not opinions in a style guide nobody reads: standards applied as you write, and checked before you commit.

## Skills

| Skill | Activates on | Enforces |
|-------|--------------|----------|
| `python-clean-code` | refactor, naming, comments, code smells | Readability: naming, comments, functions-vs-classes, data types, DRY/KISS/YAGNI |
| `python-design-principles` | SOLID, coupling, strategy, abstractions | Structure: SOLID, coupling/cohesion, Strategy over branch-on-type |
| `python-testing-tdd` | tests, pytest, TDD, fixtures, coverage | Red-Green-Refactor with quality pytest patterns |
| `python-code-review` | review, pre-merge, check my code | Review Pyramid, priority-first review |
| `python-anti-patterns` | import order, file length, hardcoded values | Module organization: import order, file size, cohesion, centralized constants |

## Install

```
/plugin marketplace add JoseVelazcoH/python-skills
/plugin install python-skills@clean-python
```

Skills auto-activate by context once installed. No further setup.

## Pre-commit harness

A reusable command, `/python-skills:review-rules`, reviews a Python diff against the skill rules and reports violations. Wire it into any project so commits are blocked when code breaks the rules.

```
cp assets/pre-commit.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

On each commit, the hook pipes the staged diff to Claude in headless mode and blocks if violations are found. Requires `claude` and `jq` on PATH. Bypass once with `git commit --no-verify`.

This is an LLM review: non-deterministic, with per-commit latency and token cost. It catches judgment-level rules (cohesion, SOLID, hardcoded values) that a linter cannot. For the mechanical subset (import order, file length), pair it with a linter.

## Layout

```
skills/         the five skills, each a SKILL.md plus references
commands/       review-rules.md, the diff-review command
assets/         pre-commit.sh, the portable git hook
bin/            validate_skills.py, validates SKILL.md structure
.claude-plugin/ plugin and marketplace manifests
```

## Editing skills

Edit a `SKILL.md`, run `python bin/validate_skills.py` to check frontmatter and structure, commit, and consumers get the update via `/plugin update`. A local pre-commit hook runs the validator automatically.

## License

Released under the [Apache-2.0](LICENSE) license.
