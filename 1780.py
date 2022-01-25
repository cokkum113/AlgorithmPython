import sys
input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

def check(x, y, n):
    for i in range(n):
        for j in range(n):
            if graph[x][y] != graph[x + i][y + j]:
                return -2
    return 2

m1cnt = 0
zerocnt = 0
p1cnt = 0

def cnt_paper(x, y, n):
    global m1cnt, zerocnt, p1cnt
    ans = check(x, y, n)
    if ans == -2:
        for i in range(0, 3):
            for j in range(0, 3):
                cnt_paper(x + i * n // 3, y + j * n // 3, n // 3)
    else:
        if graph[x][y] == -1:
            m1cnt += 1
        elif graph[x][y] == 0:
            zerocnt += 1
        elif graph[x][y] == 1:
            p1cnt += 1

cnt_paper(0, 0, n)
print(m1cnt, zerocnt, p1cnt, sep='\n')
        