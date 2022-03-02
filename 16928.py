import sys
input = sys.stdin.readline
from collections import deque

'''
질문. 전에 푼 방식으로는 왜 안되는지, 반례가 뭐가 나오는지.
22퍼에서 계속 틀리는데 이유를 모르겠음
지금 코드랑 똑같은거같음
시간초과가 아닌 틀렸습니다 제출이 22퍼에서 틀린것.
'''
n, m = map(int, input().split())

bridge = [0] * 101

visit = [False] * 101

for _ in range(n):
    x, y = map(int, input().split())
    bridge[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    bridge[x] = y

def bfs(sp):
    ans = int(1e9)
    que = deque()
    que.append([sp, 0])
    visit[sp] = True
    while True:
        status = que.popleft()
        if status[0] == 100:
            ans = min(ans, status[1])
            return ans

        for i in range(1, 7):
            new_pos = status[0] + i

            if 100 < new_pos:
                continue
            if visit[new_pos]:
                continue
            visit[new_pos] = True

            if bridge[new_pos] != 0:
                new_pos = bridge[new_pos]
            que.append([new_pos, status[1] + 1])
                
print(bfs(1))