import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    stack = []
    compare = []
    s = input().rstrip()
    flag = 0
    
    for i in range(len(s)):
        stack.append(s[i])
    
    for j in range(len(stack)):
        if(stack[j] == '('):
            compare.append('(')
            
        elif(stack[j] == ')'):
            if len(compare) > 0:
                compare.pop()
                
            else:
                print("NO")
                flag = 1
                break
          
    if (flag == 0) and len(compare) == 0 :
        print("YES")
    elif (flag == 0) and len(compare) != 0:
        print("NO") 


