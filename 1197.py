from collections import deque
import sys
input = sys.stdin.readline

v, e = map(int, input().split())

edge = [list(map(int, input().split()))for _ in range(e)]
edge2 = deque(sorted(edge, key=lambda x : x[2]))

parent = [0] * (v + 1)

for i in range(v + 1):
    parent[i] = i

def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    parent[rootA] = rootB

tree = []
while len(tree) < v - 1:
    e = edge2.popleft()
    if find(e[0]) != find(e[1]):
        union(e[0], e[1])
        tree.append(e)



print(sum(list(zip(*tree))[2]))

