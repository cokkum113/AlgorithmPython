import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

order = [0] * (n + 1)
for i in range(n):
    index = 0
    for j in range(1, n+ 1):
        if nums[i] == index and order[j] == 0:
            order[j] = i + 1
            break
        elif order[j] == 0:
            index += 1

order = order[1:]
print(*order)