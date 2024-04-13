h1, h2, h3, w1, w2, w3 = map(int, input().split())
count = 0

def make_array(num):
    arrays = []
    for i in range(1, num - 1):
        for j in range(1, num - 1):
            if num - i - j >= 1:
                array = [i, j, num - i - j]
                arrays.append(array)
    
    return (arrays)

h1_arrays = make_array(h1)
h2_arrays = make_array(h2)
h3_arrays = make_array(h3)

for h1_array in h1_arrays:
    for h2_array in h2_arrays:
        for h3_array in h3_arrays:
            if h1_array[0] + h2_array[0] + h3_array[0] == w1 and h1_array[1] + h2_array[1] + h3_array[1] == w2 and h1_array[2] + h2_array[2] + h3_array[2] == w3:
                count += 1
            
print(count)
