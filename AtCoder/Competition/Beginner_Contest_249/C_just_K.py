n, k = map(int, input().split())
words = []
for i in range(n):
    words.append(input())

hashtable = {}
for word in words:
    for letter in word:
        if letter not in hashtable:
            hashtable[letter] = 1
        else:
            hashtable[letter] += 1

suggested_words = []
for key in hashtable:
    if hashtable[key] >= k:
        suggested_words.a