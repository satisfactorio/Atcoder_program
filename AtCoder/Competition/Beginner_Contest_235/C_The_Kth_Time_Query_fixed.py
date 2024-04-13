n, q = map(int, input().split())
numbers = list(map(int, input().split()))
queries = []

for i in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

hashtable = {}

for index in range(len(numbers)):
    if numbers[index] not in hashtable:
        hashtable[numbers[index]] = [index + 1]

    else:
        hashtable[numbers[index]].append(index + 1)

for query in queries:
    try:
        ans = hashtable[query[0]][query[1] - 1]
        print(ans)
    except:
        print(-1)

