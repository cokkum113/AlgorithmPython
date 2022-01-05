import sys
input = sys.stdin.readline

f = int(input())
s = int(input())
nums = list(map(int, input().split()))

frame = [[] for _ in range(f)]

def emptyframe(frame):
    total = 0
    for i in range(len(frame)):
        x =  sum(frame[i])
        total += x
    if total == 0:
        return True
    else:
        return False

def fullframe(frame):
    check = 0
    for i in range(len(frame)):
        if 0 in frame[i] or len(frame[i]) == 0:
            check = 1
    if check == 1:
        return False
    elif check == 0:
        return True


order = 0

for i in range(s):
    mini = 10001
    minsave = []
    ordersave = [] 
    order += 1
    changeIndex = 0
    changevalue = 0
    if fullframe(frame) == False and emptyframe(frame) == False:
        for j in range(len(frame)):
            if len(frame[j]) != 0 and frame[j][0] == nums[i]:
                frame[j] = [nums[i], frame[j][1] + 1, order]
                break
            elif len(frame[j]) == 0 or sum(frame[j]) == 0:
                frame[j] = [nums[i], 1, order]
                break

    elif emptyframe(frame):
        frame[0] = [nums[i], 1, order]

    elif fullframe(frame):
        # print(frame)
        for j in range(len(frame)):
            if frame[j][0] == nums[i]:
                frame[j] = [nums[i], frame[j][1] + 1, order]
                break
                               
            elif frame[j][0] != nums[i]:
                for p in range(len(frame)):
                    cntvalue = frame[p][1]
                    minsave.append(cntvalue)
                    changevalue = min(minsave)
                    
                
                for t in range(len(frame)):
                    if frame[t][1] == changevalue:
                        if frame[t][2] <= mini:
                            mini = frame[t][2]
                
                for u in range(len(frame)):
                    if frame[u][2] == mini:
                        if frame[u][1] == changevalue:
                            changeIndex = u
                            

                frame[changeIndex] = [nums[i], 1, order]
                break
        

anslist = []
for i in range(len(frame)):
    if len(frame[i]) != 0:
        ans = frame[i][0]
        anslist.append(ans)
anslist.sort()
print(*anslist)