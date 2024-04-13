a, b, c, d = map(int, input().split())

def is_prime(n, judge = True):
    if n == 1:
        judge = False
    else:
        for i in range(2, n):
            if n % i == 0:
                judge = False
                break
    return judge


count = 0
hashtable = {}
for i in range(a, b + 1):
    Aoki = False
    count += 1
    for k in range(c, d + 1):
        if is_prime(i + k):
            Aoki = True
            break
    hashtable[count] = Aoki

judge = True
for key in range(1, 100):
    try:
        if hashtable[key] == False:
            judge = False
            break
    except:
        break

if judge:
    print('Aoki')
else:
    print('Takahashi')
