import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] =list(map(int, input().split()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

#ice가 나왔을 때  bfs탐색 -> bfs 탐색수 : 총 ice의 갯수
def bfs(x, y):
    que = deque()
    que.append([x, y])
    melting_ice = deque() #ice가 녹는 x,y Ice가 녹는 정도
    visited[x][y] = True

    while que:
        st = que.popleft()
        melt_cnt = 0
        for i in range(4):
            nx = st[0] + dx[i]
            ny = st[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    que.append([nx, ny])
                
                else:
                    melt_cnt += 1
                    #0이면 그만큼 녹으니까 그점이 나중에 어떻게 녹을지에 대한 카운트 수 
                    #이만큼 빼주기 위해서
        
        if melt_cnt != 0:
            melting_ice.append([st[0], st[1], melt_cnt])
    
    return melting_ice

cnt = 0
while True:
    visited = [[False] * m for _ in range(n)]
    ice = 0 #빙산의 갯수
    for i in range(n - 1):
        for j in range(m - 1):
            if graph[i][j] != 0 and visited[i][j] == False:
                #빙하가 남아있고 방문하지 않았을 경우
                ice += 1
                melt = bfs(i, j)
                while melt:
                    status = melt.popleft()
                    graph[status[0]][status[1]] = max(graph[status[0]][status[1]] - status[2], 0)
    
    if ice == 0:
        cnt = 0
        break
    if ice >= 2:
        break

    cnt += 1

print(cnt)

