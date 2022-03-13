import unittest

def tripleStep(n):

    if n < 0:
        return 0

    dp = {0: 1, 1: 1, 2: 2, 3: 4}

    for i in range(3, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

    return dp[n]

def TripleHopRecursive(x, memo):
    if x < 0:
        return 0
    memo[0] = 1
    if x >= 1:
        memo[1] = 1
    if x >= 2:
        memo[2] = memo[1] + memo[0]
    if x > 2:
        for i in range(3, x + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[x]

def Method2(x):
    memo = [-1] * (x + 1)
    return TripleHopRecursive(x, memo)

for i in range(45):
    answer = Method2(i)
    result = tripleStep(i)
    if answer != result:
        print(i)