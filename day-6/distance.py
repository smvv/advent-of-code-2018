#!/usr/bin/env python3
# Parts of this code are based on:
# https://github.com/petertseng/adventofcode-rb-2018/blob/master/06_chronal_coordinates.rb
import sys
import math


def minmax(arr):
    arr = list(arr)
    return min(arr), max(arr)


points = [
    tuple(map(int, line.strip().split(', ')))
    for line in sys.stdin
]

owned = [0] * len(points)
infinite = [False] * len(points)
within = 0

x_min, x_max = minmax(x for x, _ in points)
y_min, y_max = minmax(y for _, y in points)

for y in range(y_min, y_max + 1):
    edge_y = y == y_min or y == y_max

    for x in range(x_min, x_max + 1):
        best_dist = math.inf
        best = None
        dist_sum = 0

        for i, p in enumerate(points):
            dist = abs(p[0] - x) + abs(p[1] - y)
            dist_sum += dist

            if dist < best_dist:
                best = i
                best_dist = dist
            elif dist == best_dist:
                best = None

        edge_x = x == x_min or x == x_max

        if dist_sum < 10000:
            within += 1

        if not best:
            continue

        if edge_x or edge_y:
            infinite[best] = True
        else:
            owned[best] += 1

print(max([
    count
    for i, count in enumerate(owned)
    if not infinite[i]
]))

print(within)
