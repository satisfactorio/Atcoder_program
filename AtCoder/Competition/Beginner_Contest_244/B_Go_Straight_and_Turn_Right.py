n = int(input())
t = input()
x, y = 0, 0
direction = 'E'
for i in t:
    if i == 'R':
        if direction == 'E':
            direction = 'S'
        elif direction == 'S':
            direction = 'W'
        elif direction == 'W':
            direction = 'N'
        else:
            direction = 'E'
    else:
        if direction == 'E':
            x += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'W':
            x -= 1
        else:
            y += 1
print(x, y)