import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [[[0] * m for _  in range(n)]for _ in range(2)]

for i in range(n):
    s = input().rstrip()
    for j in s:
        graph[i].append(int(j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = -1

def bfs(x, y):
    global ans
    one_cnt = 0
    que = deque()
    que.append([one_cnt, x, y, 1])
    visited[0][0][0] = 1

    while que:
        status = que.popleft()
        if status[1] == n - 1 and status[2] == m - 1:
            ans = status[3] 
            break
        for i in range(4):
            nx = status[1] + dx[i]
            ny = status[2] + dy[i]
            if (0<=nx<n and 0<=ny<m):

                if graph[nx][ny] == 0 and visited[status[0]][nx][ny] == 0:
                    visited[status[0]][nx][ny] = 1
                    que.append([status[0], nx, ny, status[3] + 1])
                
                elif graph[nx][ny] == 1:
                    if status[0] == 0 and visited[0][nx][ny] == 0:
                        visited[1][nx][ny] = 1 
                        que.append([status[0] + 1, nx, ny, status[3] + 1])
       
        
    return ans

if n == 1 and m == 1:
    print(1)
else:
    print(bfs(0, 0))
    

