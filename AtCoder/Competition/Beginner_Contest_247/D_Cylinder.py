# Upsolving


from collections import deque

q = int(input())
que = deque()

for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        que.append([query[1], query[2]])
        
    else:
        total = 0
        c = query[1]
        
        while c > 0:
            if que[0][1] >= c:
                que[0][1] -= c
                total += que[0][0] * c
                c -= c
            else:
                c -= que[0][1]
                total += que[0][0] * que[0][1]
                que.popleft()
        print(total)
