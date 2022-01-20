import sys
input = sys.stdin.readline

n, m, k = map(int,input().split())
dp = [[0] * m for _ in range(n)]

if k == 0:
    for i in range(n):
        for j in range(m):
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[n - 1][m - 1])

else:
    nx = (k - 1) // m
    ny = (k - 1) % m

    for i in range(nx + 1):
        for j in range(ny + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    for i in range(nx, n):
        for j in range(ny, m):
            if i == nx and j == ny:
                continue
            if i == nx:
                dp[i][j] = 1
            elif j == ny:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(dp[nx][ny] * dp[n - 1][m - 1]) 


