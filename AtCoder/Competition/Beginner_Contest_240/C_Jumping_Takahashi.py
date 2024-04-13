'''import itertools

n, x = map(int, input().split())
jumps = []
for i in range(n):
    jump = list(map(int, input().split()))
    jumps.append(jump)

smallest = 0
for jump in jumps:
    smallest += jump[0]

if smallest > x:
    print('No')
elif smallest == x:
    print('Yes')
else:
    differences = []
    for jump in jumps:
        difference = jump[1] - jump[0]
        differences.append(difference)
    desired_result = x - smallest
    combis = []
    for i in range(1, len(differences) + 1):
        for c in itertools.combinations(differences, i):
            combis.append(sum(c))
    judge = False
    for addition in combis:
        if addition == desired_result:
            judge = True
            break
    if judge:
        print('Yes')
    else:
        print('No')'''


# Right Answer

n, x = map(int, input().split())
jumps = []
for i in range(n):
    jump = list(map(int, input().split()))
    jumps.append(jump)

distance = set()
distance.add(0)

for jump in jumps:
    new_distance = set()
    for now in distance:
        if now + jump[0] <= x:
            new_distance.add(now + jump[0])
        if now + jump[1] <= x:
            new_distance.add(now + jump[1])
    
    distance = new_distance

if x in distance:
    print('Yes')
else:
    print('No')