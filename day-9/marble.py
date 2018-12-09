from collections import deque


def play(players, marbles):
    scores = [0] * players
    circle = deque([0])

    for m in range(1, marbles + 1):
        if m % 23 == 0:
            circle.rotate(7)
            scores[m % players] += m + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(m)

    return max(scores)


assert play(marbles=25, players=9) == 32
assert play(marbles=1618, players=10) == 8317
assert play(marbles=7999, players=13) == 146373
assert play(marbles=1104, players=17) == 2764
assert play(marbles=6111, players=21) == 54718
assert play(marbles=5807, players=30) == 37305
print(play(marbles=71019, players=432))
print(play(marbles=71019 * 100, players=432))
