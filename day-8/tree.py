import sys


class Node:
    def __init__(self):
        self.children = []
        self.metadata = []

    def sum(self):
        return sum(self.metadata) + sum(c.sum() for c in self.children)

    def value(self):
        if not self.children:
            return sum(self.metadata)

        return sum(
            self.children[c - 1].value()
            for c in self.metadata
            if c and c - 1 < len(self.children)
        )


def parse(numbers):
    node = Node()

    pos = 2
    children, entries = numbers[0:pos]

    for _ in range(children):
        child, end = parse(numbers[pos:])
        node.children.append(child)
        pos += end

    node.metadata.extend(numbers[pos: pos + entries])
    pos += entries

    return node, pos


numbers = list(map(int, sys.stdin.read().split(' ')))
root, pos = parse(numbers)
assert pos == len(numbers)

print(root.sum())
print(root.value())
