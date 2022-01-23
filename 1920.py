import sys
input = sys.stdin.readline
n = int(input())
l = list(input().split())
m = int(input())

l2 = list(input().split())

dic = {num : True for num in l}

for t in l2:
    if t in dic:
        print(1)
    else:
        print(0)