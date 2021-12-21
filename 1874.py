import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

ansList = []

for _ in range(n):
    x = int(input())
    ansList.append(x)

tempList = []
result = []
num = 1
flag = 0

for i in ansList:
    while num <= i:
        tempList.append(num)
        result.append('+')
        num += 1
    
    if tempList[-1] == i :
        tempList.pop()
        result.append('-')
  
if len(tempList) == 0:
    print('\n'.join(result))
else:
    print("NO")

