import sys
input = sys.stdin.readline

n, m = map(int, input().split())

#1 : ->
d1x = [1]
d1y = [0]
#2 :  <- -> 
d2x = [-1, 1]
d2y = [0, 0]
#3 : 위 오른쪽
d3x = [0, 1]
d3y = [-1, 0]
#4 : 왼 상 우
d4x = [-1, 0, 1]
d4y = [0, -1, 0]
#5 : 상 하 좌 우
d5x = [1, -1, 0, 0]
d5y = [0, 0, 1, -1]

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

