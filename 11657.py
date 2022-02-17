import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
graph = [INF] * (n + 1)
edge = []

for _ in range(m):
    a,b,c = map(int, input().split())
    edge.append([a,b,c])

graph[1] = 0
for i in range(n): #0 ~ n-1번
    for j in range(m):
        start = edge[j][0]
        end = edge[j][1]
        cost = edge[j][2]

        if graph[start] != INF and graph[end] > graph[start] + cost:
            graph[end] = graph[start] + cost
            if i == n-1:
                print(-1)
                exit()

for i in range(2, n + 1):
    if graph[i] == INF:
        print(-1)
    else:
        print(graph[i])
