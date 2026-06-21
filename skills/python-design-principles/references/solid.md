# SOLID in Python

## S: Single Responsibility
One reason to change. Split a class that creates users *and* sends email *and* exports CSV into focused classes.

## O: Open/Closed
Add behavior with a new class, not by editing an `if/elif`. See Strategy in `coupling-strategy.md`.

```python
from abc import ABC, abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, amount: float) -> float: ...
class VIPDiscount(DiscountStrategy):       # extend without touching others
    def calculate(self, amount: float) -> float: return amount * 0.3
```

## L: Liskov Substitution
A subtype must honor the parent contract. A `Penguin(Bird)` that raises on `fly()` breaks LSP: model `move()` on `Bird`, `fly()` on `FlyingBird`.

## I: Interface Segregation
Prefer small `Protocol`s. Don't force a `Robot` to implement `eat()`/`sleep()`.

```python
from typing import Protocol
class Workable(Protocol):
    def work(self) -> None: ...
```

## D: Dependency Inversion
High-level code depends on abstractions; inject concretions.

```python
class OrderService:
    def __init__(self, db: DatabaseProtocol, email: EmailProtocol):
        self._db = db; self._email = email
```
