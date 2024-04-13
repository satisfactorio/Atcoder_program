n = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if len(set([a[i], a[j], a[k]])) == 3:
                count += 1

print(count)