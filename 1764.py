import sys
input = sys.stdin.readline

n, m= map(int, input().split())

l1 = []
l2 = []

for i in range(n):
    l1.append(input().rstrip())
for i in range(m):
    l2.append(input().rstrip())


ans = []
cnt = 0
for i in l1:
    if i in l2:
        cnt +=1
        ans.append(i)

ans.sort()
print(cnt)
for i in ans:
    print(i)

    


