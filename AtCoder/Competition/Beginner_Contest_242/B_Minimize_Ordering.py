'''s = list(input())
count = 1
while count > 0:
    before = s[0]
    count = 0
    for i in range(1, len(s)):
        now = s[i]
        if now < before:
            temp = now
            s[i] = before
            s[i - 1] = temp
            count += 1
        else:
            before = s[i]
print(''.join(s))'''


# Another solution

print(''.join(sorted(input())))
    
    
