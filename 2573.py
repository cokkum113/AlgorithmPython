import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] =list(map(int, input().split()))


print(graph)

