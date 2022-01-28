from re import T
import sys
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())

graph = []
for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

# visit = [[False] * n for _ in range(n)]
#따로 값을 세주는 카운트가 따로 있어야할거 같음 , 갱신하도록 값들을
#그 각 칸의 값을 갱신하는 값이 필요함
#새롭게 그래프하나를 만들어주기 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
sumlist = []
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
                        bfs(nx,ny)
cnt = 0
visit = [[False] * n for _ in range(n)]
while True:
    new_graph = [[0] * n for _ in range(n)]
    new_block = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False:
                bfs(i, j)
                new_block = sum(sumlist) // len(sumlist)
                # print(new_block)
                new_graph[i][j] = new_block
            cnt += 1
                
    break
                
print(cnt)