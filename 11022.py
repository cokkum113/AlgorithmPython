import sys

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    ans = x + y
    print("Case #%d: %d + %d = %d"  %(i+1, x, y, ans))