'''n, s = int(input()), input()
a = [0]
pointer = 0
for i in range(n):
    if s[i] == 'L':
        a.insert(pointer, i + 1)
    if s[i] == 'R':
        a.insert(pointer + 1, i + 1)
        pointer += 1

for index in range(len(a)):
    if index == len(a) - 1:
        print(a[index])
    else:
        print(a[index], end=' ')'''


# Smart answer

import collections

n, s = int(input()), input()
que = collections.deque()

que.append(n)

for i in range(n - 1, -1, -1):
    if s[i] == 'L':
        que.append(i)
    if s[i] == 'R':
        que.appendleft(i)

print(*que)