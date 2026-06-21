# Data Types, Code Smells, DRY/KISS/YAGNI

## Right data structure
Model structured data with types, not loose primitives.

```python
# Bad: parallel lists / raw dict
user = ("Ana", "ana@x.com", 30)
# Good
from dataclasses import dataclass
@dataclass
class User:
    name: str
    email: str
    age: int
```
Use `Enum` for fixed choices, `NamedTuple` for lightweight immutable records.

## Classes vs functions (tip 5)
No state to hold → use a function, not a class-as-namespace.

```python
# Bad
class MathUtils:
    def add(self, a, b): return a + b
# Good
def add(a: int, b: int) -> int: return a + b
```

## Code smells
- Long function → decompose into named steps.
- 4+ params → Parameter Object (`@dataclass`).
- Deep nesting → guard clauses (early return).

## DRY / KISS / YAGNI
- DRY: extract a shared, parameterized function: after the third repeat, not before.
- KISS: simplest construct that works; avoid factories/abstractions for trivial logic.
- YAGNI: model only what is needed now; no speculative fields or hooks.
