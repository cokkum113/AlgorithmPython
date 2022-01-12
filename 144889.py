import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from itertools import combinations

n = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    x = list(map(int, input().split()))
    for j in x:
        graph[i].append(j)

indexlist = combinations(range(n), n//2)

minimum = 10**9
for t in indexlist:
    start = list(t)
    link = list(set(range(n)) - set(start))
    
    starttotal = 0
    linktotal = 0
    for i in range(n//2 - 1):
        for j in range(i + 1, n//2):
            starttotal += graph[start[i]][start[j]] + graph[start[j]][start[i]]
            linktotal += graph[link[i]][link[j]] + graph[link[j]][link[i]]
    
    minimum = min(minimum, abs(starttotal - linktotal))
print(minimum)

