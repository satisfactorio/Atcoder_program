n = int(input())
suggestions = []
for i in range(1, 2 * n + 2):
    suggestions.append(i)
for i in range(1, 2 * n + 3):
    if i % 2 == 1:
        print(suggestions[0])
        del suggestions[0]
    elif i == 2 * n + 2:
        x = int(input())
        exit()
    else:
        x = int(input())
        suggestions.remove(x)
        

