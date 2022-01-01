from collections import deque
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
ans = [-1] * n

nums = list(map(int, input().split()))

stack = deque()

for i in range(n - 1, -1, -1):
    while stack:
        if(stack[0] > nums[i]):
            ans[i] = stack[0]
            break
        else:
            stack.popleft()
    stack.appendleft(nums[i])

for i in ans:
    print(i, end=' ')