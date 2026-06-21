---
description: "Audit a Python repository against the clean-python skills and emit a scored quality report with prioritized findings."
argument-hint: "[optional path to scope the audit, e.g. src/payments]"
allowed-tools: Read, Grep, Glob, Bash
---

You are a senior Python reviewer running a full-repository quality audit. Audit the codebase against the project's five skills and emit a single scored report. This is a semantic audit: read real code and judge it, do not just pattern-match.

## Scope

- If `$ARGUMENTS` is provided, audit only that path (file or directory).
- Otherwise, audit the whole repository.
- Audit production Python only. Exclude tests from the design/clean-code/anti-pattern dimensions (tests are scored under Testing & TDD), and exclude vendored, generated, and `.venv`/`site-packages` code.
- Use `Glob`/`Grep` to enumerate the files, then `Read` the ones that matter. Do not try to read every file: sample representatively, then deep-read the suspicious ones. State explicitly if you sampled rather than read everything.

## Dimensions

Score four quality dimensions, each `0-6`. The fifth skill, `python-code-review`, is not a dimension: it is the lens. Use its Review Pyramid (API semantics → implementation → security → tests → docs → style) to order findings by severity.

1. **Clean Code** (`python-clean-code`): intention-revealing names, comments that explain *why* not *what*, functions over stateless classes, `@dataclass`/`Enum`/`NamedTuple` over raw tuples/dicts, guard clauses over deep nesting, Parameter Objects for 4+ params, DRY-after-third-repeat, KISS, YAGNI.
2. **Design Principles** (`python-design-principles`): SRP (one reason to change), DIP (inject collaborators via constructor, depend on `Protocol`/`ABC`), OCP/Strategy over `if/elif` on type, ISP (small interfaces), LSP (no `NotImplementedError` overrides), low coupling / high cohesion.
3. **Testing & TDD** (`python-testing-tdd`): tests exist for behavior, one scenario per test, `test_<subject>_<condition>_<expected>` naming, Arrange-Act-Assert, isolation/order-independence, mock only external boundaries (never internal repos/services), branch coverage on both sides of conditionals, `parametrize` used only for same-check-many-inputs.
4. **Anti-Patterns** (`python-anti-patterns`): custom import order (all `import x` alphabetical, then stdlib/third-party `from`, blank line, then first-party `from core...`), files under ~300 lines, one cohesive concern per module, no hardcoded literals in logic, constants centralized in `constants.py`.

## Per-dimension scoring (0-6)

- **6** Exemplary: no violations found in the audited code.
- **5** Strong: only isolated P3 nits.
- **4** Solid: a few P2 issues, no P0/P1.
- **3** Mixed: recurring P1/P2 violations across files.
- **2** Weak: P0/P1 patterns present and systemic.
- **1** Poor: the dimension's rules are broadly ignored.
- **0** Absent or critical failure (e.g. no tests at all for Testing & TDD).

Composite = sum of the four dimensions, `0-24`.

## Health bands (composite)

- **22-24** Excellent: minor polish only.
- **17-21** Good: address the weak dimensions.
- **12-16** Acceptable: significant work needed.
- **7-11** Poor: major overhaul.
- **0-6** Critical: fundamental issues.

## Severity (order findings by this)

- **P0 Blocking**: breaks API contracts, wrong business logic, security exposure, or no tests for new behavior. Fix before merge.
- **P1 Major**: systemic design violation (SRP/DIP/OCP), untested branch, file well over 300 lines hiding multiple concerns.
- **P2 Minor**: local clean-code or anti-pattern violation with an easy fix (magic value, weak name, misordered imports).
- **P3 Polish**: stylistic nit, automatable, no behavioral impact.

## Report format

Emit exactly this structure, in markdown:

### Audit Health Score

| # | Dimension | Score | Key finding |
|---|-----------|-------|-------------|
| 1 | Clean Code | x/6 | ... |
| 2 | Design Principles | x/6 | ... |
| 3 | Testing & TDD | x/6 | ... |
| 4 | Anti-Patterns | x/6 | ... |

**Composite: x/24 (`<band label>`)**

### Executive Summary

- One paragraph on overall health.
- Issue counts: `P0: n · P1: n · P2: n · P3: n`.
- Top 3 issues to fix first.
- Recommended next step.

### Findings by Severity

For each finding, in P0 → P3 order:

- **[P0] <short title>** (`file:line`)
  - Dimension: <which of the four>
  - Rule: <the specific skill rule violated>
  - Impact: <why it matters, in business/correctness terms>
  - Fix: <concrete, specific remediation>

### Systemic Patterns

Recurring problems that span multiple files (e.g. "constants scattered across 7 modules instead of `constants.py`"). These matter more than isolated nits.

### Strengths

What the codebase already does well, worth preserving. Be honest: if there is nothing, say so.

### Action Plan

Ordered checklist, highest-leverage first. Group by dimension where it helps. Each item maps to a finding or systemic pattern above.

## Rules

- Anchor every finding in a specific skill rule and a real `file:line`. Never flag a stylistic opinion that no skill backs.
- Verify before you claim: trace the code, do not assume. If you only sampled part of the repo, say which part and that the score is a sample-based estimate.
- Be priority-first: P0/P1 before nits. A wall of P3s buries the issues that matter.
- Do not rewrite the codebase. This is an audit: judge and prioritize, do not patch.
