import sys
input = sys.stdin.readline

x, y = map(int, input().split())

cnt = 1
while True:
    if x == y :
        break
    elif x > y :
        cnt = -1
        break
    # elif int(str(x) + '1') < y:
    #     cnt += 1
    #     y = y // 10 
    elif y % 10 == 1:
        y = y // 10
        cnt += 1
    elif y % 2 == 0:
        y = y // 2
        cnt += 1
    else:
        cnt = -1
        break
    
print(cnt)


