import sys
input = sys.stdin.readline

n = int(input())
s = int(input())

nums = list(map(int, input().split()))

frame = []


def checkinside(frame, recommend):
    for i in frame:
        if i[0] == recommend:
            return True
    return False

for index, recommendman in enumerate(nums):
    if checkinside(frame, recommendman):
        for i, j in enumerate(frame):
            if j[0] == recommendman:
                frame[i][1] += 1
                break

    
    else:
        if len(frame) < n:
            frame.append([recommendman, 1, index])
        elif len(frame) == n:
            frame[0] = [recommendman, 1, index]
    
    frame.sort(key=lambda x: (x[1], x[2]))


anslist = []
for i in range(len(frame)):
    if len(frame[i]) != 0:
        ans = frame[i][0]
        anslist.append(ans)
anslist.sort()
print(*anslist)


 