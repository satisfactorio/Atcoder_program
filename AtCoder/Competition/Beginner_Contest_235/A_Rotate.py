number = input()

abc = number[0] + number[1] + number[2]
bca = number[1] + number[2] + number[0]
cab = number[2] + number[0] + number[1]

print(f'{int(abc) + int(bca) + int(cab)}')
