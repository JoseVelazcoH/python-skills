---
name: python-clean-code
description: "Trigger: clean code, readable Python, refactor, naming, comments, magic numbers, data classes, code smells, DRY, KISS, YAGNI. Make Python read like prose at the line and function level."
license: Apache-2.0
metadata:
  author: velazco-joseh
  version: "1.0"
---

# Python Clean Code

Line- and function-level readability: naming, classes-vs-functions, comments, data types, plus DRY/KISS/YAGNI.

## Activation Contract

Apply when code is hard to read, a function does too much, names are cryptic, comments restate code, primitives model structured data, or the user asks to refactor/clean up Python. For class/module structure and SOLID, use `python-design-principles` instead.

## Hard Rules

- Name by intent: `verb_noun` for functions, `is_/has_` for booleans, named constants for magic numbers. A good name removes the need for a comment.
- Delete comments that restate code or hold dead code. Keep only *why* (rationale) and docstrings.
- Use a function, not a class, when there is no state to hold. Use `@dataclass`/`Enum`/`NamedTuple` instead of tuples or raw dicts for structured data.
- Flatten nesting with guard clauses (early return). Extract long functions into named steps.
- Replace repeated blocks with one parameterized abstraction (DRY): but only after the third repeat, never speculative (YAGNI). Prefer the simplest construct that works (KISS).

## Decision Gates

| Symptom | Fix |
|---------|-----|
| Magic number / cryptic name | Named constant / intention-revealing name |
| Comment explains *what* | Delete it; improve the name |
| Class with no state, only methods | Plain functions |
| Tuple/dict passed around as a record | `@dataclass` or `NamedTuple` |
| 4+ params | Parameter Object (`@dataclass`) |
| Deep `if` nesting | Guard clauses |
| Copy-pasted block (3rd time) | Extract shared function |

## Execution Steps

1. Read the smell; name which gate above it hits.
2. Show a tight `# Bad` → `# Good` diff: change one smell at a time.
3. Keep behavior identical; if tests exist, they must stay green.
4. Stop at KISS: do not introduce abstraction the current code does not need.

```python
# Bad
d = 86400
def process(u):
    if u:
        if u.active:
            return charge(u)

# Good
SECONDS_IN_DAY = 86400
def charge_if_active(user: User) -> Receipt | None:
    if not user or not user.active:
        return None
    return charge(user)
```

## Output Contract

Return the refactored Python, one smell per diff, with a one-line rationale per change. Never expand scope beyond the smell asked about.

## References

- `references/naming-and-comments.md`: naming and comment rules with examples.
- `references/data-and-smells.md`: data-type modeling, code smells, DRY/KISS/YAGNI.
