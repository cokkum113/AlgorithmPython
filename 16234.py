import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())

graph = []
for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
sumlist = []
cnt = 0
def bfs(x, y):
    que = deque()
    que.append([x, y])
    visit[x][y] = True
    sumlist.append(graph[x][y])

    while que:
        q = que.popleft()
        i = q[0]
        j = q[1]
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                diff = abs(graph[nx][ny] - graph[i][j])
                if l <= diff <= r:
                    if visit[nx][ny] == False:
                        visit[nx][ny] = True 
                        sumlist.append(graph[nx][ny])  
                        bfs(nx,ny)     

while True:
    new_graph = [[0] * n for _ in range(n)]
    new_block = 0
    visit = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False:
                bfs(i, j)
                
                if len(sumlist) > 0:
                    new_block = sum(sumlist) // len(sumlist)
                    new_graph[i][j] = new_block
                else:
                    cnt += 1
    break
print(new_graph)
print(cnt)
        