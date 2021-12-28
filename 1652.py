import sys
input = sys.stdin.readline

k, n = map(int, input().split())

x = []
for _ in range(k):
    line = int(input())
    x.append(line)

lo = 1
hi = max(x)

while(hi >= lo):
    mid = (hi + lo)//2
    ans = 0
    for i in x:
        ans += (i//mid)
    if ans >= n:
        lo = mid + 1
    else:
        hi = mid - 1 

print(hi)
