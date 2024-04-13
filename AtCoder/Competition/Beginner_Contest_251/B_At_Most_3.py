n, w = map(int, input().split())
a = list(map(int, input().split()))

good_weight = set()

if n == 1:
    for i in range(n):
        if a[i] <= w:
            good_weight.add(a[i])

elif n == 2:
    for i in range(n):
        if a[i] <= w:
            good_weight.add(a[i])

    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = a[i] + a[j]
            if sum <= w:
                good_weight.add(sum)

else:
    for i in range(n):
        if a[i] <= w:
            good_weight.add(a[i])

    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = a[i] + a[j]
            if sum <= w:
                good_weight.add(sum)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sum = a[i] + a[j] + a[k]
                if sum <= w:
                    good_weight.add(sum)

print(len(good_weight))