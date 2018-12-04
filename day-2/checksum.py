#!/usr/bin/python
import sys
from collections import Counter

lines = sys.stdin.read().split('\n')
two = 0
three = 0

for line in lines:
    counter = Counter(line)
    found_two = False
    found_three = False

    for letter, count in counter.items():
        if count == 2:
            found_two = True
        elif count == 3:
            found_three = True

    if found_two:
        two += 1

    if found_three:
        three += 1

print(two * three)
