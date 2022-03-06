import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

edge = [list(map(int, input().split())) for _ in range(m)]
edge2 = deque(sorted(edge, key=lambda x : x[2]))

parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i

def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    parent[rootA] = rootB

e = []
while len(e) < n - 1:
    ed = edge2.popleft()
    if find(ed[0]) != find(ed[1]):
        union(ed[0], ed[1])
        e.append(ed)
        
x = sum(list(zip(*e))[2])
ans = x - e[-1][-1]
print(ans)