r, c = map(int, input().split())
a_matrix = []
for i in range(2):
    a = list(map(int, input().split()))
    a_matrix.append(a)

print(a_matrix[r - 1][c - 1])