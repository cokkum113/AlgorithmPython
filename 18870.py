import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
ans = []
ans = nums.copy()

nums = set(nums)
nums = sorted(nums)


dict1 = dict()
for i in range(len(nums)):
    dict1[nums[i]] = i

for i in ans:
    print(dict1[i], end= ' ')
