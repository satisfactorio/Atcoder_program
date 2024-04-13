s = list(input())
s2 = []
for i in s:
    s2.append(int(i))

numbers = []
for i in range(0, 10):
    numbers.append(i)
for num in numbers:
    if num not in s2:
        print(num)
        break