'''n, k = map(int, input().split())
p = list(map(int, input().split()))

for t in range(k, n + 1):
    new_p = p[:t]
    sorted_new_p = sorted(new_p, reverse = True)
    kth_number = sorted_new_p[k - 1]
    print(kth_number)'''


# Smart answer

import heapq

n, k = map(int, input().split())
p = list(map(int, input().split()))

que = []

for i in range(k):
    que.append(p[i])

print(min(que))

heapq.heapify(que)

for i in range(k, n):
    x = heapq.heappop(que)
    heapq.heappush(que, max(x, p[i]))
    print(que[0])
