#!/usr/bin/python
import sys

freq = 0
found = set([freq])

lines = sys.stdin.read().split()

while True:
    for line in lines:
        freq += int(line)
        if freq in found:
            print('found {} twice'.format(freq))
            sys.exit(0)
        found.add(freq)
