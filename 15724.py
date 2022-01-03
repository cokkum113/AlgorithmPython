import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(n):
    s = list(map(int, input().split()))
    graph[i] = s

t = int(input())
    
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + graph[i - 1][j - 1]

for i in range(t):
    sx, sy, ex, ey = map(int, input().split())
    print(dp[ex][ey] - dp[sx -1][ey] - dp[ex][sy - 1] + dp[sx - 1][sy - 1])
