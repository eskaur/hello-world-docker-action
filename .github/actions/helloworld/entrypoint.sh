#!/bin/sh -l

echo "Hello $1"
echo "GITHUB_REF: " $GITHUB_RE
time=$(date)
echo ::set-output name=time::$time