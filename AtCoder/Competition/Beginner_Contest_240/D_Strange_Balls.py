'''n = int(input())
a = list(map(int, input().split()))
former = a[0]
print(1)
count = 1
for i in range(1, n):
    if a[i] != former:
        count += 1
        print(count)
        former = a[i]
    else:
        count -= 1
        print(count)
        former = a[i - 2]'''


# Right Answer

n = int(input())
a = list(map(int, input().split()))

que = []
count = []
answer = 0

for i in range(n):
    que.append(a[i])
    answer += 1
    if len(que) >= 2 and que[-1] == que[-2]:
        count.append(count[-1] + 1)
        if count[-1] == que[-1]:
            for j in range(que[-1]):
                que.pop()
                count.pop()
                answer -= 1
    else:
        count.append(1)

    print(answer)
        