import sys
input = sys.stdin.readline

nums = []

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = []

visit = [False] * (n+1)

def p(st):
    if st == m:
        print(*ans)
        return

    for i in range(1, n+ 1):
        if visit[i]:
            continue
        visit[i] = True
        ans.append(nums[i - 1])
        p(st + 1)
        ans.pop()
        visit[i] = False


p(0)
