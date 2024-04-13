""" a, b, c, d, e, f, x = map(int, input().split())
takahashi = 0
aoki = 0

walking_time = 0
copy_x = x
while copy_x > 0:
    if copy_x >= a:
        copy_x -= a
        walking_time += a
    else:
        walking_time = x
        break
    copy_x -= c

takahashi = b * walking_time

walking_time = 0

while x > 0:
    if x >= d:
        x -= d
        walking_time += d
    else:
        walking_time = x
        break
    copy_x -= f

aoki = e * walking_time

if takahashi > aoki:
    print('Takahashi')
elif aoki > takahashi:
    print('Aoki')
else:
    print('Draw') """


# Right solution

a, b, c, d, e, f, x = map(int, input().split())
takahashi = 0
aoki = 0
copy_x = x

while copy_x > 0:
    if copy_x > a:
        copy_x -= a
        takahashi += b * a
    else:
        takahashi += b * copy_x
        break
    if copy_x > c:
        copy_x -= c
    else:
        break

while x > 0:
    if x > d:
        x -= d
        aoki += e * d
    else:
        aoki += e * x
        break
    if x > f:
        x -= f
    else:
        break

if takahashi > aoki:
    print('Takahashi')
elif aoki > takahashi:
    print('Aoki')
else:
    print('Draw')
