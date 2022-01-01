import sys
input = sys.stdin.readline

n, c = map(int, input().split())

home = []
for i in range(n):
    h = int(input())
    home.append(h)

home.sort()

lo = 0
hi = home[-1]


def possible(value):
    prev = home[0]
    cnt = 1
    for i in home:
        if prev + value <= i:
            prev = i
            cnt += 1

    if cnt >= c:
        return True
    return False

while(hi >= lo):
    mid = (hi + lo) // 2
    if possible(mid):
        lo = mid + 1
        ans = mid
    else:
        hi = mid - 1
        
        
print(ans)