import sys
input = sys.stdin.readline

n = int(input())
s = input().split()

nums = [int(i) for i in s]

ans = [0] * n
ans[0] = 0

stack = []

for i in range(n):
    while stack:
        if (stack[-1][1] > nums[i]):
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, nums[i]])

for a in ans:
    print(a, end=' ')