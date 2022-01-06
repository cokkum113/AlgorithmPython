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


for i in range(r):
    for j in range(c):
        cnt = 0
        if graph[i][j] == 'X':
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if nx < 0 or ny < 0 or ny >= c or nx >= r:
                    cnt += 1
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == '.':
                        cnt += 1
            if cnt == 3 or cnt == 4:
                graph[i][j] = 'r'

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'r':
            graph[i][j] = '.'


# print(*graph)

# ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'] 
# ['.', '.', 'X', 'X', '.', '.', '.', 'X', '.', '.'] 
# ['X', 'X', 'X', '.', '.', '.', '.', '.', '.', '.']
last_index_max = 0
last_index2_max = 0
first_index_min = 11
first_index_min2 = 11
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'X':
            if i < first_index_min:
                first_index_min = i
            if j < first_index_min2:
                first_index_min2 = j
            if i > last_index_max:
                last_index_max = i
            if j > last_index2_max:
                last_index2_max = j
# print(first_index_min, first_index_min2, last_index_max, last_index2_max)

graph2 = [[' '] * (last_index2_max + 1) for _ in range(last_index_max + 1)]
for i in range(first_index_min,last_index_max + 1):
    for j in range(first_index_min2,last_index2_max + 1):
        graph2[i][j] = graph[i][j]
        

for i in range(len(graph2)):
    for j in range(last_index2_max + 1):
        if graph2[i][j] != 'X' and graph2[i][j] != '.':
            graph2[i][j] = ''
            
for i in graph2:
    if not '' in i or 'X' in i or '.' in i:
        print(''.join(i))