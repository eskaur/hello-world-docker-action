#!/usr/bin/env python3

import os
import re


valid_patterns = [
    "^ZIVID-\d+-\w"
]



## Debug stuff
#print("Environment variables: ")
#for env in os.environ: 
#    print("{0:40}:  {1}".format(env, os.getenv(env))) 


# Get branch name
GITHUB_REF = os.getenv("GITHUB_REF")
assert GITHUB_REF is not None
branch_name_prefix = "refs/heads/"
assert GITHUB_REF.startswith(branch_name_prefix)
branch_name = GITHUB_REF.split(branch_name_prefix)[-1]


print(f"Checking branch name: {branch_name}")
matches = 0
for pattern in valid_patterns:
    print(f"--- Pattern: {pattern}   ...", end="")

    if re.match(pattern, branch_name):
        print("MATCH")
        matches += 1
    else:
        print("NO MATCH")

if matches > 0:
    print(f"Branch name matched at least one pattern. ---OK")
else:
    raise AssertionError("Branch name did not match any of the patterns. ---FAILED")


