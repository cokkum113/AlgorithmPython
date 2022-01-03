import sys
input = sys.stdin.readline

n, x = map(int, input().split())

nums = list(map(int,input().split()))

lo = 0
hi = 0

total = nums[0]
cnt = 0
maximum = 0
day = 0

while hi != n - 1:
    # if (hi + 1) % x == 0:
    if day == x:
        day = 0
        if total > maximum:
            maximum = total
            total = nums[lo]
            cnt = 1
        elif total == maximum:
            total = nums[lo]
            cnt += 1   
        else:
            total = nums[lo]
        
    if day != x:
        hi += 1
        total += nums[hi]
        
        total += nums[lo]
        lo += 1
    day += 1
    # print(day)

print(cnt)

