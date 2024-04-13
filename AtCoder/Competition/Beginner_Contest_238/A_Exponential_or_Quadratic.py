n = int(input())
if 1 <= n <= 4:
    if 2**n > n**2:
        print('Yes')
    else:
        print('No')
else:
    print('Yes')
