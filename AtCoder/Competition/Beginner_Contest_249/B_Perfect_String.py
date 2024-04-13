s = input()

upper_judge = False
lower_judge = False
distinct_judge = True

for character in s:
    if character.isupper():
        upper_judge = True
        break

for character in s:
    if character.islower():
        lower_judge = True
        break

hashtable = {}
for character in s:
    if character not in hashtable:
        hashtable[character] = True
    else:
        distinct_judge = False

if upper_judge == True and lower_judge == True and distinct_judge == True:
    print('Yes')
else:
    print('No')
