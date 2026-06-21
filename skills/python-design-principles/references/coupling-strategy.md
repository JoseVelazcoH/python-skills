# Coupling/Cohesion & Strategy

## Coupling & Cohesion (tip 1)
- **High cohesion**: related behavior lives together. A `VehicleRegistry` that also formats prices and prints output is low-cohesion — split each responsibility.
- **Low coupling**: classes depend on few others, through abstractions. A → B → A import cycles signal tight coupling; invert one dependency behind a `Protocol`.

```python
# Bad — one class does ID generation, pricing, registration, printing
class VehicleRegistry:
    def generate_id(self): ...
    def calculate_price(self): ...
    def register(self): ...
    def print_receipt(self): ...

# Good — focused, loosely coupled collaborators
class IdGenerator: ...
class PriceCalculator: ...
class VehicleRegistry:           # orchestrates, owns none of their internals
    def __init__(self, ids: IdGenerator, pricing: PriceCalculator): ...
```

## Strategy Pattern (tip 3)
Replace branch-on-type with interchangeable strategies behind one interface. Realizes Open/Closed + Dependency Inversion.

```python
from typing import Protocol
class PaymentProcessor(Protocol):
    def pay(self, order: "Order") -> None: ...

class CreditProcessor:
    def pay(self, order: "Order") -> None: ...
class DebitProcessor:
    def pay(self, order: "Order") -> None: ...

def checkout(order: "Order", processor: PaymentProcessor) -> None:
    processor.pay(order)        # add a new processor without editing this
```
A functional variant passes a `Callable[[Order], None]` instead of a class — prefer it when the strategy is stateless.
