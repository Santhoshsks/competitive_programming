def min_copper_coins(n):
    if n == 0:
        return 0
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
        if i >= 2:
            dp[i] = min(dp[i], dp[i - 2] + 1)
        if i >= 4:
            dp[i] = min(dp[i], dp[i - 4] + 1)
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    result = min_copper_coins(n)
    print(result)
