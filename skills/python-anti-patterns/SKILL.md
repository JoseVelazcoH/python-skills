---
name: python-anti-patterns
description: "Trigger: anti-patterns, import order, file too long, split module, unrelated functions, hardcoded values, magic values, module constants, extract constants. Enforce battle-tested Python module-organization rules."
license: Apache-2.0
metadata:
  author: velazco-joseh
  version: "1.0"
---

# Python Anti-Patterns

Prescriptive module-organization rules learned in practice. These are enforced engineering standards, not style preferences: apply them on every Python file touched.

## Activation Contract

Apply when writing or reviewing any Python module: checking import order, file size, module cohesion, hardcoded values, or where constants live. Flag every violation below; do not wait to be asked.

## Hard Rules

- **Import order (custom convention):** first all `import x` statements (alphabetical), then `from x import ...` for stdlib/third-party, then a blank line, then first-party `from core...` imports. No blank line between the `import` block and the non-local `from` block. See `references/import-order.md`. NOTE: ruff's isort (`I`) rule reverts this: disable `I` in the linter config or it overwrites the skill.
- **File length:** ~300 lines is a hard smell. Split by responsibility before that. A long file almost always hides multiple concerns.
- **Module cohesion:** functions with no relationship to the module's purpose must be extracted to their own module. One module = one cohesive concern.
- **No hardcoded values:** never inline literals (URLs, paths, thresholds, column names, magic numbers/strings) in logic. Name them.
- **Centralize constants for reuse:** do not scatter constants at the top of feature modules. Put them in a dedicated `constants.py` so any module can import and reuse them. The reason is reusability: a local constant dies in its file; a centralized one is shared.

## Decision Gates

| Symptom | Fix |
|---------|-----|
| Imports mixed/misordered | Reorder per the custom convention above |
| File approaching ~300 lines | Split by responsibility into separate modules |
| Function unrelated to module purpose | Extract to its own module |
| Literal inside logic | Replace with a named constant |
| `CONST = ...` atop a feature module | Move to `constants.py`, import it |

## Execution Steps

1. Scan the module against each gate; list every hit with `file:line`.
2. Fix imports first (cheap, mechanical), then extract constants to `constants.py`, then split oversized/incohesive files.
3. Replace each hardcoded literal with an imported named constant.
4. Confirm each remaining module has a single cohesive concern.

```python
# Bad: hardcoded + local constant + mixed imports
from core.utils.logger import get_logger
import requests
TIMEOUT = 30
def fetch(): requests.get("https://api.inegi.org.mx/data", timeout=TIMEOUT)

# Good: named, centralized, ordered
# constants.py
INEGI_DATA_URL = "https://api.inegi.org.mx/data"
REQUEST_TIMEOUT_SECONDS = 30

# module.py
import requests

from core.constants import INEGI_DATA_URL, REQUEST_TIMEOUT_SECONDS
from core.utils.logger import get_logger

def fetch():
    return requests.get(INEGI_DATA_URL, timeout=REQUEST_TIMEOUT_SECONDS)
```

## Output Contract

Return the corrected module(s) with imports reordered, constants moved to `constants.py`, hardcoded values named, and oversized/incohesive files split. Cite each violation by `file:line`.

## References

- `references/import-order.md`: the custom import-ordering convention with full examples.
