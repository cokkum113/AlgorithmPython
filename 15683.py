from lib2to3.pgen2 import grammar
import sys
input = sys.stdin.readline


#우 좌 하 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

print(graph)