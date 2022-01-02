import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
dp = [-1] * 10001

def topdown(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    if dp[n] != -1:
        return dp[n] 

    dp[n] = topdown(n - 1) + topdown(n - 2)
    return dp[n]

print(topdown(n)%10007)





    

    

