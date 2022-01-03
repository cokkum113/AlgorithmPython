import sys
input = sys.stdin.readline

n = int(input())
step = [0] * 301

for i in range(n):
    x = int(input())
    step[i] = x

dp = [0] * 301

dp[0] = step[0]
dp[1] = step[0] + step[1]
dp[2] = max(step[0] + step[2], step[1] + step[2])

for i in range(3, n):
    dp[i] = max(step[i] + dp[i - 2], step[i] + step[i - 1] + dp[i - 3])

print(dp[n - 1])