# n, m = map(int, input().split())
# pairs = []

# for i in range(m):
#     pair = list(input().split())
#     pairs.append(pair)
# answer = 0

# for i, pair in enumerate(pairs):
#     for j in range(i + 1, m):
#         if pair[1] == pairs[j][0]:
#             next = pairs[j][1]
#             for k in range(i + 1, m):
#                 if set(pairs[k]) == set((pair[0], next)):
#                     answer += 1
#         elif pair[1] == pairs[j][1]:
#             next = pairs[j][0]
#             for k in range(i + 1, m):
#                 if set(pairs[k]) == set((pair[0], next)):
#                     answer += 1

# print(answer)


# better solution

n, m = map(int, input().split())
pairs = []

for i in range(m):
    pair = list(input().split())
    pairs.append(pair)
answer = 0

for i in range(m - 2):
    for j in range(i + 1, m - 1): 
        judge = False
        for k in range(j + 1, m):
            vertex_set = {pairs[i][0], pairs[i][1], pairs[j][0], pairs[j][1], pairs[k][0], pairs[k][1]}
            if len(vertex_set) == 3:
                answer += 1
                judge2 = True
                break
        if judge:
            break
        
print(answer)



