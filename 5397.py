import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    stack = deque()
    stack2 = deque()

    s = input().rstrip()

    for i in range(len(s)):
        if s[i] == '<':
            if len(stack) == 0:
                continue
            else:
                x = stack.pop()
                stack2.appendleft(x)
        
        elif s[i] == '>':
            if len(stack2) == 0:
                continue
            else:
                x = stack2.popleft()
                stack.append(x)

        elif s[i] == '-':
            if(len(stack) != 0):
                stack.pop()
                 
        else:
            stack.append(s[i])
    
    stack2 = list(stack2)
    
    stack = list(stack)

    ans = stack + stack2
    print(''.join(ans))