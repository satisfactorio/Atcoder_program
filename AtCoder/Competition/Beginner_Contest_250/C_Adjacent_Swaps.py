n, q = map(int, input().split())
x_list = []

for i in range(q):
    x = int(input())
    x_list.append(x)


answer = []

for i in range(1, n + 1):
    answer.append([i, i])

for num in x_list:
    if num != n:
        answer[num - 1][1] += 1
        answer[num][1] -= 1
    else:
        answer[num - 2][1] += 1
        answer[num - 1][1] -= 1

last_answer = [0] * n
for i in range(n):
    last_answer[answer[i][1]] = answer[i][0]

print(*last_answer)