# Naming & Comments

## Naming
Names should reveal intent so comments become unnecessary.

```python
# Bad
d = 86400; u = get_user(); tmp = calc()
# Good
SECONDS_IN_DAY = 86400
current_user = get_user()
total_price = calc()
```

- Functions: `verb_noun` — `calculate_total_price`, `send_welcome_email`.
- Booleans: `is_`, `has_`, `can_` — `is_active`, `has_permission`.
- Constants: UPPER_SNAKE for magic numbers — never inline `0.2`, name it `PREMIUM_DISCOUNT_RATE`.

## Comments
Keep only what code cannot express.

```python
# Bad — restates code
count += 1  # increment count

# Good — explains why
# Retry once: the upstream API drops the first request after idle.
retry_once(call)
```

- Delete commented-out (dead) code — version control remembers it.
- A comment compensating for a bad name is a smell — rename instead.
- Public functions/classes get docstrings; internal helpers rarely need them.
