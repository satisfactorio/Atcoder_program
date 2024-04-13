n = int(input())
s = input()
w = list(map(int, input().split()))
age_and_weights = list(zip(w, list(s)))

age_and_weights.sort(key=lambda x:x[0])
answer = []
adult = s.count('1')
answer.append(adult)
index = 0

while index <= n - 1:
    while True:
        try:
            if age_and_weights[index][0] == age_and_weights[index + 1][0]:
                index += 1
            else:
                break
        except:
            break
    if age_and_weights[index][1] == '1':
        adult -= 1
    else:
        adult += 1
    index += 1
    answer.append(adult)

print(max(answer))   7




