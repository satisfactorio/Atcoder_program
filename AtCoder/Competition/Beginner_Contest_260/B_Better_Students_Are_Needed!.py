import copy

n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_and_b = []
for i in range(n):
    a_and_b.append(a[i] + b[i])

answer = []

a_b_hash_table = dict(zip(tuple(range(n)), tuple(zip(a, b))))
a_order = []
sorted_a = list(sorted(set(a), reverse=True))
for v in sorted_a:
    for i in range(n):
        if a[i] == v:
            a_order.append(i)

answer.extend(a_order[:x])

for i in a_order[:x]:    
    del a_b_hash_table[i]

updated_b = copy.deepcopy(b)
for num in a_order[:x]:
    del updated_b[num]

b_order = []
sorted_b = list(sorted(set(updated_b), reverse=True))
for v in sorted_b:
    for i in range(n):
        if b[i] == v:
            b_order.append(i)

answer.extend(b_order[:y])

for i in b_order[:y]:    
    del a_b_hash_table[i]

total_of_a_b = {}
for k, v in a_b_hash_table.items():
    total_of_a_b[k] = v[0] + v[1]

total_of_a_b_list = []
for v in total_of_a_b.values():
    total_of_a_b_list.append(v)

total_of_a_b_list.sort(reverse=True)

a_b_order = []
for v in total_of_a_b_list:
    for i in range(n):
        if a_and_b[i] == v:
                a_b_order.append(i)

answer.extend(a_b_order[:z])
answer.sort()
for i in answer:
    print(i + 1)

