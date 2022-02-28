import sys
input = sys.stdin.readline

n = int(input())

primelist = []

def find_prime():
    nums = [True] * 4000000
    sqr = int(4000000 ** 0.5)
    for i in range(2, sqr + 1):
        if nums[i] == True:
            for j in range(i + i, 4000000, i):
                nums[j] = False
    
    for i in range(2, len(nums)):
        if nums[i]:
            primelist.append(i)
find_prime()

lw = 0
hi = 0

total = primelist[0]
cnt = 0

while(True):
    if hi == len(primelist) - 1 and total < n:
        break
    if total > n:
        total -= primelist[lw]
        lw += 1
    
    elif total < n:
        hi += 1
        total += primelist[hi]
    
    elif total == n:
        total -= primelist[lw]
        lw += 1
        cnt += 1

print(cnt)