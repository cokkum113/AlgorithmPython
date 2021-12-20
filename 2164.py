import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

deque1 = deque()
for i in range(n):
    deque1.append(i + 1)

while(len(deque1) != 1):
    x = deque1.popleft()
    y = deque1.popleft()
    deque1.append(y)

print(deque1.pop())