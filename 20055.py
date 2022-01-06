import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
convey = deque(list(map(int,input().split())))
robot = deque([0 for _ in range(n)])

cnt = 0
ans = 0
while True:
    ans += 1

    x = convey.pop()
    convey.appendleft(x)
    y = robot.pop()
    robot.appendleft(y)

    robot[n - 1] = 0
    #n-1이 로봇이 내려가는 자리 

    # print(robot)
    if sum(robot) != 0:
        for i in range(n - 2, -1, -1):
            if robot[i] == 1 and robot[i + 1] == 0 and convey[i + 1] >= 1:
                convey[i + 1] -= 1
                robot[i] = 0
                robot[i + 1] = 1
            else:
                continue
        
        robot[n - 1] = 0
        

        
    if robot[0] == 0 and convey[0] >= 1:
        robot[0] = 1
        convey[0] -= 1
    
    cnt = convey.count(0)
    # print(convey)
    # print(robot)
    
    if cnt >= k:
        break
    

print(ans)

