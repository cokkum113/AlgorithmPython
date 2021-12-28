import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())

graph = [[] for _ in range(n)]


slist = []
for i in range(n):
    slist = input().split()
    for j in slist:
        graph[i].append(int(j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
que = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append([i, j, 0])
            

def bfs():
    day = 0
    while que:
        st = que.popleft()
        day = st[2]
        for d in range(4):
            nx = st[0] + dx[d]
            ny = st[1] + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    que.append([nx, ny, st[2] + 1])
    
    return day

ans = bfs()
for lo in graph:
    for tu in lo:
        if tu == 0:
            print(-1)
            exit()
        
print(ans)
