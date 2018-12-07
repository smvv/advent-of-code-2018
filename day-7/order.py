#!/usr/bin/env python3
import sys
from collections import defaultdict

deps = defaultdict(list)

for line in sys.stdin:
    parts = line.strip().split(' ')
    before, after = parts[1], parts[7]

    deps[after].append(before)
    deps[before]

done = set()
order = []


def available():
    # List of tasks that have no dependencies and are not done.
    return sorted([
        task
        for task, after in deps.items()
        if not after and task not in done
    ])


def complete(task):
    print('completed', task)
    order.append(task)

    # Remove completed task from each depended task.
    for t, after in deps.items():
        if task in after:
            after.remove(task)


def task_time(task):
    if not task:
        return 0

    return ord(task) - ord('A') + 60


total_workers = 5
timers = [0] * total_workers
workers = [None] * total_workers
time = 0


while len(done) != len(deps) or any(workers):
    # Decrement the timers, and mark work as completed.
    for i, w in enumerate(timers):
        if w:
            timers[i] = w - 1
            continue

        if workers[i]:
            complete(workers[i])
            workers[i] = None

    # Assign tasks to workers.
    tasks = iter(available())
    for i, w in enumerate(timers):
        if workers[i]:
            continue

        try:
            task = next(tasks)
        except StopIteration:
            task = None

        workers[i] = task
        timers[i] = task_time(task)

        if task:
            done.add(task)

    # Status report
    print('time', time, 'timers', timers, 'workers', workers,
          'done', ''.join(order), 'tasks', available())

    time += 1

print(''.join(order))
