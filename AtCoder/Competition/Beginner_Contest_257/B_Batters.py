# n = int(input())
# a = list(map(int, input().split()))
# count = 0

# if n == 1:
#     if a[0] < 4:
#         count += 1
# elif n == 2:
#     if a[-1] + a[-2] < 4:
#         count += 1
#     if a[-1] < 4:
#         count += 1
# else:
#     if a[-1] + a[-2] + a[-3] < 4:
#         count += 1
#     if a[-1] + a[-2] < 4:
#         count += 1
#     if a[-2] < 4:
#         count += 1


# print(n - count)

n = int(input())
a = list(map(int, input().split()))
p = 0

for i in range(n):
    total = 0
    for j in range(i, n):
        total += a[j]
    if total >= 4:
        p += 1

print(p)
