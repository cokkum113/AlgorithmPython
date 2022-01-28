import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
# visit = [[False] * m for _ in range(n)]

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y):
    que = deque()
    que.append([x, y])
    visit = [[False] * m for _ in range(n)]
    visit[x][y] = True
    cnt = 0
    while que:
        q = que.popleft()
        i = q[0]
        j = q[1]
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visit[nx][ny] == False:
                    visit[nx][ny] = True
                    que.append([nx, ny])
                #여기까지가 0에서 0을 만나는 애들 처리해주는 부분

                #1을 만날 때를 다르게 처리해줘야함. 1을 0으로 바꾸는 부분
                elif graph[nx][ny] == 1 and visit[nx][ny] == False:
                    visit[nx][ny] = True
                    graph[nx][ny] = 0
                    cnt += 1
    return cnt

anslist = []
t = 0
while True:
    ans = bfs(0, 0)
    if ans == 0:
        break
    #ans가 0이면 다 녹았을때 그때 답 출력
    anslist.append(ans)
    t += 1
        
print(t)
print(anslist[-1])
        




