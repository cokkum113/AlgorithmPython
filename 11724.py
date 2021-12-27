import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [False] * (n + 1)



def dfs(current, visit):
    if visit[current]:
        return
    visit[current] = True
    for n in graph[current]:
        dfs(n, visit)
cnt = 0
for i in range(1, n + 1):
    if visit[i] == False:
        dfs(i, visit)
        cnt += 1

print(cnt)