'''s = input()
if len(s) % 2 == 0:
    head = s[: len(s) // 2]
    tail = s[len(s) // 2:]
else:
    head = s[: (len(s) - 1) // 2]
    tail = s[(len(s) - 1) // 2 + 1:]
reversed_tail = tail[::-1]
judge = False
for i in range(5 * 10 ** 5):
    if tail in head:
        judge = True
        break
    head = 'a' + head
if judge:
    print('Yes')
else:
    print('No')'''


# TLE answer

'''s = list(input())

def is_palindrome(s, judge = True):
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            judge = False
            break
    return judge

def a_of_head_tail(s, head = 0, tail = 0):
    for i in range(len(s)):
        if s[-1] == 'a':
            tail += 1
            del s[-1]
        else:
            break
    for i in range(len(s)):
        if s[0] == 'a':
            head += 1
            del s[0]
        else:
            break
    return [head, tail]

head_tail = a_of_head_tail(s)
if len(s) == 1:
    print('Yes')
elif head_tail[0] > head_tail[1]:
    print('No')
elif is_palindrome(s):
    print('Yes')
else:
    print('No')'''


# Right answer

s = input()

a_front = 0

for i in range(len(s)):
    if s[i] == 'a':
        a_front += 1
    else:
        break

a_back = 0

for i in range(len(s) - 1, -1, -1):
    if s[i] == 'a':
        a_back += 1
    else:
        break

if a_back < a_front:
    print('No')
    exit()

s = 'a' * (a_back - a_front) + s

for i in range(len(s)):
    if s[i] != s[len(s) - 1 - i]:
        print('No')
        exit()

print('Yes')
