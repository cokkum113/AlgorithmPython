import sys; input = sys.stdin.readline
numList = []
n = int(input())
numList = list(map(int, input().split()))



minimum = 1000001
maximum = -1000001

for i in range(len(numList)):
    if(numList[i] > maximum):
        maximum = numList[i]
    if(numList[i] < minimum):
        minimum = numList[i]

print(minimum, maximum)