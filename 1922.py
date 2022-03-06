from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

edge = [list(map(int, input().split())) for _ in range(m)]
edge2 = deque(sorted(edge,key= lambda x : x[2]))

parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    
    return parent[u]

def union(a,b):
    rootA = find(a)
    rootB = find(b)
    parent[rootA] = rootB

ans = []
res = 0
while len(ans) < n - 1:
    s = edge2.popleft()
    if find(s[0]) != find(s[1]):
        union(s[0], s[1])
        ans.append(s)
        res += s[2]

# print(sum(list(zip(*ans))[2]))
print(res)
