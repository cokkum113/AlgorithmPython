import sys
input = sys.stdin.readline

n,m = map(int, input().split())

visit = [False] * n

ans = []
def p(st):
    if st == m:
        print(*ans)
        return
    
    for i in range(n):
        if visit[i]:
            continue
        visit[i] = True
        ans.append(i + 1)
        p(st + 1)
        ans.pop()
        # visit[i] = False
        for j in range(i + 1, n):
            visit[j] = False

p(0)
