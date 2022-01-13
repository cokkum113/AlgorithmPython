import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [[] for _ in range(r)]

for i in range(r):
    s = input().rstrip()
    for j in s:
        graph[i].append(j)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x in range(r):
    for y in range(c):
        cnt = 0
        if graph[x][y] == 'X':
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or ny < 0 or ny >= c or nx >= r:
                    cnt += 1
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == '.':
                        cnt += 1
            if cnt >= 3:
                graph[x][y] = 'ch'

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'ch':
            graph[i][j] = '.'
            
start_x = 11
start_y = 11
end_x = 0
end_y = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'X':
            if i < start_x:
                start_x = i
            if j < start_y:
                start_y = j
            if i > end_x:
                end_x = i
            if j > end_y:
                end_y = j

new_graph = [[' '] * (end_y + 1) for _ in range(end_x + 1)]
for i in range(start_x,end_x + 1):
    for j in range(start_y,end_y + 1):
        new_graph[i][j] = graph[i][j]
        

for i in range(len(new_graph)):
    for j in range(end_y + 1):
        if new_graph[i][j] != 'X' and new_graph[i][j] != '.':
            new_graph[i][j] = ''
            
for i in new_graph:
    if not '' in i or 'X' in i or '.' in i:
        print(''.join(i))