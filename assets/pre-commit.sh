#!/bin/sh
# clean-python pre-commit harness.
# Reviews the staged Python diff against the clean-python plugin skills via
# Claude headless, and BLOCKS the commit if violations are found.
#
# INSTALL (per target project):
#   1. Install the plugin:   /plugin install python-skills@clean-python
#   2. Copy this file to:    .git/hooks/pre-commit   (and chmod +x it)
#   3. Requires `claude` and `jq` on PATH.
#
# Bypass once with:  git commit --no-verify

# Only review staged Python files; skip otherwise to keep commits fast.
staged_py=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.py$')
[ -z "$staged_py" ] && exit 0

echo "clean-python: reviewing staged diff against skill rules..."

diff=$(git diff --cached -- $staged_py)
[ -z "$diff" ] && exit 0

response=$(printf '%s' "$diff" | claude -p "/python-skills:review-rules" \
    --output-format json \
    --permission-mode dontAsk \
    --allowedTools "Read" 2>/dev/null)

if [ -z "$response" ]; then
    echo "clean-python: review inconclusive (no response from claude). Commit allowed."
    echo "  Check that 'claude' is on PATH and the plugin is installed."
    exit 0
fi

result=$(printf '%s' "$response" | jq -r '.result')

if printf '%s' "$result" | grep -q "VIOLATION:"; then
    echo
    echo "Commit blocked: clean-python rule violations:"
    printf '%s' "$result" | grep "VIOLATION:"
    echo
    echo "Fix them, or bypass with: git commit --no-verify"
    exit 1
fi

if printf '%s' "$result" | grep -q "NO_VIOLATIONS"; then
    echo "clean-python: passed."
    exit 0
fi

# Neither sentinel: fail safe: do not silently let unknown output through.
echo "clean-python: review inconclusive. Raw output:"
printf '%s\n' "$result"
echo "Bypass with: git commit --no-verify"
exit 1
