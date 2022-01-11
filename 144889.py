import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


n = int(input())

graph = [[] for _ in range(n)]

for i in range(n):
    x = list(map(int, input().split()))
    for j in x:
        graph[i].append(j)

visit = [False] * n
mini = 10**9
ans = 0
def backtracking(st, index):
    if st == n//2:
        global cnt
        global mini
        global ans
        starttotal = 0
        linktotal = 0
        start = []
        link = []
        for i in range(n):
            if visit[i]:
                start.append(i)
            else:
                link.append(i)
        for i in range(n//2):
            for j in range(n//2):
                starttotal += graph[start[i]][start[j]] + graph[start[j]][start[i]]
                linktotal += graph[link[i]][link[j]] + graph[link[j]][link[i]]
        
        ans = abs(starttotal - linktotal)
        mini = min(ans, mini)
        return

    for i in range(index, n):
        if visit[i]:
            continue
        visit[i] = True
        backtracking(st + 1, i)
        visit[i] = False


backtracking(0,0)
print(mini//2)

