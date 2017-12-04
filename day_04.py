with open("input.txt") as f:
    data = []
    for line in f.read().splitlines():
        data.append(list(map(str, line.split())))


def first(d):
    c = 0
    for x in d:
        if len(x) == len(set(x)):
            c += 1
    return c


def second(d):
    c = 0
    for x in d:
        for i in range(0, len(x)):
            x[i] = ''.join(sorted(x[i]))
        if len(x) == len(set(x)):
            c += 1
    return c


print(first(data))
print(second(data))