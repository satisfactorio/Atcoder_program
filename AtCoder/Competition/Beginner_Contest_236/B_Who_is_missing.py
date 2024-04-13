n = int(input())
numbers = list(map(int, input().split()))

hashtable = {}
for number in numbers:
    if not number in hashtable:
        hashtable[number] = 1
    else:
        hashtable[number] += 1
    
for key in hashtable:
    if hashtable[key] == 3:
        print(key)

