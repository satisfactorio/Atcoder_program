h, w = map(int, input().split())
r, c = map(int, input().split())
count = 0

if r + 1 > h:
    pass
else:
    count += 1
if r - 1 <= 0:
    pass
else:
    count += 1
if c + 1 > w:
    pass
else:
    count += 1
if c - 1 <= 0:
    pass
else:
    count += 1

print(count)