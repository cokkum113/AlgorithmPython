import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]
nums = [0] * ((n**2) + 1)
incnt = [] #들어오는 순서를 기억하고 있는 리스트 
for i in range(n**2):
    s = list(map(int, input().split()))
    incnt.append(s[0])
    nums[s[0]] = s[1:]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# if n%2 == 0:
#     graph[n//2 - 1][n//2 -1] = incnt[0]
# else:
#     graph[n//2][n//2] = incnt[0]

# 이 가정이 아예 틀렸음.
#첫시작을 중앙이라고 생각한게 착각이었음
#(1,1)에 처음 시작이 와야함!

# graph[1][1] = incnt[0] ------> 얘 때문에 계속 틀렸었음.....
#초기화하면안됨

ans = []
for t in incnt: 
    findx = 0
    findy = 0
    likecntmax = -1
    zerocntmax = -1
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                likecnt = 0
                zerocnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] in nums[t]:
                            likecnt += 1
                        if graph[nx][ny] == 0:
                            zerocnt += 1
                if (likecntmax == likecnt and zerocnt > zerocntmax) or (likecnt > likecntmax):
                    likecntmax = likecnt
                    zerocntmax = zerocnt
                    findx = i
                    findy = j
    graph[findx][findy] = t

ans = 0
for i in range(n):
    for j in range(n):
        anscnt = 0
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in nums[graph[i][j]]:
                    anscnt += 1
        
        if anscnt == 1:
            ans += 1
        elif anscnt == 2:
            ans += 10
        elif anscnt == 3:
            ans += 100
        elif anscnt == 4:
            ans += 1000

print(ans)