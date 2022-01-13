import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]

nums = [0] * (n**2 + 1)

comelist = []

t = n**2
for i in range(t):
    s = list(map(int, input().split()))
    comelist.append(s[0])
    nums[s[0]] = s[1:]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = []
for x in comelist:
    fx = 0
    fy = 0
    likemax = -1
    zeromax = -1
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                likecnt = 0
                zerocnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]

                    if 0 <= nx < n and 0<= ny < n:
                        if graph[nx][ny] in nums[x]:
                            likecnt += 1
                        if graph[nx][ny] == 0:
                            zerocnt += 1
                if (likecnt == likemax and zerocnt > zeromax) or likecnt > likemax :
                    likemax = likecnt
                    zeromax = zerocnt
                    fx = i
                    fy = j
    
    graph[fx][fy] = x

ansbox = [0,1,10,100,1000]
total = 0
for i in range(n):
    for j in range(n):
        anscnt = 0
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in nums[graph[i][j]]:
                    anscnt += 1
        
            
        total += ansbox[anscnt]
print(total)
