""" n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
judge = True
for i in range(n - 1):
    if abs(a[i] - a[i + 1]) > k and abs(a[i] - b[i + 1]) > k and abs(b[i] - a[i + 1]) > k and abs(b[i] - b[i + 1]) > k:
        judge = False
        break
if judge:
    print('Yes')
else:
    print('No') """


# Right Solution


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
distance1 = []
distance2 = []
distance3 = []
distance4 = []
for i in range(n - 1):
    distance = abs(a[i] - a[i + 1])
    distance1.append(distance)
for i in range(n - 1):
    distance = abs(a[i] - b[i + 1])
    distance2.append(distance)
for i in range(n - 1):
    distance = abs(b[i] - a[i + 1])
    distance3.append(distance)
for i in range(n - 1):
    distance = abs(b[i] - b[i + 1])
    distance4.append(distance)
distances = [distance1, distance2, distance3, distance4]

for column in range(n - 1):
    suggestions = []
    for row in range(4):
        suggestions.append(distances[row][column])
    if min(suggestions) > k:
        print('No')
        exit()
print('Yes')

            