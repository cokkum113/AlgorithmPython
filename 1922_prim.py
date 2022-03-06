import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

edge = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])

start = 3
#아무데나 임의의 수를 설정
pq = []
for e in edge[start]:
    heapq.heappush(pq, e)

visited = [False] * (n + 1)
visited[start] = True
cnt = 0
ans = 0
while cnt < n - 1:
    weight, vertex = heapq.heappop(pq)
    if visited[vertex]:
        continue
    visited[vertex] = True
    cnt += 1
    ans += weight
    for next in edge[vertex]:
        heapq.heappush(pq, next)

print(ans)
