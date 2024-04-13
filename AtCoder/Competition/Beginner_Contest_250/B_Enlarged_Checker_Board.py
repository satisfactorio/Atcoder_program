n, a, b = map(int, input().split())

answer = []
top_matrix = []

row = ''
white = True

for i in range(n):
    for j in range(b):
        if white:
            row += '.'
        else:
            row += '#'
    if white:
        white = False
    else:
        white = True

for i in range(a):
    top_matrix.append(row)


reversed_matrix = []
reversed_row = ''

for state in row:
    if state == '.':
        reversed_row += '#'
    else:
        reversed_row += '.'

for i in range(a):
    reversed_matrix.append(reversed_row)

top = True

for i in range(n):
    if top == True:
        answer.append(top_matrix)
    else:
        answer.append(reversed_matrix)
    if top == True:
        top = False
    else:
        top = True

for matrix in answer:
    for row in matrix:
        print(row)

