from operator import ge
from random import randrange
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

anslist = []
for i in range(1, len(graph)):
    x = graph[i]
    total = 0
    for j in range(1, len(x)):
        total += x[j]
    anslist.append(total)
mini = INF
for i in range(len(anslist)):
    if anslist[i] < mini:
        mini = anslist[i]
        ans = i
print(ans + 1)

