import sys
from types import resolve_bases
input = sys.stdin.readline

s = input().rstrip()



check = []
flag = 0
for i in s:
    if i == '(' or i == '[':
        check.append(i)
    elif i == ')':
        if len(check) != 0 and check[-1]  == '(':
            check.pop()
        else:
            flag = 1
    elif i == ']':
        if len(check) != 0 and check[-1]  == '[':
            check.pop()
        else:
            flag = 1



stack = []
for i in s:
    if i == '(':
        stack.append('(')
    elif i == '[':
        stack.append('[')
        
    elif i == ')' and len(stack) != 0:
        x = stack[-1]

        if x == '(':
            stack.pop()
            stack.append(2)
           
        else:
            a = 0
            for j in range(len(stack) - 1, -1, -1):
                if(stack[j] == '('):
                    stack[j] = a * 2
                    break
                else:
                    a += stack[j]
                    stack.pop()
                        
                        
    elif i == ']' and len(stack) != 0:
        x = stack[-1]

        if x == '[':
            stack.pop()
            stack.append(3)
           
        else:
            a = 0
            for j in range(len(stack) - 1, -1, -1):
                if(stack[j] == '['):
                    stack[j] = a * 3
                    break
                else:
                    a += stack[j]
                    stack.pop()
    
ans = 0
if flag == 0 and len(check) == 0:
    for i in range(len(stack)):
        if stack[i].isdigit == True:
            ans += stack[i]
        else:
            print(0)
            exit()
else:
    print(0)
