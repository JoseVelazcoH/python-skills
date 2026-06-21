---
name: python-code-review
description: "Trigger: code review, review my changes, review this PR, check my code, pre-merge review, review diff. Review Python changes by the Review Pyramid, priority-first."
license: Apache-2.0
metadata:
  author: velazco-joseh
  version: "1.0"
---

# Python Code Review

Review Python changes using the Review Pyramid — prioritize what matters, automate what doesn't.

## Activation Contract

Apply when the user asks to review changes, a diff, or a PR, or to check code before merge. Reviewing is distinct from writing — focus on judgment, not rewriting.

## Hard Rules

- Review bottom-up: API semantics → implementation correctness → docs → tests → style. Spend effort where the pyramid is widest at the base.
- Flag style/nits last and lightest — they are automatable (ruff/formatter), not merge-blockers.
- Always anchor review in task/business context; correctness depends on intent.
- Block on: breaking API contracts, wrong business logic, unhandled edge cases, security issues, missing tests for new behavior.
- Verify claims against the diff — never approve logic you have not traced.

## Decision Gates

| Layer | Check | Severity |
|-------|-------|----------|
| API semantics | Breaking changes, naming, contracts | Critical |
| Implementation | Business logic, edge cases, error handling | Critical |
| Security | Injection, authz, data exposure | Critical |
| Tests | New behavior covered, branch coverage | High |
| Docs | Public surface documented | Medium |
| Style | Lint/format | Nit (automate) |

## Execution Steps

1. Quick pass: lint, type check, security pattern scan, confirm tests exist.
2. Deep pass: trace API and implementation semantics against the stated task.
3. Check edge cases and error paths; confirm tests cover new branches.
4. Report findings ordered by severity (Critical → Nit), each with file:line and a concrete fix.

## Output Contract

Return findings grouped by pyramid layer, severity-ordered, each citing `file:line` with a specific remediation. Separate merge-blockers from nits explicitly. Do not rewrite the change — review it.

## References

- Pair with `python-clean-code`, `python-design-principles`, and `python-testing-tdd` to justify findings.
