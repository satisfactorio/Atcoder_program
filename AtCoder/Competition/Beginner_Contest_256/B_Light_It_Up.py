n, k = map(int, input().split())
a = list(map(int, input().split()))
xys = []
for i in range(n):
    xy = list(map(int, input().split()))
    xys.append(xy)

have_light = []
for i in a:
    have_light.append(xys[i - 1])

not_have_light = []
b = set(range(1, n + 1))
not_have_light_index = list(b - set(a))

for i in not_have_light_index:
    not_have_light.append(xys[i - 1])

distance2 = []

for xy in not_have_light:
    distance = []
    for xy2 in have_light:
        d = abs(((xy[0] - xy2[0])**2 + (xy[1] - xy2[1])**2)**(1 / 2))
        distance.append(d)
    distance2.append(min(distance))

print(max(distance2))