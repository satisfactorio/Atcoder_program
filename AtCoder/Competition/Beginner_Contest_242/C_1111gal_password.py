'''n = int(input())
prefix_1 = 2
prefix_2 = 3
prefix_3 = 3
prefix_4 = 3
prefix_5 = 3
prefix_6 = 3
prefix_7 = 3
prefix_8 = 3
prefix_9 = 2

if n == 2:
    print(25)
else:
    for i in range(n - 2):
        temp_prefix_1 = prefix_1 + prefix_2
        temp_prefix_2 = prefix_1 + prefix_2 + prefix_3
        temp_prefix_3 = prefix_2 + prefix_3 + prefix_4
        temp_prefix_4 = prefix_3 + prefix_4 + prefix_5
        temp_prefix_5 = prefix_4 + prefix_5 + prefix_6
        temp_prefix_6 = prefix_5 + prefix_6 + prefix_7
        temp_prefix_7 = prefix_6 + prefix_7 + prefix_8
        temp_prefix_8 = prefix_7 + prefix_8 + prefix_9
        temp_prefix_9 = prefix_8 + prefix_9

        prefix_1 = temp_prefix_1
        prefix_2 = temp_prefix_2
        prefix_3 = temp_prefix_3
        prefix_4 = temp_prefix_4
        prefix_5 = temp_prefix_5
        prefix_6 = temp_prefix_6
        prefix_7 = temp_prefix_7
        prefix_8 = temp_prefix_8
        prefix_9 = temp_prefix_9

    print((prefix_1 + prefix_2 + prefix_3 + prefix_4 + prefix_5 + prefix_6 + prefix_7 + prefix_8 + prefix_9) % 998244353)'''



# Another solution

'''import sys
sys.setrecursionlimit(10 ** 8)

n = int(input())
MOD = 998244353
def f(n, k, memo = {}):
    if n == 2:
        if k == 1 or k == 9:
            return 2
        else:
            return 3
    else:
        if k == 1:
            if (n, k) not in memo:
                memo[n, k] = (f(n - 1, k, memo) + f(n - 1, k + 1, memo))
        elif k == 9:
            if (n, k) not in memo:
                memo[n, k] = (f(n - 1, k, memo) + f(n - 1, k - 1, memo))
        else:
            if (n, k) not in memo:
                memo[n, k] = (f(n - 1, k - 1, memo) + f(n - 1, k, memo) + f(n - 1, k + 1, memo))
        return memo[n, k]

total = 0
for i in range(1, 10):
    total += f(n, i)
print(total % MOD)'''


# Another solution

n = int(input())
MOD = 998244353
def f(n):
    dp = [[0] * 10 for i in range(n + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    
    for d in range(2, n + 1):
        for i in range(1, 10):
            if i == 1:
                dp[d][i] = dp[d - 1][i] + dp[d - 1][i + 1]
            elif 2 <= i <= 8:
                dp[d][i] = dp[d - 1][i - 1] + dp[d - 1][i] + dp[d - 1][i + 1]
            else:
                dp[d][i] = dp[d - 1][i - 1] + dp[d - 1][i]
            
            dp[d][i] %= MOD
        
    return sum(dp[n]) % MOD

print(f(n))

