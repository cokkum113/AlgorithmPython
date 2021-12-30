import sys
input = sys.stdin.readline

n, c = map(int, input().split())

home = []
for i in range(n):
    h = int(input())
    home.append(h)

home.sort()

lo = 1
hi = home[-1] - home[0]

offset = 0
cnt = 0
ans = 0
while(hi >= lo):
    mid = (lo + hi) // 2
    for i in range(len(home)):
        if offset <= home[i]:
            offset = home[i] + mid
            cnt += 1
        
    if cnt >= c:
        lo = mid + 1
        ans = mid

    else:
        hi = mid - 1

print(ans)