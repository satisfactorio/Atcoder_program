x, y = map(int, input().split())

count = 0

while x < y:
    x += 10
    count += 1

print(count)
