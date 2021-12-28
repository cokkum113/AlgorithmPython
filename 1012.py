import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visit = [[False] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def dfs(x, y, visit):
        if visit[x][y]:
            return
        visit[x][y] = True
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == False and graph[nx][ny] == 1:
                    dfs(nx, ny, visit)
        
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visit[i][j] == False:
                dfs(i, j, visit)
                cnt += 1
    print(cnt)
