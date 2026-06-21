---
name: python-testing-tdd
description: "Trigger: write tests, pytest, TDD, red-green-refactor, fixtures, mocks, parametrize, coverage, test first. Drive Python features test-first with quality pytest patterns."
license: Apache-2.0
metadata:
  author: velazco-joseh
  version: "1.0"
---

# Python Testing & TDD

Test-first development with pytest. Combines the Red-Green-Refactor workflow with quality test patterns.

## Activation Contract

Apply when the user writes tests, builds a feature test-first, asks about pytest/fixtures/mocks/coverage, or wants the full TDD cycle. Default to TDD: test before implementation.

## Hard Rules

- Red → Green → Refactor, in that order. Write a failing test first; write the minimal code to pass; then improve with tests green.
- One scenario per test. Name it `test_<subject>_<condition>_<expected>`. Follow Arrange-Act-Assert.
- Tests must be isolated and order-independent: no shared mutable module state.
- Mock only external boundaries (APIs, email, payments, time, uuid, random). Use a real test database; never mock internal repositories/services or the code under test.
- Enable branch coverage (`--cov-branch`); cover both sides of every conditional, not just lines.
- Use `parametrize` only for the same check over many inputs: separate tests for distinct scenarios.

## Decision Gates

| Situation | Action |
|-----------|--------|
| New behavior requested | Write failing test first (Red) |
| External dependency in unit | Mock it (`AsyncMock`/`Mock(spec=...)`) |
| DB involved | Real test DB + transaction rollback fixture |
| Same assertion, many inputs | `@pytest.mark.parametrize` |
| Distinct scenarios | Separate named tests |
| Async code | `asyncio_mode = "auto"`, async fixtures |

## Execution Steps

1. RED: write the smallest failing test for the next behavior; run it, confirm it fails for the right reason.
2. GREEN: write the minimal code to pass; run, confirm green.
3. REFACTOR: clean code and tests while green.
4. Repeat per behavior; track phases explicitly for non-trivial features.

```python
async def test_create_order_with_two_items_sums_total(service):
    # Arrange
    items = [{"price": 100, "qty": 2}, {"price": 50, "qty": 1}]
    # Act
    order = await service.create(items=items)
    # Assert
    assert order.total == 250
```

## Output Contract

Return tests (and, in TDD, the minimal implementation) with clear behavior-naming, isolation via fixtures, and external-only mocking. State which phase (Red/Green/Refactor) each change belongs to.

## References

- Pair with `python-clean-code` and `python-design-principles` during Refactor.
