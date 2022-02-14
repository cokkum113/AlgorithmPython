import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for i in range(1, len(graph)):
    x = graph[i]
    for j in range(1, len(graph)):
        y = x[j]
        if y == INF:
            y = 0
        print(y, end= ' ')
    print()
