import sys
input = sys.stdin.readline

while(True):
    stack1 = []

    flag = 0
    s = input().rstrip()
    if s == '.':
        break
    for i in s:
        if i == '(':
            stack1.append('(')
        elif i == ')':
            if(len(stack1) == 0):
                flag = 1
                break
            elif(stack1[-1] == '['):
                flag = 1
                break
            else:
                stack1.pop()
        
        if i == '[':
            stack1.append('[')
        elif i == ']':
            if(len(stack1) == 0):
                flag = 1
                break
            elif(stack1[-1] == '('):
                flag = 1
                break
            
            else:
                stack1.pop()

    if (len(stack1) == 0 and flag == 0):
        print("yes")
    else:
        print("no")
