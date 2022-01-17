import sys
input = sys.stdin.readline

n = int(input())


dp = [0] * (n + 1)

# [1,1,2,3,5,8,,,,]
if n == 1:
    print(1)
    exit()
elif n == 2:
    print(1)
    exit()
else:
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n])