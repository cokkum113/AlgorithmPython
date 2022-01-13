import sys
input = sys.stdin.readline

n = int(input())
s = int(input())
nums = list(map(int, input().split()))

frame = []
# frame.append([nums[0], 1, 0])

#선체크해야함
def inside_same_check(x):
    for i in frame:
        if x == i[0]:
            return True
    return False

# def push_fullframe(x):
#     if inside_same_check:
#         for i in range(len(frame)):
#             if x == frame[i][0]:
#                 frame[i] = [x, frame[i][1] + 1, frame[i][2]]
#     else:
#         for i in range(len(nums)):
#             frame[0] = [x, 1, i]

# def push_frame(x):
#     if inside_same_check:
#         for i in range(len(frame)):
#             if x == frame[i][0]:
#                 frame[i] = [x, frame[i][1] + 1, frame[i][2]]
#     else:
#         for i in range(len(nums)):
#             frame.append([x, 1, i])

for index, value in enumerate(nums):
    frame.sort(key=lambda x : (x[1], x[2]))
    if inside_same_check(value):
        for i in range(len(frame)):
            if frame[i][0] == value:
                frame[i][1] += 1
                break
    else:
        if len(frame) < n:
            frame.append([value, 1, index])
        elif len(frame) == n:
            frame[0] = [value, 1, index]
    
    
    # print(frame)  
ans = []
for i in range(len(frame)):
    ans.append(frame[i][0])
ans.sort()
print(*ans)
