import sys
input = sys.stdin.readline

n, x = map(int, input().split())
nums = list(map(int,input().split()))

dp = [0] * 8001

#for문을 안돌고 투포인터로 계산하기

lo = 0
hi = x - 1

dp[0] = sum(nums[:x])
cnt = 0
total = dp[0]
maximum = 0

while hi <= n - 1:
    
    if total > maximum:
        maximum = total
        cnt = 1
    elif total == maximum:
        cnt += 1
    
    if hi == n - 1:
        break
    
    total -= nums[lo]
    hi += 1
    lo += 1
    total += nums[hi]

if max(nums) == 0:
    print("SAD")
else:
    print(maximum)
    print(cnt)    


