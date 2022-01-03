import sys
input = sys.stdin.readline

n, m = map(int, input().split())
slist = []
mlist = []
for _ in range(n):
    s = input().rstrip()
    slist.append(s)

for _ in range(m):
    c = input().rstrip()
    mlist.append(c)

cnt = 0
for i in mlist:
    if i in slist:
        cnt += 1
print(cnt)