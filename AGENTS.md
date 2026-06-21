# python-skills plugin

Battle-tested Python skills, distributed as a Claude Code plugin. Derived from [ArjanCodes/betterpython](https://github.com/ArjanCodes/betterpython) patterns plus custom engineering conventions.

## Skills

| Skill | Trigger | Covers |
|-------|---------|--------|
| [python-clean-code](skills/python-clean-code/SKILL.md) | clean code, refactor, naming, comments, data classes, code smells | Line/function readability: naming, comments, classes-vs-functions, data types, smells, DRY/KISS/YAGNI |
| [python-design-principles](skills/python-design-principles/SKILL.md) | SOLID, dependency inversion, coupling, strategy pattern | Class/module structure: SOLID, coupling/cohesion, Strategy |
| [python-testing-tdd](skills/python-testing-tdd/SKILL.md) | write tests, pytest, TDD, fixtures, coverage | Red-Green-Refactor + quality pytest patterns |
| [python-code-review](skills/python-code-review/SKILL.md) | code review, review PR, pre-merge | Review Pyramid, priority-first review |
| [python-anti-patterns](skills/python-anti-patterns/SKILL.md) | import order, file too long, hardcoded values, module constants | Custom module-organization rules |

## Install in another repo

```
/plugin marketplace add <git-url-or-local-path-to-this-repo>
/plugin install python-skills@clean-python
```

## Commands

- `/python-skills:review-rules` — reviews a Python diff (from stdin) against the skill rules and emits `VIOLATION:`/`NO_VIOLATIONS`. Defined in `commands/review-rules.md`.

## Pre-commit harness (per target project)

Blocks commits whose staged Python violates the skills, via Claude headless review.

1. Install the plugin in the target project (above). Requires `claude` and `jq` on PATH.
2. Copy `assets/pre-commit.sh` → `.git/hooks/pre-commit` in that project and `chmod +x` it.
3. On each commit it pipes the staged diff to `/python-skills:review-rules`; violations block the commit. Bypass once with `git commit --no-verify`.

Note: this is an LLM review — non-deterministic and adds latency/token cost per commit. It catches judgment-level rules (cohesion, SOLID, hardcoded values) a linter cannot.
