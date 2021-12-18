import sys
input = sys.stdin.readline

t = int(input())
scoreList = []
for i in range(t):
    StudentList = list(input().split())
    scoreList.append(StudentList)

scoreList = sorted(scoreList, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# for j in range(1, t):
#     if(int(scoreList[j - 1][1]) == int(scoreList[j][1])):
#         if(int(scoreList[j - 1][2]) > int(scoreList[j][2])) :
#             scoreList[j], scoreList[j - 1] = scoreList[j -1], scoreList[j]
        

# for j in range(1, t):
#     if((int(scoreList[j - 1][1]) == int(scoreList[j][1])) and (int(scoreList[j -1][2]) == int(scoreList[j][2]))):
#         if(int(scoreList[j - 1][3]) < int(scoreList[j][3])):
#             scoreList[j], scoreList[j - 1] = scoreList[j -1], scoreList[j]

# for j in range(1, t):
#     if((int(scoreList[j - 1][1]) == int(scoreList[j][1])) and (int(scoreList[j -1][2]) == int(scoreList[j][2])) and (int(scoreList[j - 1][3]) == int(scoreList[j][3]))):
#         if(scoreList[j - 1][0] > scoreList[j][0]):
#             scoreList[j], scoreList[j - 1] = scoreList[j -1], scoreList[j]

for i in range(t):
    print(scoreList[i][0])