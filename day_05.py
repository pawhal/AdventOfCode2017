def first():
    with open('input.txt') as f:
        data = [int(i) for i in f.read().splitlines()]
    x = 0
    s = 0
    while True:
        try:
            move = data[x]
            if 0 and move >= 3:
                data[x] -= 1
            else:
                data[x] += 1
            x += move
            s += 1
        except IndexError:
            break
    return s


def second():
    with open('input.txt') as f:
        data = list(int(i) for i in f.read().splitlines())
    x = 0
    s = 0
    while True:
        try:
            move = data[x]
            if 1 and move >= 3:
                data[x] -= 1
            else:
                data[x] += 1
            x += move
            s += 1
        except IndexError:
            break
    return s


print(first())
print(second())