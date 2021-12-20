import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
stack = deque()
ansStack = []
for _ in range(n):
    a = int(input())
    stack.appendleft(a)


for i in range(len(stack) - 1, 0, -1):
    if(stack[i] > stack[i - 1]):
        ansStack.append(stack.popleft())
        print(ansStack)
