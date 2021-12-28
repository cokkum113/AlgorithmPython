import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())

visit = [[False] * n for _ in range(n)]

graph = [[] for _ in range(n)]

for i in range(n):
    s = input().rstrip()
    for j in s:
        graph[i].append(int(j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

anslist = []
ans = 0

def dfs(x, y, visit):
    global ans
    ans += 1
    if visit[x][y]:
        return
    visit[x][y] = True
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if visit[nx][ny] == False and graph[nx][ny] == 1:
                dfs(nx, ny, visit)
                
cnt = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == False and graph[i][j] == 1:
            dfs(i, j, visit)
            cnt += 1
            anslist.append(ans)
            ans = 0
print(cnt)
anslist.sort()
for i in anslist:
    print(i)