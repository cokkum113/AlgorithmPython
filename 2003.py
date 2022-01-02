import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

lw = 0
hi = 0

total = nums[0]
cnt = 0

while True:
    if hi == n - 1 and total < m:
        break
    if total > m:
        total -= nums[lw]
        lw += 1
    elif total < m:
        hi += 1
        total += nums[hi]
    else:
        total -= nums[lw]
        lw += 1
        cnt += 1

print(cnt)