from lib2to3.pgen2 import grammar
import sys
input = sys.stdin.readline

n = int(input())
edge = int(input())

INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(edge):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

print(graph)
# [[0, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000], 
# [1000000000, 0, 2, 3, 1, 4], 
# [1000000000, 12, 0, 15, 2, 5], 
# [1000000000, 8, 5, 0, 1, 1], [1000000000, 10, 7, 13, 0, 3],
#  [1000000000, 7, 4, 10, 6, 0]]

for i in range(1, len(graph)):
    x = graph[i]
    for j in range(1, n + 1):
        c = x[j]
        if c == INF:
            c = 0
        print(c, end=' ')
    print()