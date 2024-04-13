import string
from types import new_class

s = input()
t = input()

alphabet = string.ascii_lowercase * 2
s_index_list = []

for word in s:
    s_index_list.append(alphabet.index(word))

judge = False

for i in range(26):
    new_s = ''
    for k in range(len(s_index_list)):
        s_index_list[k] += 1
        new_s += alphabet[s_index_list[k]]

    if t == new_s:
        judge = True
        break

if judge:
    print('Yes')
else:
    print('No')





    



    
    
   





        
    

    

    
    
