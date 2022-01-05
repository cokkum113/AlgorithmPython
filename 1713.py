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
        if len(frame[i]) == 0:
            check = 1
    if check == 1:
        return False
    elif check == 0:
        return True


for i in range(s):
    mini = 0
    minsave = []
    ordersave = [] 
    changeIndex = 0
    changevalue = 0
    ordercheck = 0
    aaa = 0
    wantchange = 0
    if fullframe(frame) == False and emptyframe(frame) == False:
        for j in range(len(frame)):
            if len(frame[j]) != 0 and frame[j][0] == nums[i]:
                frame[j] = [nums[i], frame[j][1] + 1, frame[j][2]]
                break
            elif len(frame[j]) == 0 and sum(frame[j]) == 0:
                frame[j] = [nums[i], 1, i]
                break 

    elif emptyframe(frame):
        frame[i] = [nums[i], 1, i]
        
    elif fullframe(frame):
        for p in range(len(frame)):
            cntvalue = frame[p][1]
            minsave.append(cntvalue)
        changevalue = min(minsave)

        for x in range(len(frame)):
            ordercheck = frame[x][2]
            ordersave.append(ordercheck)
        wantchange = min(ordersave)
#################################################
        for t in range(len(frame)):
            if frame[t][1] == changevalue and frame[t][2] == wantchange:
                changeIndex = t
                break
              
        ############################################
        numlist = []  
        for r in range(len(frame)):
            if frame[r][0] == nums[i]:
                numlist.append(r)
        

        for j in range(len(frame)):
            if frame[j][0] != nums[i]:
                frame[changeIndex] = [nums[i], 1, i]
                break
            
            frame[numlist[0]] = [nums[i], frame[numlist[0]][1] + 1, frame[numlist[0]][2]]
            break
       



anslist = []
for i in range(len(frame)):
    if len(frame[i]) != 0:
        ans = frame[i][0]
        anslist.append(ans)
anslist.sort()
print(*anslist)




