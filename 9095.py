import sys
input = sys.stdin.readline

t = int(input())

dp = [-1] * 100

dp[0] = 0
dp[1] = 1

dp[2] = 2
dp[3] = 4
dp[4] = 7

for _ in range(t):
    x = int(input())
    for i in range(5, x + 1):
        dp[i] = dp[i -1] + dp[i - 2] + dp[i - 3]
    print(dp[x])

