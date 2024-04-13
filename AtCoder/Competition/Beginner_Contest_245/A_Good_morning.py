a, b, c, d = map(int, input().split())
if 60 * a + b < 60 * c + d + 1:
    print('Takahashi')
else:
    print('Aoki')