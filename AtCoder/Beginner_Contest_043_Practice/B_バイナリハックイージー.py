s = input()
word = []
for letter in s:
    if letter == '0':
        word.append('0')
    if letter == '1':
        word.append('1')
    if letter == 'B':
        if len(word) >= 1:
            del word[-1]

ans = ''
for letter in word:
    ans += letter

print(ans)
