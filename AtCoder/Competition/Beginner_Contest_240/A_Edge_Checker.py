a, b = map(int, input().split())
judge = False
if a == 1:
    if b == 2 or b == 10:
        judge = True
    else:
        judge = False
elif b == 1:
    if a == 2 or a == 10:
        judge = True
    else:
        judge = False
elif a == 10:
    if b == 1 or b == 9:
        judge = True
    else:
        judge = False
elif b == 10:
    if a == 1 or a == 9:
        judge = True
    else:
        judge = False
else:
    if a == b + 1 or a == b - 1:
        judge = True
    elif b == a + 1 or b == a - 1:
        judge = True
    else:
        judge = False

if judge:
    print('Yes')
else:
    print('No')