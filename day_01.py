with open('input.txt') as f:
    data = f.read().rstrip()

def first():
    c = 0
    for i in range(len(data)):
        if data[i] == data[i-1]:
            c += int(data[i])
    return c

def second():
    c = 0
    data_len = len(data)
    for i in range(data_len)[::-1]:
        if data[i] == data[i - data_len//2]:
            c += int(data[i])
    return c

print(first())
print(second())