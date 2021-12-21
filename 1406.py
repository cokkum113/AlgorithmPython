import sys
input = sys.stdin.readline
from collections import deque

s = input().rstrip()
stack = deque([i for i in s])
stack2 = deque()

n = int(input())

for _ in range(n):
    cal = input().split()

    if cal[0] == 'P':
        stack.append(cal[1])
        
    elif cal[0] == 'L' and len(stack) != 0:
        x = stack.pop()
        stack2.appendleft(x)

    elif cal[0] == 'B' and len(stack) != 0:
        x = stack.pop()


    elif cal[0] == 'D' and len(stack2) != 0:
        x = stack2.popleft()
        stack.append(x)

stack3 = stack + stack2
print(''.join(stack3))
