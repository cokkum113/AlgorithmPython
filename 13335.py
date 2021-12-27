import sys
input = sys.stdin.readline
from collections import deque

n, w, l = map(int, input().split())
nums = list(map(int, input().split()))
numList = deque()
for i in nums:
    numList.append(i)

stack = deque([0 for _ in range(w)])
cnt = 0

while numList:
    stack.popleft()
    
    if(sum(stack) + numList[0] <= l):
        y = numList.popleft()
        stack.append(y)
    else:
        stack.append(0)
    
    cnt += 1

print(cnt + w)