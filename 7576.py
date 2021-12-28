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

que = deque()


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append([i, j])
            visit[i][j] = True


def bfs():
    while que:
        st = que.popleft()
        for d in range(4):
            nx = st[0] + dx[d]
            ny = st[1] + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == False:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[st[0]][st[1]] + 1
                        visit[nx][ny] = True
                        que.append([nx, ny])

bfs()
ans = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    ans = max(ans, max(i))
print(ans - 1)