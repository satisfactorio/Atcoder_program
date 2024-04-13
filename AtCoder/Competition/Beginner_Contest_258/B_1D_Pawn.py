n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

index_and_position = dict(zip(range(1, k + 1), a))

for i in l:
    judge = True
    if index_and_position[i] != n:
        for value in index_and_position.values():
            if index_and_position[i] + 1 == value:
                judge = False
                break
        
        if judge:
            index_and_position[i] += 1

print(*list(index_and_position.values()))