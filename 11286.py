import sys
input = sys.stdin.readline
import heapq

n = int(input())

tree = []
for i in range(n):
    x = int(input())

    if x == 0:
        if len(tree) == 0:
            print(0)
        elif len(tree) > 0:
            print(heapq.heappop(tree)[1])
    
    else:
        heapq.heappush(tree, [abs(-x),x])

