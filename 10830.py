import sys
input = sys.stdin.readline

n, b = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

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

# def matrix(x, y, n):
#     if n == 1:
#         return
    
    
    