import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
dp = [-1] * 1000001

def topdown(n):
    a = n
    b = n
    c = n
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    
    if dp[n] != -1:
        return dp[n]
    
    if n % 3 == 0:
        a = topdown(n//3)
    
    if n % 2 == 0:
        b = topdown(n//2)
    
    c = topdown(n - 1)

    dp[n] = min(a,b,c) + 1

    return dp[n]
print(topdown(n))

