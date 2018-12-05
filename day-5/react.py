#!/usr/bin/env python3
import sys


def react(chain):
    changed = True

    while changed:

        new_chain = []
        changed = False

        i = 0
        while i < len(chain) - 1:
            cur = chain[i]
            next = chain[i + 1]

            if cur.islower() and cur.upper() == next:
                i += 2
                changed = True
                continue
            if cur.isupper() and cur.lower() == next:
                i += 2
                changed = True
                continue

            i += 1
            new_chain.append(cur)

        chain = new_chain + [chain[-1]]

    return chain


chain = sys.stdin.read().strip()
chain = react(chain)
print(len(chain))

shortest = min([
    len(react([x for x in chain if x != letter and x != letter.upper()]))
    for letter in map(lambda x: chr(ord('a') + x), range(0, 26))
])

print(shortest)
