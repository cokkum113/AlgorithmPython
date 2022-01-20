import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
graph = [[] for _ in range(r)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    x = input().rstrip()
    for j in x:
        graph[i].append(j)

if n <= 1:
    for i in range(len(graph)):
        print(*graph[i],sep='')

elif n % 2 == 0:
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 'O':
                graph[i][j] = 'O'
    
    for i in range(len(graph)):
        print(*graph[i],sep='')


else:
    graph2 = [['O']*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                graph2[i][j] = '.'
            else:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < r and 0<= ny < c and graph[nx][ny] == 'O':
                        graph2[i][j] = '.'
                        break
                            
    graph3 = [['O']*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph2[i][j] == 'O':
                graph3[i][j] = '.'
            else:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < r and 0<= ny < c and graph2[nx][ny] == 'O':
                        graph3[i][j] = '.'
                        break
    
    if n % 4 == 3:
        for i in range(len(graph2)):
            print(*graph2[i],sep='')

    if n % 4 == 1:
        for i in range(len(graph2)):
            print(*graph3[i],sep='')