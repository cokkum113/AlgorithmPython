import sys
input = sys.stdin.readline

n, m = map(int, input().split())

visit = [False] * n

ans = []
def p(st):
    if st == m:
        print(*ans)
        return
    
    for i in range(n):
        if visit[i]:
            continue
        
        ans.append(i + 1)
        
        p(st + 1)
        visit[i] = True
        ans.pop()
        for j in range(i + 1, n):
            visit[j] = False

p(0)