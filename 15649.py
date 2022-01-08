import sys
input = sys.stdin.readline

n,m = map(int, input().split())

visit = [False] * (n + 1)

ans = []

def p(st):
    if st == m:
        print(*ans)
        return

    for i in range(n):
        if visit[i] == True:
            continue
        visit[i] = True
        ans.append(i + 1)
        p(st + 1)
        ans.pop()
        visit[i] = False
    
p(0)
#1부터 넣으면 바로 끝나버림 if문에서 
