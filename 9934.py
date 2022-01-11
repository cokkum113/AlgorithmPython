from itertools import combinations
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    x = list(map(int, input().split()))
    for j in x:
        graph[i].append(j)

mini = 10**9
start = []
link = []

def backtracking(st):
    global mini
    ans = 0
    if st == n//2:
        starttotal = 0
        linktotal = 0
        for i in range(n):
            if i not in start:
                link.append(i)
        for i in range(n//2 - 1):
            for j in range(i + 1, n//2):
                starttotal += graph[start[i]][start[j]] + graph[start[j]][start[i]]
                linktotal += graph[link[i]][link[j]] + graph[link[i]][link[j]]
        ans = abs(starttotal - linktotal)
        mini = min(ans, mini)

        link.clear()
        return

    for i in range(n):
        if i in start:
            continue
        if len(start) > 0 and start[len(start) - 1] > i:
            continue
        start.append(i)
        backtracking(st + 1)
        start.pop()

print(ans)