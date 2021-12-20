from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
numlist = []

ansList = []


s = input().rstrip()

for _ in range(n):
    x = int(input())
    numlist.append(x)

for i in s:
    if ('A' <= i <= 'Z'):
        x = ord(i) - ord('A')
        real = numlist[x]
        ansList.append(real)
    
    else:
        num2 = ansList.pop()
        num1 = ansList.pop()

        if i == '+':
            a = num1 + num2
            ansList.append(a)
            
        elif i == '-':
            a = num1 - num2
            ansList.append(a)
            
        elif i == '*':
            a = num1 * num2
            ansList.append(a)
            
        elif i == '/':
            a = num1 / num2
            ansList.append(a)
  

print("%.2f" %(ansList[0]))
        