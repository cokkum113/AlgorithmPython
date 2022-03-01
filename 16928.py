from os import stat
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

bridge = [[] * (101) for _ in range(101)]
snake = [[] * (101) for _ in range(101)]
#이렇게는 하나씩 쭉있어야함. 양옆으로 갈 필요가 없음

visit = [False] * (101)

for _ in range(n):
    x, y = map(int, input().split())
    bridge[x].append(y)
    bridge[y].append(x)

for _ in range(m):
    x, y = map(int, input().split())
    snake[x].append(y)

    

def bfs(sp):
    que = deque()
    que.append([sp, 0])
    visit[sp] = True
    while True:
        status = que.popleft()
        if status[0] == 100:
            return status[1]
        
        if 0 <= status[0] + 1 <= 100 and visit[status[0] + 1] == False:
            if len(snake[status[0] + 1]) != 0:
                que.append([snake[status[0] + 1, status[1] + 1]])
            if bridge[status[0] + 1] != 0 and visit[bridge[status[0] + 1]] == False:
                que.append([bridge[status[0] + 1], status[1]]) 
            visit[status[0] + 1] = True
            que.append([status[0] + 1, status[1] + 1])
        
        if 0 <= status[0] + 2 <= 100 and visit[status[0] + 2] == False:
            if len(snake[status[0] + 2]) != 0:
                que.append([snake[status[0] + 2, status[1] + 1]])
            if bridge[status[0] + 2] != 0 and visit[bridge[status[0] + 2]] == False:
                que.append([bridge[status[0] + 2], status[1]]) 
            visit[status[0] + 2] = True
            que.append([status[0] + 2, status[1] + 1])
        
        if 0 <= status[0] + 3 <= 100 and visit[status[0] + 3] == False:
            if len(snake[status[0] + 3]) != 0:
                que.append([snake[status[0] + 3, status[1] + 1]])
            if bridge[status[0] + 3] != 0 and visit[bridge[status[0] + 3]] == False:
                que.append([bridge[status[0] + 3], status[1]]) 
            visit[status[0] + 3] = True
            que.append([status[0] + 3, status[1] + 1])
        
        if 0 <= status[0] + 4 <= 100 and visit[status[0] + 4] == False:
            if len(snake[status[0] + 4]) != 0:
                que.append([snake[status[0] + 4, status[1] + 1]])
            if bridge[status[0] + 4] != 0 and visit[bridge[status[0] + 4]] == False:
                que.append([bridge[status[0] + 4], status[1]]) 
            visit[status[0] + 4] = True
            que.append([status[0] + 4, status[1] + 1])
        
        if 0 <= status[0] + 5 <= 100 and visit[status[0] + 5] == False:
            if len(snake[status[0] + 5]) != 0:
                que.append([snake[status[0] + 5, status[1] + 1]])
            if bridge[status[0] + 5] != 0 and visit[bridge[status[0] + 5]] == False:
                que.append([bridge[status[0] + 5], status[1]]) 
            visit[status[0] + 5] = True
            que.append([status[0] + 5, status[1] + 1])
        
        if 0 <= status[0] + 6 <= 100 and visit[status[0] + 6] == False:
            if len(snake[status[0] + 6]) != 0:
                que.append([snake[status[0] + 6, status[1] + 1]])
            if bridge[status[0] + 6] != 0 and visit[bridge[status[0] + 6]] == False:
                que.append([bridge[status[0] + 6], status[1]]) 
            visit[status[0] + 6] = True
            que.append([status[0] + 6, status[1] + 1])
print(bfs(1))