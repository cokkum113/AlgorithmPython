import sys
input = sys.stdin.readline

n = int(input())
clist = list(map(int, input().split()))

clist.sort()
ans = []
mini = 1000000001

lo = 0
hi = n - 1
a = clist[lo] + clist[hi]

while hi > lo:
    if abs(a) < mini:
        mini = abs(a)
        ans.append([clist[lo], clist[hi]])

    if a == 0:
        ans.append([clist[lo], clist[hi]])
        break

    elif a > 0:
        hi -= 1
        a = clist[lo] + clist[hi]

    elif a < 0:
        lo += 1
        a = clist[lo] + clist[hi]

print(ans[-1][0], ans[-1][1])