#!/usr/bin/env python3
import sys

lines = sys.stdin.read().split('\n')
matches = {}

for line in lines:
    for i in range(len(line)):
        left, right = line[:i], line[i + 1:]
        key = str(i) + '_' + left + right

        if key in matches:
            print('found match:', left + right)

        matches[key] = line
