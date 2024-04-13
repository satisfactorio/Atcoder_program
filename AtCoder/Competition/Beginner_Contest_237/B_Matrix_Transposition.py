h, w = map(int, input().split())
a = []
for _ in range(h):
    a.append(list(map(int, input().split())))
b = []
for i in range(w):
    b2 = []
    for i in range(h):
        b2.append(0)
    b.append(b2)
for row in range(w):
    for column in range(h):
        b[row][column] = a[column][row]
for row in range(w):
    for column in range(h):
        if column == h - 1:
            print(b[row][column])
        else:
            print(b[row][column], end=' ')