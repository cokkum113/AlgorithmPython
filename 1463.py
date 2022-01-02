import sys
input = sys.stdin.readline

n = int(input())
dp = [-1] * 1000001

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    pre3 = n
    pre2 = n
    pre1 = n
    if i % 2 == 0:
        pre2 = dp[i//2]
    if i % 3 == 0:
        pre3 = dp[i//3]
    
    pre1 = dp[i - 1]
    
    dp[i] = min(pre1, pre2, pre3) + 1

print(dp[n])
