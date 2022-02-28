import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())

#BFS 로 풀어보기

def bfs(sp, dp):
    que = deque()
    que.append([sp, 0])
 
    while que:
        status = que.popleft()

        if status[0] == dp:
            return status[1] + 1  
             
        if status[0] * 2 <= dp :
            que.append([status[0] * 2, status[1] + 1])
   
        
        if int(str(status[0]) + '1') <= dp:
            que.append([int(str(status[0]) + '1'), status[1] + 1])
          
        
    return -1 
        
print(bfs(a, b))
