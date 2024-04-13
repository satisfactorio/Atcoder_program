n = int(input())
matrix = []
for i in range(n):
    s = list(input())
    matrix.append(s)

def search_right(row, column):
    count = 0
    for i in range(6):
        if matrix[row][column + i] == '#':
            count += 1
    return count

def search_down(row, column):
    count = 0
    for i in range(6):
        if matrix[row + i][column] == '#':
            count += 1
    return count

def search_right_down(row, column):
    count = 0
    for i in range(6):
        if matrix[row + i][column + i] == '#':
            count += 1
    return count

def search_left_down(row, column):
    count = 0
    for i in range(6):
        if matrix[row + i][column - i] == '#':
            count += 1
    return count

for row in range(n):
    for column in range(n):
        if column + 5 < n:
            if search_right(row, column) >= 4:
                print('Yes')
                exit()
        if row + 5 < n:
            if search_down(row, column) >= 4:
                print('Yes')
                exit()
        if column + 5 < n and row + 5 < n:
            if search_right_down(row, column) >= 4:
                print('Yes')
                exit()
        if column - 5 >= 0 and row + 5 < n:
            if search_left_down(row, column) >= 4:
                print('Yes')
                exit()

print('No')

