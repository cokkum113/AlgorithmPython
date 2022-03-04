import sys
input = sys.stdin.readline
from collections import deque
#뭔가 연결요소랑 섞어 풀면 될듯한데
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    graph[i] =list(map(int, input().split()))

cnt = 0
#true ///1보다 크면 -1 이라고하고, 1이랑같으면 -10라고하고 //-10 이면 그때 cnt를 리턴

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    global cnt
    que = deque()
    que.append([x, y])
    visited[x][y] = True

    while que:
        status = que.popleft()

        cnt += 1
        for i in range(4):
            nx = status[0] + dx[i]
            ny = status[1] + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] > 1:
                    graph[nx][ny] = graph[nx][ny] - 1
                    que.append([nx, ny])
                elif graph[nx][ny] == 1:
                    return cnt
               

print(bfs(0, 0))

