import sys
input = sys.stdin.readline

n, c = map(int, input().split())

home = []
for i in range(n):
    h = int(input())
    home.append(h)

home.sort()

offset = 0
offlist = []
for i in range(1, n):
    offset = home[i] - home[i - 1]
    offlist.append(offset)

maxi = 0
for i in range(1, n - 1):
    a = offlist[i] - offlist[i - 1]
    maxi = max(a, maxi)

print(maxi)