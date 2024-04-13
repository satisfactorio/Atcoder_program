N = int(input())

A = list(map(int, input().split()))
count = 0
A1 = [i for i in A]

while len(A1) == N:
    A2 = []
    for i in A1:
        if i%2 == 0:
            A2.append(i/2)
    if len(A2) == N:
        count += 1
        A1 = A2
    else:
        break

print(count)
        
    




        
