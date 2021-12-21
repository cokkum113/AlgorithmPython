import sys
input = sys.stdin.readline

s = input()

lineCnt = 0
cutCnt = 0
stack2 = []

for i in range(len(s)):
    if s[i] == '(':
        stack2.append('(')

    elif(s[i] == ')'):
        if(s[i - 1] == '('):
            stack2.pop()
            lineCnt += len(stack2)
            cutCnt += 1
        elif(s[i - 1] == ')'):
            lineCnt += 1
            stack2.pop()
print(lineCnt)