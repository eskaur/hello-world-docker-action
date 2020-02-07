#!/usr/bin/env python3

import os
import re
import sys

# For debugging purposes
print(os.environ)
print(sys.argv)

# List of valid patterns
valid_patterns = [
    "^master$",
    "^release-\d\.\d+\.\d+$",
    "^ZIVID-\d+-\w",
    "^MISC-\d{8}-\w"
]

# Get branch name
GITHUB_REF = os.getenv("GITHUB_REF")
assert GITHUB_REF is not None
branch_name_prefix = "refs/heads/"
assert GITHUB_REF.startswith(branch_name_prefix)
branch_name = GITHUB_REF.split(branch_name_prefix)[-1]

# Check branch name against patterns
print(f"\nChecking branch name: {branch_name}")
matches = 0
for pattern in valid_patterns:
    print(f"{'--- Pattern:':15} {pattern:30}   ...", end="")

    if re.match(pattern, branch_name):
        print("MATCH")
        matches += 1
    else:
        print("NOT A MATCH")

if matches > 0:
    print(f"\nBranch name matched at least one pattern. ---OK")
else:
    raise AssertionError("Branch name did not match any of the patterns. ---FAILED")


