n, q = map(int, input().split())
numbers = list(map(int, input().split()))
queries = []

for i in range(q):
    query = list(map(int, input().split()))
    queries.append(query)


for query in queries:
    result = []
    for index, value in enumerate(numbers):
        if value == query[0]:
            result.append(index)
    if not result:
        print(-1)
    elif len(result) < query[1]:
        print(-1)
    else:
        print(result[query[1] - 1] + 1)