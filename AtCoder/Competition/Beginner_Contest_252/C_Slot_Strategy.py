import copy

n = int(input())
s = []
for i in range(n):
    s.append(input())

candidates = []
for i in range(10):
    temp_s = copy.copy(s)
    count = -1
    while True:
        count += 1
        for k in range(len(temp_s)):
            if i == int(temp_s[k][count % 10]):
                del temp_s[k]
                break
        if len(temp_s) == 0:
            break
    candidates.append(count)

print(min(candidates))
        
