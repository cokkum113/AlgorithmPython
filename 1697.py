import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

visit = [False] * 1000001

def bfs(sp, dp):
    que = deque()
    que.append([sp, 0])
    visit[sp] = True
    while que:
        status = que.popleft()
        if status[0] == dp:
            return status[1]
        if 0 <= status[0] + 1 <= 1000000 and visit[status[0] + 1] == False:
            que.append([status[0] + 1, status[1] + 1])
            visit[status[0] + 1] = True
        if 0 <= status[0] - 1 <= 1000000 and visit[status[0] - 1] == False:
            que.append([status[0] - 1, status[1] + 1])
            visit[status[0] - 1] = True
        if 0 <= status[0] * 2 <= 1000000 and visit[status[0] * 2] == False:
            que.append([status[0] * 2, status[1] + 1])
            visit[status[0] * 2] = True
    
print(bfs(n, k))



