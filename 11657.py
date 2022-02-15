import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
graph = [INF] * (n + 1)

arr = [[] for _ in range(n + 1)]
graph[1] = 0 #시작점

for _ in range(m):
    a,b,c = map(int, input().split())
    arr[a].append([b, c])


flag = True
for re in range(n):
    for i in range(1, n + 1):
        for B, C in arr[i]:
            if graph[i] != INF and graph[B] > graph[i] + C:
                graph[B] = graph[i] + C
                if re == n - 1:
                    flag = False

if flag:
    for i in graph[2:]:
        if i == INF:
            print(-1)
        else:
            print(i)
else:
    print(-1)
