A, B, C, X = int(input()), int(input()), int(input()), int(input())

A1= X // 500
A2 = []
for i in range(A1):
    A2[i] = X - 500 * i

B2 = []
for i in A2:
    B1 = i // 100
    B2[i] = i - 100 * B1

C2 = []
count = 0
for i in B2:
    C1 = i //50
    C2[i] = i - 50 * C1
    if C2[i] == 0:
        count += 1

D = [len(A2), len(B2), len(C2)]


print(f'{len(A2) * len(B2) * count}')
