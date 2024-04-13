""" n = int(input())
poem_and_scores = []
for i in range(n):
    poem_and_scores.append(list(input().split()))

originals = []
poems = []

for i in range(n):
    if poem_and_scores[i][0] not in poems:
        originals.append([poem_and_scores[i][0], int(poem_and_scores[i][1]), i + 1])
        poems.append(poem_and_scores[i][0])
    else:
        poem = poem_and_scores[i][0]
        for j in range(len(originals)):
            if originals[j - 1][0] == poem:
                del originals[j]
        
max_score_and_order = [originals[0][1], originals[0][2]]
for i in range(1, n):
    if originals[i - 1][1] > max_score_and_order[0]:
        max_score_and_order = [originals[i][1], originals[i][2]]
    
print(max_score_and_order[1]) """
        


# Right solution

n = int(input())

poem_and_scores = []
for i in range(n):
    poem_and_scores.append(list(input().split()))
    



    
