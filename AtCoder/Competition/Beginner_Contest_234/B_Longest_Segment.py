import itertools

n = int(input())
points = []
for i in range(n):
    point = list(map(int, input().split()))
    points.append(point)

two_points = list(itertools.combinations(points, 2))

distance = []
for two_point in two_points:
    d = ((two_point[1][0] - two_point[0][0])**2 + (two_point[1][1] - two_point[0][1])**2)**(1/2)
    distance.append(d)

print(max(distance))