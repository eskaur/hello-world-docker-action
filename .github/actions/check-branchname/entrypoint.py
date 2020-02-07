#!/usr/bin/env python3

import os

print("Hello from Python")

#print("Environment variables: ")
#for env in os.environ: 
#    print("{0:40}:  {1}".format(env, os.getenv(env))) 



GITHUB_REF = os.getenv("GITHUB_REF")
assert GITHUB_REF is None




