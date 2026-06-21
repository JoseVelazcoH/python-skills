# Import Order (Custom Convention)

This is a deliberate project convention. It differs from PEP 8 / ruff-isort defaults: that is intentional.

## The rule
1. All plain `import x` statements first, alphabetical.
2. Then `from x import ...` for stdlib and third-party packages.
3. One blank line.
4. Then first-party `from core... import ...` imports.

No blank line between blocks 1 and 2; the only blank line separates non-local from first-party (`core`) imports.

## Correct

```python
import io
import pandas as pd
import requests
from typing import Any, Optional

from core.pipelines.stage import Stage
from core.pipelines.censo_poblacion.config import settings
from core.pipelines.censo_poblacion.constants import (
    RENAME_INEGI_2010_COL,
    RENAME_INEGI_2015_COL,
    RENAME_INEGI_2020_COL,
)
from core.utils.files import read_csv_from_zip_url
from core.utils.logger import get_logger
```

## Wrong: `from typing` placed before plain imports
```python
from typing import Any, Optional   # must come after the import block
import io
import pandas as pd
```

## Wrong: stdlib/third-party imports split by a blank line
```python
from typing import Any, Optional

import io
import pandas as pd
import requests
```

## Tooling caveat
ruff's import-sorting rule (`I`/isort) will rewrite this to its own grouping. To keep this convention, disable `I` in `pyproject.toml`:

```toml
[tool.ruff.lint]
ignore = ["I"]
```
Otherwise the formatter and this convention fight, and the formatter wins on every save.
