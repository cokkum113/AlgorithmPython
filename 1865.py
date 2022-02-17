import sys
input = sys.stdin.readline

tc = int(input())
INF = int(1e9)

def bellmanford(s):
    graph[s] = 0
    for re in range(1, n + 1):
        for i in range(1, n + 1):
            for next, t in edge[i]:
                if graph[next] > graph[i] + t:
                    graph[next] = graph[i] + t
                    if re == n:
                        return True
    return False

for _ in range(tc):
    n, m, w = map(int, input().split())

    graph = [INF] * (n + 1)
    edge = [[] for _ in range(n + 1)]

    for _ in range(m):
        S, E, T = map(int, input().split())
        edge[S].append([E, T])
        edge[E].append([S, T])
    for _ in range(w):
        S, E, T = map(int, input().split())
        edge[S].append([E, -T])

    if bellmanford(1):
        print("YES")
    else:
        print("NO")



