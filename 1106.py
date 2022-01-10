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

#값을 저장해두고 그 개수가 빌때마다 원래 값을 더해주면 되나?
#dp에 최대값부터 저장하고 모자르면 가져오고
#그런식으로
for i in range(n - 1):
