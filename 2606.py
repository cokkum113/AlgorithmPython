import sys
input = sys.stdin.readline

n = int(input())
e = int(input())

graph = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)

for i in range(e):
    s = input().split()
    graph[int(s[0])].append(int(s[1]))
    graph[int(s[1])].append(int(s[0]))

cnt = 0
def dfs(x, visit):
    global cnt
    if visit[x]:
        return
    visit[x] = True
    cnt += 1
    for n in graph[x]:
        dfs(n, visit)
        

dfs(1, visit)
print(cnt - 1)