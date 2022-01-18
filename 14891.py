import sys
input = sys.stdin.readline
from collections import deque

a1 = input().rstrip()
a2 = input().rstrip()
a3 = input().rstrip()
a4 = input().rstrip()

t1 = deque([i for i in a1])
t2 = deque([i for i in a2])
t3 = deque([i for i in a3])
t4 = deque([i for i in a4])

def rotation(dir, ch):
    if dir == 1:
        ch.appendleft(ch.pop())
    elif dir == -1:
        ch.append(ch.popleft())

r = int(input())
for i in range(r):
    t, dir = map(int, input().split())
    
    if t == 1:
        ch = t1
        x = ch[2]
        y = t2[6]
        x2 = t2[2]
        y2 = t3[6]
        x3 = t3[2]
        y3 = t4[6]
        rotation(dir, ch)
        if x != y:
            rotation(-dir, t2)
            if x2 != y2:
                rotation(dir, t3)
                if x3 != y3:
                    rotation(-dir, t4)
        # elif x == y:
        #     continue
    
    elif t == 2:
        ch = t2
        right = ch[2]
        right2 = t3[6]
        left = ch[6]
        left2 = t1[2]
        tr3 = t3[2]
        tl4 = t4[6]
        rotation(dir, ch)
        if right != right2:
            rotation(-dir, t3)
            if tr3 != tl4:
                rotation(dir, t4)
        if left != left2:
            rotation(-dir, t1)
    
    elif t == 3:
        ch = t3
        rrrr = ch[2]
        r2 = t4[6]
        l = ch[6]
        l2 = t2[2]
        tl2 = t2[6]
        tr1 = t1[2]
        rotation(dir, ch)
        if rrrr != r2:
            rotation(-dir, t4)
            
        if l != l2:
            rotation(-dir, t2)
            if tl2 != tr1:
                rotation(dir, t1)
    
    elif t == 4:
        ch = t4
        ll = ch[6]
        ll2 = t3[2]
        t3l = t3[6]
        t2r = t2[2]

        t2l = t2[6]
        t1r = t1[2]
        rotation(dir, ch)
        if ll != ll2:
            rotation(-dir, t3)
            if t3l != t2r:
                rotation(dir, t2)
                if t2l != t1r:
                    rotation(-dir, t1)
        # else:
        #     continue

# print(t3)
ans = 0
if t1[0] == '1':
    ans +=1
if t2[0] == '1':
    ans += 2
if t3[0] == '1':
    ans += 4
if t4[0] == '1':
    ans += 8
print(ans)