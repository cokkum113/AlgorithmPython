import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(n):
    s = input().rstrip()
    for j in s:
        graph[i].append(int(j))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]




#0 : 갈 수 있는 길 
#1 : 벽이기 때문에 못감, one_cnt == 0 이면 갈수 있음
#2 : 벽을 부수지않은 상태에서 왔던길
#3 : 벽을 부순 상태에서 왔던길

def bfs(x, y):
    one_cnt = 0
    que = deque()
    que.append([x, y, one_cnt])

    graph[0][0] = 2
    cnt = -1

    while que:
        cnt += 1
        for _ in range(len(que)):
            status = que.popleft()
            if status[0] == n -1 and status[1] == m - 1:
                return cnt + 1
            
            for i in range(4):
                nx = dx[i] + status[0]
                ny = dy[i] + status[1]
                if (0 <= nx < n and 0 <= ny < m):
                    if status[2] == 0:
                        if graph[nx][ny] == 0:
                            graph[nx][ny] = 2
                            que.append([nx, ny, status[2]])
                            #status[2] 는 one_cnt
                        elif graph[nx][ny] == 1:
                            que.append([nx, ny, 1])
                        
                        elif graph[nx][ny] == 3:
                            que.append([nx, ny, status[2]])
                            graph[nx][ny] = 2
                    elif status[2] == 1:
                        #one_cnt = 1 일때
                        if graph[nx][ny] == 0:
                            graph[nx][ny] = 3
                            que.append([nx, ny, status[2]])
    return -1
    

print(bfs(0, 0))