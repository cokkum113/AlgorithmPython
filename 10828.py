import sys
input = sys.stdin.readline

n = int(input())

stack = []
for i in range(n):
    string = input().split()
    
    if string[0] == 'push':
        
        stack.append(string[1])
        
    
    if string[0] == "pop":
        if(len(stack) == 0):
            print(-1)
            
        else:
            print(stack.pop())
            
        
    
    if string[0] == "size":
        print(len(stack))
        

    if string[0] == "empty":
        if(len(stack) == 0):
            print(1)
            
        else:
            print(0)
            
        

    if string[0] == "top":
        if(len(stack) == 0):
            print(-1)
            
        else:
            print(stack[-1])
            
        
