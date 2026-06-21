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
