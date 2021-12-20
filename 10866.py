import sys
input = sys.stdin.readline
from collections import deque

deque1 = deque()
n = int(input())

for _ in range(n):
    s = input().split()
    
    if s[0] == 'push_front':
        deque1.appendleft(s[1])
        
    elif s[0] == 'push_back':
        deque1.append(s[1])
        
    elif s[0] == 'pop_front':
        if(len(deque1) == 0):
            print('-1')
        else:
            x = deque1.popleft()
            print(x)

    elif s[0] == 'pop_back':
        if(len(deque1) == 0):
            print('-1')
        else:
            print(deque1.pop())
    
    
    elif s[0] == 'size':
        print(len(deque1))
    elif s[0] == 'empty':
        if(len(deque1) == 0):
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if(len(deque1) == 0):
            print(-1)
        else:
            print(deque1[0])
    elif s[0] == 'back':
        if(len(deque1) == 0):
            print(-1)
        else:
            print(deque1[-1])

