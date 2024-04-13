n = int(input())
for i in range(n):
    if i == 0:
        answer = str(i + 1)
    else:
        answer = answer + ' ' + str(i + 1) + ' ' + answer
print(answer)

