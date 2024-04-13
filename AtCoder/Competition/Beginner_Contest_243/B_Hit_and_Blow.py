n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer_1 = 0
for i in range(n):
    if a[i] == b[i]:
        answer_1 += 1

answer_2 = 0
for i in range(n):
    for j in range(n):
        if i != j and a[i] == b[j]:
            answer_2 += 1
print(answer_1)
print(answer_2)