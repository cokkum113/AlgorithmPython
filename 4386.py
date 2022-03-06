import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
xylist = []
for i in range(n):
    x, y = map(float, input().split())
    xylist.append([x, y])

distance = []
for i in range(n - 1):
    for j in range(i + 1, n):
        dis = (((xylist[i][0] - xylist[j][0])**2) + ((xylist[i][1] - xylist[j][1])**2))**0.5
        distance.append([dis,i, j])

distance2 = deque(sorted(distance, key=lambda x : x[0]))

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

tree = []
while len(tree) < n - 1:
    e = distance2.popleft()
    if find(e[1]) != find(e[2]):
        union(e[1], e[2])
        tree.append(e)

ans = 0
for i in tree:
    ans += i[0]
print(round(ans, 2))