n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

judge = True
for num in b:
    try:
        a.remove(num)
    except:
        judge = False

if judge:
    print('Yes')
else:
    print('No')
