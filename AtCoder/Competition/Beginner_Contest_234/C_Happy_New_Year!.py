k = int(input())

binary_number = format(k, 'b')
formatted_binary_number = ''
for num in binary_number:
    if num == '1':
        num = '2'
    formatted_binary_number += num

print(formatted_binary_number)





