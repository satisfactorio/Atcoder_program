'''n, x = map(int, input().split())


for i in range(n):'''
    

# Right answer

n, x = map(int, input().split())
l = []
a = []
for i in range(n):
    l_a = list(map(int, input().split()))
    l.append(l_a[0])
    a.append(l_a[1:])

products = [1]
    
for i in range(n):
    temp = []
    for a_element in a[i]:
        for product in products:
            temp.append(a_element * product)
    products = temp

print(products.count(x))