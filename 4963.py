import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [1, -1, 0, 0,1, 1, -1, -1]
dy = [0, 0, 1, -1,-1, 1, -1, 1]
def dfs(x,y, visit):
    if visit[x][y]:
        return
    visit[x][y] = True
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1 and visit[nx][ny] == False:
                dfs(nx, ny, visit)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [[] for _ in range(h)]
    visit = [[False] * w for _ in range(h)]

    for i in range(h):
        s = input().split()
        for j in s:
            graph[i].append(int(j))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visit[i][j] == False:
                dfs(i, j, visit)
                cnt += 1
    
    print(cnt)
    
    
    
