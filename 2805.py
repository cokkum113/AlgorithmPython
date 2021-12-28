import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

hi = max(tree)
lo = 1

while(hi >= lo):
    mid = (hi + lo) // 2
    total = 0

    for i in range(n):
        if(tree[i] > mid):
            x = tree[i] - mid
            total += x

    if total >= m :
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)