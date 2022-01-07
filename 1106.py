import sys
input = sys.stdin.readline

c, n = map(int, input().split())
#c명이 될때까지 도는 것 c명이 되거나 넘는 순간 바로 break

cntlist = []

for i in range(n):
    m, p = map(int, input().split())
    cntlist.append([m,p])

cntlist = sorted(cntlist, key = lambda x : x[1])
cntlist.reverse()

dp = []
#값을 저장

# 값들을 추가하는 식.
# 사람수 많은 수대로
person = 0
money = 0
remain = 0
for i in range(n - 1):
    person  = c//cntlist[i][1]
    money = person * cntlist[i][0]

    remain = c - (cntlist[i][1] * person)
    for j in range(1, n):
        if c >= (person * cntlist[i][1] + remain):
            print(person * cntlist[i][1] + remain)
            break