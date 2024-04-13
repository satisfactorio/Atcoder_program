'''n = int(input())

standard = []
for num in range(1, 19):
    number = '9' * num
    standard.append(number)


def f(x, answer = 0):
    for i in range(1, x + 1):
        if i <= 9:
            answer += i
        else:'''
            

# Right answer

mod = 998244353

n = int(input())

def get_total(a, b):
    return (b - a + 1) * (a + b) // 2

answer = 0
for x in range(1, 19):
    if 10 ** x <= n:
        answer += get_total(1, 9 * 10 ** (x - 1))
    else:
        answer += get_total(1, n - 10 ** (x - 1) + 1)
        break

print(answer % mod)



