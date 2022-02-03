import sys
input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

zero_cnt = 0
one_cnt = 0

def check(x, y, n):
    for i in range(n):
        for j in range(n):
            if graph[x][y] != graph[x + i][y + j]:
                return -1
    return graph[x][y]


anslist = []
def recursion(x, y, n):
    change = check(x, y, n)
    if change != -1:
        anslist.append(change)
        return
    
    nx = x + (n//2)
    ny = y + (n//2)

    recursion(x, ny, n//2)
    recursion(x, y, n//2)
    
    
    recursion(nx, ny, n//2)
    recursion(nx, y, n//2)

recursion(0, 0, n)
for i in anslist:
    if i == 0:
        zero_cnt += 1
    else:
        one_cnt += 1
print(zero_cnt)
print(one_cnt)





