x, a, d, n = map(int, input().split())

def a_y(a, d, y):
    return a + d * y - d


if d >= 0:
    if x <= a_y(a, d, 1):
        print(a_y(a, d, 1) - x)
    elif x >= a_y(a, d, n):
        print(x - a_y(a, d, n))
    else:
        ans = round((x - a + d) / d)
        print(abs(x - a_y(a, d, ans)))
else:
    if x >= a_y(a, d, 1):
        print(x - a_y(a, d, 1))
    elif x <= a_y(a, d, n):
        print(a_y(a, d, n) - x)
    else:
        ans = round((x - a + d) / d)
        print(abs(x - a_y(a, d, ans)))
