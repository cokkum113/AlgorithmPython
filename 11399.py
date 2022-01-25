import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
cnt = 0
sumlist = []
for i in nums:
    cnt += i
    sumlist.append(cnt)
print(sum(sumlist))