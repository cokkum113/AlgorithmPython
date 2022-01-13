import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * n)

ans = 0
while True:
    ans += 1
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())

    # print(belt)
    # print(robot)
    
    if robot[n - 1] == 1:
        robot[n - 1] = 0
    for i in range(n - 2, -1, -1):
        if belt[i + 1] >= 1 and robot[i] == 1 and robot[i + 1] == 0:
            robot[i] = 0
            robot[i + 1] = 1
            belt[i + 1] -= 1
        else:
            continue
        
    if robot[n - 1] == 1:
        robot[n - 1] = 0

    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    
    if belt.count(0) >= k:
        break
print(ans)    