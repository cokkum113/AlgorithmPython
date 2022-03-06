import sys
input = sys.stdin.readline
import heapq

v, e = map(int, input().split())

edge = [[] for _ in range(v + 1)]

for i in range(e):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])

start = 1
pq = []
for e in edge[start]:
    heapq.heappush(pq, e)

cnt = 0
ans = 0
visited = [False] * (v + 1)
visited[start] = True

while cnt < v - 1:
    ed = heapq.heappop(pq)
    if visited[ed[1]]:
        continue
    cnt += 1
    visited[ed[1]] = True
    ans += ed[0]
    for next in edge[ed[1]]:
        heapq.heappush(pq, next)

print(ans)