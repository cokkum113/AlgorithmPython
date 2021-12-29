import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

graph = [[] for _ in range(n)]
visit = [[False] * n for _ in range(n)]

graph2 = [[] for _ in range(n)]
visit2 = [[False] * n for _ in range(n)]


for i in range(n):
    s = input().rstrip()
    for j in s:
        if j == 'R':
            graph[i].append(0)
            graph2[i].append(0)
        elif j == 'G':
            graph[i].append(0)
            graph2[i].append(1)
        else:
            graph[i].append(1)
            graph2[i].append(2)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, visit):
    if visit[x][y]:
        return
    visit[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if visit[nx][ny] == False and graph[nx][ny] == graph[x][y]:
                dfs(nx, ny, visit)

def dfs2(x, y, visit):
    if visit[x][y]:
        return
    visit[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if visit[nx][ny] == False and graph2[nx][ny] == graph2[x][y]:
                dfs2(nx, ny, visit)

cnt = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            dfs(i, j, visit)
            cnt += 1

for i in range(n):
    for j in range(n):
        if visit2[i][j] == False:
            dfs2(i, j, visit2)
            cnt2 += 1

print(cnt2, cnt)