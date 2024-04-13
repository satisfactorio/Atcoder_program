n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
a.sort()
answer = 0
for num in a:
    if answer == num:
        answer += 1
    else:
        break
print(answer)