import sys
input =sys.stdin.readline

n, m = map(int, input().split())
T = []
for _ in range(n):
    t = int(input())
    T.append(t)


def test(k):
    total = 0 
    for t in T:
        total += (k // t)

    if total >= m:
        return True
    return False

lo = 1
hi = int(1e21)

ans = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if test(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(ans)
