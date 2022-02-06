import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

ans = []
n = int(input())

#하노이, 위의것을 정답이 아닌곳으로,아래것을 정답인 곳으로
def hanoi(n, st, temp, end):
    if n == 1:
        ans.append([st, end])
        return
    hanoi(n - 1, st, end, temp)
    ans.append([st, end])
    hanoi(n - 1, temp,st,end)

hanoi(n, 1, 2, 3)
print(len(ans))
for i in ans:
    print(*i)