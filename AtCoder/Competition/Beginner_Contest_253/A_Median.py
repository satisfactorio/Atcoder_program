import numbers


numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)

if numbers[1] != sorted_numbers[1]:
    print('No')
else:
    print('Yes')