#!/usr/bin/env python3
import sys

debug = False

grid_size = 1000

claims = sys.stdin.read().strip().split('\n')
grid = [[[] for j in range(grid_size)] for i in range(grid_size)]

claim_ids = set()

# Load claims into grid
for claim in claims:
    claim_id, _, rect, size = claim.split(' ')

    # Strip leading '#' from ID.
    claim_id = claim_id[1:]
    claim_ids.add(claim_id)

    # Strip trailing ':' from rect.
    rect = tuple(map(int, rect[:-1].split(',')))
    size = tuple(map(int, size.split('x')))

    if debug:
        print(claim_id, rect, size)

    for y in range(size[1]):
        for x in range(size[0]):
            grid[rect[1] + y][rect[0] + x].append(claim_id)


# Optionally, dump the grid
if debug:
    for j in range(grid_size):
        for i in range(grid_size):
            cell = grid[j][i]
            if len(cell) >= 2:
                sys.stdout.write('X')
            elif cell:
                sys.stdout.write(cell[0])
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')


# Compute overlapping inches
overlapping = set()

for j in range(grid_size):
    for i in range(grid_size):
        cell = grid[j][i]

        if len(cell) >= 2:
            for claim_id in cell:
                overlapping.add(claim_id)

print(claim_ids - overlapping)
