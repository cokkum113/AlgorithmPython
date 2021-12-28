import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visit = [[False] * m for _ in range(n)]

for i in range(n):
    s = input().rstrip()
    for j in s:
        graph[i].append(int(j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    que = deque()
    que.append([x, y, 1])
    visit[x][y] = True
    while que:
        st = que.popleft()

        if st[0] == n - 1 and st[1] == m - 1:
            return st[2]

        for d in range(4):
            nx = st[0] + dx[d]
            ny = st[1] + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visit[nx][ny] == False:
                    visit[nx][ny] = True
                    que.append([nx, ny , st[2] + 1])
                    
                if graph[nx][ny] == 0:
                    continue
    return st[2]
print(bfs(0, 0))



