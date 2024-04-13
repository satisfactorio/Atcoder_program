n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_value = max(a)
selected_index = []

for i in range(len(a)):
    if a[i] == max_value:
        selected_index.append(i + 1)

judge = False

for index in selected_index:
    if index in b:
        judge = True
        break

if judge:
    print('Yes')
else:
    print('No')