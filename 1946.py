import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    compare = []
    cnt = 1
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        a = [x,y]
        compare.append(a)

    compare.sort()
    compared = compare[0][1]

    for i in range(1, n):
        if compared > compare[i][1]:
            compared = compare[i][1]
            cnt += 1
    print(cnt)
