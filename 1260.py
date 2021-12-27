import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    e = list(map(int,input().split()))
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])

for i in range(1, n + 1):
    graph[i].sort()

visit1 = [False] * (n + 1)
visit2 = [False] * (n + 1)

def dfs(current, visit):
    if visit[current]:
        return
    print(current, end=' ')
    visit[current] = True
    for next in graph[current]:
        dfs(next, visit)

def bfs(start):
    que = deque()
    que.append(start)
    visit2[start] = True
    while que:
        t = que.popleft()
        print(t, end=' ')
        for n in graph[t]:
            if visit2[n]:
                continue
            else:
                que.append(n)
                visit2[n] = True

dfs(v, visit1)
print()
bfs(v)

