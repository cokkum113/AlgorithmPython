import sys
input = sys.stdin.readline

n = int(input())
room = []
for _ in range(n):
    s, e = map(int, input().split())
    a = [s, e]
    room.append(a)


room.sort(key=lambda x : (x[1],x[0]))
cnt = 1
end = room[0][1]
for i in range(1,n):
    if room[i][0] >= end:
        end = room[i][1]
        cnt += 1
    else:
        continue
print(cnt)