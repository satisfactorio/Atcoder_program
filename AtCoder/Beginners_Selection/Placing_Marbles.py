s = input()

a, b, c = map(int, [s[0], s[1], s[2]])

count = 0

if a == 1:
    count += 1
if b == 1:
    count += 1
if c == 1:
    count += 1

print(count)

