n = int(input())
x_y_coordinates = []
for i in range(n):
    x_y = list(map(int, input().split()))
    x_y_coordinates.append(x_y)
s = input()
x_y_s = []
for i in range(n):
    x_y_s.append(x_y_coordinates[i] + [s[i]])

sorted_y = sorted(x_y_s, key = lambda x: x[1])
count = 0
while True:
    count += 1
    R_x_y = []
    L_x_y = []
    j = 0
    for i in range(j, n):
        now_y = sorted_y[i][1]
        if sorted_y[i][2] == 'R':
            R_x_y.append(sorted_y[i][:2])
        else:
            L_x_y.append(sorted_y[i][:2])
        try:
            if now_y != sorted_y[i + 1][1]:
                j = i + 1
                break
        except:
            break
    R_x_y = sorted(R_x_y)
    L_x_y = sorted(L_x_y)
    try:
        if L_x_y[-1][0] > R_x_y[0][0]:
            print('Yes')
            exit()
    except:
        pass
    if count >= n:
        break
print('No')
    
    

