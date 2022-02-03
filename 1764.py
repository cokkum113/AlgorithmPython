import sys
input = sys.stdin.readline

n, m= map(int, input().split())

l1 = []
l2 = []

for i in range(n):
    l1.append(input().rstrip())

for i in range(m):
    l2.append(input().rstrip())


l1 = set(l1)
l2 = set(l2)
ans = set()

ans = l1 & l2

ans = sorted(ans)
print(len(ans))
for i in ans:
    print(i)

