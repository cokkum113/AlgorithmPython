import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

lo = 0
hi = 0

maximum = 0
cnt =  0
cntlist = [0] * 100001
anslist = []
while hi < n:
    #whlie True: if hi == n-1을하면 한번더 안돌고 hi < n을 하면 한번 더 도는데 n - 1일 때도 돌아야함

    if (cntlist[nums[hi]] + 1) <= k:
        cntlist[nums[hi]] += 1
        hi += 1
        
        
    else:
        cntlist[nums[lo]] -= 1
        lo += 1
        
    # print("dfsdfsdfsdfsdfsdfsdfsdf")
    cnt = hi - lo
    # anslist.append(cnt)
    # print(anslist)
    if cnt > maximum:
        maximum = cnt
    
print(maximum)