import collections
from distutils import dep_util
import sys
input = sys.stdin.readline
from collections import deque


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# visit = [[False] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, k):
    que = deque()
    que.append([x, y])
    visit[x][y] = True

    while que:
        pos = que.popleft()
        for d in range(4):
            nx = pos[0] + dx[d]
            ny = pos[1] + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == False and graph[nx][ny] > k:
                    visit[nx][ny] = True
                    que.append([nx, ny])    


deepmax = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] >= deepmax:
            deepmax = graph[i][j]

ans = 0
for k in range(deepmax):
    visit = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and visit[i][j] == False:
                bfs(i, j, k)
                cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)






