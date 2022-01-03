import sys
input = sys.stdin.readline

n = int(input())
wine = []
dp = [-1] * (n + 1)
for _ in range(n):
    x = int(input())
    wine.append(x)

if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0] + wine[1])
else:

    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[1],wine[0] + wine[2], wine[1] + wine[2])

    for i in range(3, n):
        dp[i] = max(wine[i] + dp[i - 2], wine[i] + wine[i - 1] + dp[i - 3])
        dp[i] = max(dp[i - 1], dp[i])

    print(dp[n - 1])
