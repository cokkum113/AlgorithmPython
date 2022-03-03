import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(r)]
graph2 = [[' '] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        graph2[i][j] = ord(graph[i][j]) - ord('A')

anslist = []
anslist.append(graph2[0][0])
ans =0


dx = [-1, 0, 1, 0]
dy = [0,1,0,-1]

def dfs(x, y, cnt):
    global ans 
    ans = max(ans, cnt)
    for i in range(4): 
        nx = x + dx[i] 
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and graph2[nx][ny] not in anslist:
            anslist.append(graph2[nx][ny])
            dfs(nx, ny, cnt+1) 
            anslist.pop()

dfs(0,0,1) 
print(ans)

