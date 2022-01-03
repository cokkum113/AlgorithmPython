import sys
input = sys.stdin.readline

n = int(input())

dp = [-10001] * (n + 1)

nums = list(map(int, input().split()))

dp[0] = nums[0]

if n == 1:
    print(nums[0])
else:
    for i in range(1, n):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
    print(max(dp))