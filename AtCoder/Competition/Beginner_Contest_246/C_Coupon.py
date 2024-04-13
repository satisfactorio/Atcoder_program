n, k, x = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)

div = [i // x for i in a]
div = sum(div)
if div >= k:
    print(total - k * x)
else:
    total -= (div * x)
    count = k - div
    mod = [i % x for i in a]
    mod.sort()
    index = -1
    for i in range(count):
        try:
            total -= mod[index]
            index -= 1
        except:
            print(0)
            exit()
    print(total)