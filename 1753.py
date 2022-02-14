import sys
import heapq
input = sys.stdin.readline

V, E = map(int,input().split())
start = int(input())

INF = int(1e9)
visited = [False] * (V+1)
graph = [[] for _ in range(V+1)]
dis = [INF] * (V+1)

heap = []

for i in range(E):
    u, v, w = map(int,input().split())
    graph[u].append([w, v])

heapq.heappush(heap, [0,start])
dis[start] = 0

while heap:
    T = heapq.heappop(heap)
    current = T[1]
    if visited[current]:
        continue
    else:
        visited[current] = True 
        
    for next in graph[current]:
        if dis[next[1]] > dis[current] +next[0]:
            dis[next[1]] = dis[current] +next[0]
            heapq.heappush(heap, [dis[next[1]],next[1]])
            
for i in range(1, V+1):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])