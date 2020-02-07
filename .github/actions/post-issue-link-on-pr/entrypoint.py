#!/usr/bin/env python3

import os
import sys
import re



print(os.environ)

print(sys.argv)

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