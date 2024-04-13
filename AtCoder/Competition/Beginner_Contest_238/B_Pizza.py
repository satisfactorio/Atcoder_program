'''import collections
from platform import java_ver

n = int(input())
a = list(map(int, input().split()))

que = collections.deque()

for i in range(361):
    que.append(i)

que.appendleft('|')
count = 1
total = 0

for angle in a:
    if total > 360 + count:
        que.rotate(-(angle + count))
        que.appendleft('|')
        count += 1
        total += angle
    else:
        que.rotate(-(angle))
        que.appendleft('|')
        count += 1
        total += angle
        

que.rotate(-1)

angle_list = []
head_pointer = 0
tail_pointer = 0

while True:
    if tail_pointer == len(que):
        break

    for i in range(len(que)):
        if i == '|':
            tail_pointer = i
            break
    angle = []
    for a in range(head_pointer, tail_pointer):
        angle.append(a)
    
    angle_list.append(len(angle))
    head_pointer = tail_pointer + 1

print(max(angle_list))'''

n = int(input())
a = list(map(int, input().split()))

angles = [0, 360]

pointer = 360

for angle in a:
    gap = pointer - angle
    if gap < 0:
        gap += 360
    angles.append(gap)
    pointer = gap

angles.sort()
differences = []
for i in range(1, len(angles)):
    difference = angles[i] - angles[i - 1]
    differences.append(difference)

print(max(differences))
    


    
        



