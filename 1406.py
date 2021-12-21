import sys
input = sys.stdin.readline
from collections import deque

s = input().rstrip()
stack = [i for i in s]

n = int(input())
current = len(stack)

for _ in range(n):
    cal = input().split()

    if cal[0] == 'P':
        stack.insert(current, cal[1])
        current = current + 1
        
    elif cal[0] == 'L':
        if(current == 0):
            continue
        else:
            current = current - 1

    elif cal[0] == 'B':
        if(current == 0):
            continue
        else:
            del(stack[current - 1])
            # current = current - 1 
        

    elif cal[0] == 'D':
        if(current == len(stack)):
            continue
        else:
            current = current + 1

print(''.join(stack))
