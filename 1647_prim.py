import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())

edge = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])

visited = [False] * (n + 1)
start = 1
visited[start] = True
pq = []
for e in edge[start]:
    heapq.heappush(pq, e)

cnt = 0
ans = 0
x= 0
while cnt < n - 1:
    ed = heapq.heappop(pq)

    if visited[ed[1]]:
        continue
    visited[ed[1]] = True
    cnt += 1
    ans += ed[0]
    for next in edge[ed[1]]:
        heapq.heappush(pq, next)
    x = ed[0]

    

print(ans - x)    