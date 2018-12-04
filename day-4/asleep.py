#!/usr/bin/env python3
import sys

entries = sys.stdin.read().strip().split('\n')
entries = sorted(entries)

time_table = {}
guard_id = None

for entry in entries:
    date, time, command, arg, *args = entry.split(' ')

    if command == 'Guard':
        # Strip the leading '#'
        guard_id = int(arg[1:])
    elif command == 'falls':
        # Strip the trailing ']'
        start = int(time[:-1].split(':')[1])
    else:
        assert command == 'wakes'
        end = int(time[:-1].split(':')[1])

        if guard_id not in time_table:
            time_table[guard_id] = [0] * 60

        for i in range(start, end):
            time_table[guard_id][i] += 1


most_total = 0
most_guard = None
most_minutes = 0

for guard_id, minutes in time_table.items():
    total = sum(minutes)
    if total > most_total:
        most_total = total
        most_minutes = minutes.index(max(minutes))
        most_guard = guard_id

print('strategy 1', most_guard * most_minutes)

most_minutes = 0
most_guard = None
max_minutes = 0

for guard_id, minutes in time_table.items():
    cur = max(minutes)

    if cur > max_minutes:
        max_minutes = cur
        most_minutes = minutes.index(cur)
        most_guard = guard_id

print('strategy 2', most_guard * most_minutes)
