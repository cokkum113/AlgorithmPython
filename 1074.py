import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, r, c = map(int, input().split())
cnt = 0
def put_nums(x, y, n):
    global cnt
    if x == r and y == c:
        print(cnt)
        exit()
    if n == 1:
        cnt += 1
        return
    
    if not( x <= r < x + n and y <= c < y + n):
        cnt += n * n
        return
        
    nx = x + (n//2)
    ny = y + (n//2)
    
    put_nums(x, y, n//2)
    put_nums(x, ny, n//2)
    put_nums(nx, y, n//2)
    put_nums(nx, ny, n//2)

put_nums(0, 0, 2**n)
