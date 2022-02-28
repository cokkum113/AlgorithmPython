import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

visit = [False] * 100001

def bfs(sp, dp):
    que = deque()
    que.append([sp, 0])
    visit[sp] = True

    while que:
        status = que.popleft()
        if status[0] == dp:
            return status[1]
        
        if 0 <= status[0] - 1 < 100001 and visit[status[0] - 1] == False:
            visit[status[0] - 1] = True
            que.append([status[0] - 1 , status[1] + 1])
        
        if 0 <= status[0] * 2 < 100001 and visit[status[0] * 2] == False:
            visit[status[0] * 2] = True
            que.appendleft([status[0] * 2, status[1]])

        if 0 <= status[0] + 1 < 100001 and visit[status[0] + 1] == False:
            visit[status[0] + 1] = True
            que.append([status[0] + 1 , status[1] + 1])
        
    
        
print(bfs(n, k))