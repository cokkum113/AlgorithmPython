import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
tlist = []
for i in range(t):
    s = deque(list(input().rstrip()))
    tlist.append(s)

def rotation(dir, change):
    if dir == 1:
        change.appendleft(change.pop())
    elif dir == -1:
        change.append(change.popleft())

k = int(input())
r = 2
l = 6
for i in range(k):
    num, dir = map(int, input().split())
    before = num
    after = num
    for j in range(num - 1, t - 1):
        if tlist[j][r] != tlist[j + 1][l]:
            after += 1
            dir = -dir
        else:
            break
    for j in range(num - 1, 0, -1):
        if tlist[j][l] != tlist[j - 1][r]:
            before -= 1
            dir = -dir
        else:
            break
    
    for j in range(before - 1, after):
        rotation(dir, tlist[j])
        dir = -dir
        
        
        
ans = 0
for i in range(t):
    if tlist[i][0] == '1':
        ans += 1
print(ans)

