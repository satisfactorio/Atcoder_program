n, k = map(int, input().split())
a = list(map(int, input().split()))

b = sorted(a)
if a == b:
    print('Yes')
    exit()

sorted_index = -1
judge = True

while sorted_index <= n - 1:
    min_indexes = [i + sorted_index + 1 for i, v in enumerate(a[sorted_index + 1:]) if v == min(a[sorted_index + 1:])]
    judge2 = False

    for i in range(len(min_indexes)):
        if (min_indexes[i] - sorted_index + 1) % k == 0:
            a[min_indexes[i]], a[sorted_index + 1] = a[sorted_index + 1], a[min_indexes[i]]
            judge2 = True
            break
    if a == b:
        break

    if judge2:
        sorted_index += 1
        continue
    
    
    judge = False
    break

if judge:
    print('Yes')
else:
    print('No')