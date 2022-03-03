import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
#결국 이렇게 하면 완전탐색인데...

#lo = 0
#hi = 0
# while True:
#     if lo == n - 1:
#         break

#     if total in nums[hi:]:
#         cnt += 1
ans = 0
for i in range(n):
    numlist = nums[:i] + nums[i + 1:]
    lo = 0
    hi = n - 2 #i번째 수도 빼야하니까

    while lo < hi:
        total = numlist[lo] + numlist[hi]
        if total > nums[i]:
            hi -= 1
            total = numlist[lo] + numlist[hi]
        elif total < nums[i]:
            lo += 1
            total = numlist[lo] + numlist[hi]
        elif total == nums[i]:
            ans += 1
            break

print(ans)


