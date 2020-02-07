#!/usr/bin/env python3

import os
import sys
import re

# For debugging purposes
print(os.environ)
print(sys.argv)

branch_name = os.getenv("GITHUB_HEAD_REF")
assert branch_name is not None

token = os.getenv("INPUT_REPO-TOKEN")
print(branch_name)
print(token)
print(token[0:5])
print(token[-1])

print("-----")


#repo_token = sys.argv[1]
#print(f"Number of arguments: {len(sys.argv)}")
#print(sys.argv)
#print(f"Repo token: {repo_token}")
#
#
#
## Get branch name
#GITHUB_REF = os.getenv("GITHUB_REF")
#assert GITHUB_REF is not None
#print(f"GITHUB_REF: {GITHUB_REF}")
#


#branch_name_prefix = "refs/heads/"
#assert GITHUB_REF.startswith(branch_name_prefix)
#branch_name = GITHUB_REF.split(branch_name_prefix)[-1]
#
## Get issue code
#pattern = "^(ZIVID-\d+)-\w"
#match = re.match(pattern, branch_name)
#assert match is not None
#issue_string = match.groups()[0]
#
#
#print(f"Issue is: {issue_string}")
#