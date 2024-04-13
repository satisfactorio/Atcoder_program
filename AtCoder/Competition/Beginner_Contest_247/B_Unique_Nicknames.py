n = int(input())
names = []
for i in range(n):
    name = list(input().split())
    names.append(name)

judge = True
for i in range(n):
    judge1 = True
    judge2 = True
    for j in range(n):
        if j != i:
            for k in range(2):
                if names[i][0] == names[j][k]:
                    judge1 = False
        if j != i :
            for k in range(2):
                if names[i][1] == names[j][k]:
                    judge2 = False            
    if judge1 == False and judge2 == False:
        judge = False
        break
if not judge:
    print('No')
else:
    print('Yes')