s = input()
a, b = map(int, input().split())

answer = ''
temp1 = s[a - 1]
temp2 = s[b - 1]

for index in range(len(s)):
    if index == a - 1:
        answer += temp2
    elif index == b - 1:
        answer += temp1
    else:
        answer += s[index]

print(answer)
    



