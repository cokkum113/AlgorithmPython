import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())

edge = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])

distance = [1001] * (n + 1)
visited = [False] * (n + 1)
start = 1
distance[start] = 0
visited[start] = True
pq = []
for e in edge[start]:
    if e[0] <= distance[e[1]] and visited[e[0]] == False:
        distance[e[1]] = e[0]
        heapq.heappush(pq, e)


cnt = 0
ans = 0
maximum = 0
while cnt < n - 1:
    ed = heapq.heappop(pq)
    if visited[ed[1]]:
        continue
    cnt += 1
    ans += ed[0]
    visited[ed[1]] = True
    for next in edge[ed[1]]:
        if distance[next[1]] <= next[0] and visited[next[1]] == False:
            continue
        heapq.heappush(pq, next)  
        distance[next[1]] = next[0]   
    maximum = max(maximum, ed[0])
    
print(ans - maximum)