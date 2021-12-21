import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    important = deque(input().split())
    num = deque()
    for i in range(n):
        num.append(i)
    
    cnt = 0
    ans = num[m]

    if(n == 1):
        print(1)
        continue

    while important:
        if(important[0] == max(important)):
            cnt += 1
            if(num[0] == ans):
                print(cnt)
                break
            num.popleft()
            important.popleft()
        
        elif(important[0] < max(important)):
            x = important.popleft()
            important.append(x)
            y = num.popleft()
            num.append(y)