---
name: python-design-principles
description: "Trigger: SOLID, dependency inversion, coupling, cohesion, strategy pattern, open/closed, abstractions, Protocol, ABC, class structure. Shape Python class and module design."
license: Apache-2.0
metadata:
  author: velazco-joseh
  version: "1.0"
---

# Python Design Principles

Structure-level design: how classes and modules relate. Based on ArjanCodes/betterpython tips 1–3 (coupling/cohesion, dependency inversion, strategy) plus SOLID.

## Activation Contract

Apply when designing or refactoring class/module structure: a class does many jobs, high-level code instantiates concretions, a growing `if/elif` selects behavior, or the user asks about SOLID/coupling/abstractions. For line-level readability use `python-clean-code`; for system layering use architecture guidance.

## Hard Rules

- One reason to change per class (SRP). High cohesion (related behavior together), low coupling (few cross-dependencies).
- Depend on abstractions, not concretions (DIP). Inject collaborators via the constructor; never instantiate concrete deps inside a class.
- Open for extension, closed for modification (OCP): add behavior with a new class, not by editing an `if/elif`.
- Replace branching-on-type with the Strategy pattern — interchangeable classes behind a common `Protocol`/`ABC`.
- Prefer small `Protocol` interfaces (ISP) over fat ones. Subtypes must honor the parent contract (LSP) — no `raise NotImplementedError` overrides.

## Decision Gates

| Symptom | Principle | Fix |
|---------|-----------|-----|
| Class generates IDs, prices, prints | SRP/cohesion | Split into focused classes |
| `self.db = PostgresDB()` inside service | DIP | Inject a `Protocol` collaborator |
| `if type == "credit": ... elif ...` | OCP/Strategy | Strategy classes behind one interface |
| Interface with methods some impls reject | ISP/LSP | Split into small `Protocol`s |
| Module A imports B imports A | Coupling | Invert dependency via abstraction |

## Execution Steps

1. Identify the principle violated from the gate table.
2. Introduce the smallest abstraction that fixes it — a `Protocol` or `ABC`, injected.
3. Show `# Bad` → `# Good`; verify the client now depends only on the abstraction.
4. Do not add patterns the design does not yet need (YAGNI).

```python
from typing import Protocol

# Bad — branch on type, closed to extension
def pay(order, kind):
    if kind == "credit": ...
    elif kind == "debit": ...

# Good — Strategy behind a Protocol (OCP + DIP)
class PaymentProcessor(Protocol):
    def pay(self, order: Order) -> None: ...

class CreditProcessor:
    def pay(self, order: Order) -> None: ...

def checkout(order: Order, processor: PaymentProcessor) -> None:
    processor.pay(order)
```

## Output Contract

Return restructured Python where clients depend on abstractions, plus a one-line note naming each principle applied. Keep the abstraction minimal.

## References

- `references/solid.md` — the five SOLID principles with Python examples.
- `references/coupling-strategy.md` — coupling/cohesion and the Strategy pattern.
