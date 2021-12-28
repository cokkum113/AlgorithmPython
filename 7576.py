import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())

graph = [[] for _ in range(n)]

visit = [[False] * m for _ in range(n)]

slist = []
for i in range(n):
    slist = input().split()
    for j in slist:
        graph[i].append(int(j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            x = i
            y = j


def bfs(x, y):
    que = deque()
    que.append([x, y, 0])
    visit[x][y] = True
    while que:
        st = que.popleft()
        for d in range(4):
            nx = st[0] + dx[d]
            ny = st[1] + dy[d]
            
            if 0 <= nx < m and 0 <= ny < n:
                if visit[nx][ny] == False and graph[st[0]][st[1]] == 1:
                    graph[nx][ny] = 1
                    visit[nx][ny] = True
                    que.append([nx, ny, st[2] + 1])
    
    return st[2]

print(bfs(x,y))
