import sys
input = sys.stdin.readline

s = input().rstrip()


def check(s):
    stack = []
    flag = 0
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1]  == '(':
                stack.pop()
            else:
                flag = 1
        elif i == ']':
            if len(stack) != 0 and stack[-1]  == '[':
                stack.pop()
            else:
                flag = 1
    
    if len(stack) == 0 and flag == 0:
        return True
    else:
        return False

def fun(s):   
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
    return sum(stack)

if check(s):
    print(fun(s))
else:
    print(0)