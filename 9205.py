import sys
input = sys.stdin.readline

t = int(input())
INF = int(1e9)
happy = 20 * 50

for _ in range(t):
    n = int(input())
    graph = [[INF] * (n + 2) for _ in range(n + 2)] 
    xylist = []

    for i in range(n + 2):
        x, y = map(int, input().split())
        xylist.append([x, y])
    
    for i in range(len(graph)):
        graph[i][i] = 0
    
    for i in range(n + 2):
        for j in range(n + 2):
            if abs(xylist[i][0] - xylist[j][0]) + abs(xylist[i][1] - xylist[j][1]) <= happy:
                graph[i][j] = 1
    
    for k in range(n + 2):
        for i in range(n + 2):
            for j in range(n + 2):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
    
    #[home][fes]
    if graph[0][n + 1] >= INF:
        print("sad")
    else:
        print("happy")


