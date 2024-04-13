n = int(input())
height_list = list(map(int, input().split()))

i = 0
while i < n - 1:
    j = i + 1
    if height_list[j] > height_list[i]:
        i += 1
    else:
        break

print(height_list[i])