'''q = int(input())
queries = []
for i in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

a = []
for query in queries:
    if query[0] == 1:
        a.append(query[1])
    elif query[0] == 2:
        a.sort()
        if query[1] < a[0]:
            print(-1)
            continue
        else:
            max_value_index = len(a) - 1
            for i in range(len(a) - 1, -1, -1):
                if a[i] > query[1]:
                    max_value_index -= 1
                else:
                    break
        if max_value_index + 1 < query[2]:
            print(-1)
        else:
            print(a[max_value_index + 1 - query[2]])    
    elif query[0] == 3:
        a.sort()
        if query[1] > a[-1]:
            print(-1)
            continue
        else:
            min_value_index = 0
            for i in range(len(a)):
                if a[i] < query[1]:
                    min_value_index += 1
                else:
                    break
        if len(a) - min_value_index < query[2]:
            print(-1)
        else:
            print(a[min_value_index + query[2] - 1])'''


# Right answer

q = int(input())
queries = []
for i in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

    