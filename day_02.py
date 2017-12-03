import itertools

with open('input.txt') as f:
    data = []
    for line in f.read().splitlines():
        data.append(list(map(int, line.split())))


def first():
    cs = 0
    for row in data:
        cs += max(row) - min(row)
    return cs


def second():
    cs = 0
    for row in data:
        combos = list(itertools.combinations(row, 2))
        for c in combos:
            a, b = max(c), min(c)
            if a % b == 0:
                cs += a//b
    return cs


print(first())
print(second())