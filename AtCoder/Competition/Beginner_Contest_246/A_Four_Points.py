""" x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
    if y3 == y1:
        print(x3, y2)
    elif y3 == y2:
        print(x3, y1)
elif x1 == x3:
    if y2 == y1:
        print(x2, y3)
    elif y2 == y3:
        print(x2, y1) """



x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if y1 == y2 and x1 == x3:
    print(x2, y3)
elif x1 == x2 and y1 == y3:
    print(x3, y2)
elif x2 == x3 and y2 == y1:
    print(x1, y3)
elif x2 == x1 and y2 == y3:
    print(x3, y1)
elif x3 == x1 and y3 == y2:
    print(x2, y1)
else:
    print(x1, y2)
    