s = input()
judge = False

for letter in s:
    if s.count(letter) == 1:
        print(letter)
        judge = True
        break

if not judge:
    print(-1)

