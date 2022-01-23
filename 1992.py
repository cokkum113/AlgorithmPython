import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    s = input().rstrip()
    arr.append(list(s))

anslist = []
def check(x, y, n):
    for i in range(n):
        for j in range(n):
            if arr[x][y] != arr[x + i][y + j]:
                return -1
    
    return arr[x][y]

def quad_tree(x, y, n):
    ans = check(x, y, n)
    if ans != -1:
        anslist.append(ans)
        return
    
    # nx = x + (n//2)
    # ny = y + (n//2)
    # anslist.append('(')
    # quad_tree(x, y, n//2)
    # quad_tree(x, ny, n//2)
    # quad_tree(nx, y, n//2)
    # quad_tree(nx, ny, n//2)
    # anslist.append(')')

    anslist.append('(')
    for i in range(0, 2):
        for j in range(0, 2):
            quad_tree(x + i * n //2 , y + j * n//2, n//2)
    anslist.append(')')

quad_tree(0, 0, n)
print(*anslist, sep='')
