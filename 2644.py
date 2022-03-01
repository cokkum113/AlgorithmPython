import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

st, end = map(int, input().split())

m = int(input())

anslist = [[0] for _ in range(n + 1)]
visit = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    anslist[x].append(y)
    anslist[y].append(x)


def bfs(sp, dp):
    que = deque()
    que.append([sp, 0])
    visit[sp] = True
    
    while que:
        status = que.popleft()

        if status[0] == dp:
            return status[1]
        
        for i in anslist[status[0]]:
            if visit[i] == False:
                visit[i] = True
                que.append([i, status[1] + 1])
    return -1

print(bfs(st, end))

    