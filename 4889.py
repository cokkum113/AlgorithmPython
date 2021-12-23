import sys
input = sys.stdin.readline

ans = []
while True:
    cnt = 0
    s = input().rstrip()
    stack = []

    if '-' in s:
        break

    for i in s:
        if i == '{':
            stack.append('{')
        elif len(stack) == 0 and i == '}':
            cnt += 1
            stack.append('{')
        elif len(stack) != 0 and i == '}':
            stack.pop()
        
    
    cnt = len(stack)//2 + cnt

    ans.append(cnt)

for i in range(len(ans)):
    print("%d. %d" %(i+1, ans[i]))


