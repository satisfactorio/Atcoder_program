a, b = map(int, input().split())
distance = (a ** 2 + b ** 2) ** (1 / 2)
print(a / distance, b / distance)