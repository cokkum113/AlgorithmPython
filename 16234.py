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

flag = 0
#움직일때 사용될 깃발


def bfs(x, y):
    global flag
    unit_sum = 0
    unit_cnt = 1

    que = deque()
    que.append([x, y])
    visit[x][y] = True

    xy_list = []
    xy_list.append([x, y])

    while que:
        q = que.popleft()
        i = q[0]
        j = q[1]
        unit_sum += graph[i][j]
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                diff = abs(graph[nx][ny] - graph[i][j])
                if l <= diff <= r:
                    if visit[nx][ny] == False:
                        visit[nx][ny] = True 
                        que.append([nx, ny])
                        xy_list.append([nx, ny])  
                        unit_cnt += 1
    if unit_cnt > 1:
        flag = 1
        new_block = unit_sum // unit_cnt
        while xy_list:
            tmp = xy_list.pop()
            ch_x = tmp[0]
            ch_y = tmp[1]
            graph[ch_x][ch_y] = new_block
    
                    
cnt = 0
while True:
    flag = 0
    visit = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False:
                bfs(i, j)

    if flag == 1:
        cnt += 1
    else:
        break

print(cnt)
                        
                
                
    