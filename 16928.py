import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

bridge = [0] * 101

visit = [False] * 101

for _ in range(n):
    x, y = map(int, input().split())
    bridge[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    bridge[x] = y

def bfs(sp):
    ans = int(1e9)

    que = deque()
    que.append([sp, 0])
    visit[sp] = True
    while True:
        status = que.popleft()
        if status[0] == 100:
            ans = min(ans, status[1])
            return ans
        
        if 0 <= status[0] + 1 <= 100 and visit[status[0] + 1] == False:
            visit[status[0] + 1] = True
            que.append([status[0] + 1, status[1] + 1])
        
        if  0 <= status[0] + 1 <= 100 and bridge[status[0] + 1] != 0:
            que.append([bridge[status[0] + 1], status[1] + 1]) 
            visit[bridge[status[0] + 1]] = True
        
        if 0 <= status[0] + 2 <= 100 and visit[status[0] + 2] == False:
            visit[status[0] + 2] = True
            que.append([status[0] + 2, status[1] + 1])

        if 0 <= status[0] + 2 <= 100 and bridge[status[0] + 2] != 0:
            que.append([bridge[status[0] + 2], status[1] + 1]) 
            visit[bridge[status[0] + 2]] = True
        
        if 0 <= status[0] + 3 <= 100 and visit[status[0] + 3] == False:
            visit[status[0] + 3] = True
            que.append([status[0] + 3, status[1] + 1])

        if  0 <= status[0] + 3 <= 100 and bridge[status[0] + 3] != 0:
            que.append([bridge[status[0] + 3], status[1] + 1]) 
            visit[bridge[status[0] + 3]] = True

        if 0 <= status[0] + 4 <= 100 and visit[status[0] + 4] == False:
            visit[status[0] + 4] = True
            que.append([status[0] + 4, status[1] + 1])
        
        if 0 <= status[0] + 4 <= 100 and bridge[status[0] + 4] != 0:
            que.append([bridge[status[0] + 4], status[1] + 1]) 
            visit[bridge[status[0] + 4]] = True
        
        if 0 <= status[0] + 5 <= 100 and visit[status[0] + 5] == False:
            visit[status[0] + 5] = True
            que.append([status[0] + 5, status[1] + 1])

        if 0 <= status[0] + 5 <= 100 and bridge[status[0] + 5] != 0:
            que.append([bridge[status[0] + 5], status[1] + 1]) 
            visit[bridge[status[0] + 5]] = True
        
        if 0 <= status[0] + 6 <= 100 and visit[status[0] + 6] == False:
            visit[status[0] + 6] = True
            que.append([status[0] + 6, status[1] + 1])

        if 0 <= status[0] + 6 <= 100 and bridge[status[0] + 6] != 0:
            que.append([bridge[status[0] + 6], status[1] + 1]) 
            visit[bridge[status[0] + 6]] = True
print(bfs(1))