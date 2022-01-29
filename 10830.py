import sys
input = sys.stdin.readline

n, b = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a2 = a.copy()

ans = []
if b == 1:
    for i in range(n):
        r = []
        for j in a[i]:
            x = j % 1000
            r.append(x)
        ans.append(r)
    for i in ans:
        print(*i)
    exit()
new_matrix = [[-1] * n for _ in range(n)]
N = n
def matrix(x, y, N):
    if n == 1:
        return
    nx = x + N // n
    ny = y + N // n

    matrix(x, y, N//n)
    matrix(x, ny, N // n)
    matrix(nx, y, N // n)
    matrix(nx, ny, N // n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[k] += a[i] * a2[j]
tmp = 0
for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += a[i][k] * a2[k][j]
            new_matrix[i][j] = tmp
print(new_matrix)


    
    
    
    