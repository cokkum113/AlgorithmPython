import sys
input = sys.stdin.readline

x, y = map(int, input().split())

if x == y :
    print(-1)
    exit()

z = (y * 100)//x

if z>= 99:
    print(-1)
    exit()

lo = 1
hi = 1000000000

cnt = 0
while(hi >= lo):
    mid = (hi + lo) // 2
    nz = (y + mid) * 100 // (x + mid) 

    if nz > z:
        hi = mid - 1
        cnt = mid
    
    else:
        lo = mid + 1

print(cnt)