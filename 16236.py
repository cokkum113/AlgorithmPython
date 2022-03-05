import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

baby_shark = 2
#아기 상어 위치를 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            baby_x = i
            baby_y = j

graph[baby_x][baby_y] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(baby_x, baby_y, baby_shark):
    que = deque()
    move = 0
    que.append([baby_x, baby_y, move])
    visited = [[False] * n for _ in range(n)]

    visited[baby_x][baby_y] = True

    fish = []
    
    while que:
        status = que.popleft()
        for i in range(4):
            nx = status[0] + dx[i]
            ny = status[1] + dy[i]

            if 0<= nx < n and 0<= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = True
                if graph[nx][ny] < baby_shark and graph[nx][ny] != 0:
                    fish.append([nx, ny, status[2] + 1])
                    que.append([nx, ny, status[2] + 1])
                    visited[nx][ny] = True

                elif graph[nx][ny] == 0 or graph[nx][ny] == baby_shark:
                    visited[nx][ny] = True
                    que.append([nx, ny, status[2] + 1])
    
    fish.sort(key=lambda x : (x[2], x[0], x[1]))
    if fish:
        return [fish[0][0], fish[0][1], fish[0][2]]
    else:
        return 0


ans = 0
eat_cnt= 0
while True:
    fishes = bfs(baby_x, baby_y, baby_shark)
    if fishes != 0:
        graph[fishes[0]][fishes[1]] = 0
        #먹었음
        eat_cnt += 1
        ans += fishes[2]
        # 이동한거리

        if eat_cnt == baby_shark:
            baby_shark += 1
            eat_cnt = 0
        
        baby_x = fishes[0]
        baby_y = fishes[1]

    else:
        break

print(ans)   

    




