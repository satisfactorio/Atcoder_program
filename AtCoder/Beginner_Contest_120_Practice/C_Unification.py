s = input()
number1 = 0
number0 = 0

for num in s:
    if int(num) == 1:
        number1 += 1
    else:
        number0 += 1

if number1 <= number0:
    print(number1 * 2)
else:
    print(number0 * 2)