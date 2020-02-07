#!/usr/bin/env python3

import os

print("Hello from Python")


for env in os.environ: 
    print("{0:40}:  {1}".format(env, os.getenv(env))) 
