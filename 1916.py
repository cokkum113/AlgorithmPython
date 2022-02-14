import sys
input = sys.stdin.readline
import heapq

heap = []

n = int(input())
m = int(input())
INF = int(1e9)

dis = [INF] * (n + 1)
visit = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, w = map(int, input().split())
    graph[x].append([w, y])

st, end = map(int, input().split())

heapq.heappush(heap, [0, st])
dis[st] = 0

while heap:
    T = heapq.heappop(heap)
    current = T[1]

    if visit[current]:
        continue
    else:
        visit[current] = True
    
    for next in graph[current]:
        if dis[next[1]] > dis[current] + next[0]:
            dis[next[1]] = dis[current] + next[0]
            heapq.heappush(heap, [dis[next[1]], next[1]])
print(dis[end])

