import sys
input = sys.stdin.readline

n, k = map(int, input().split())

list1 = []

for i in range(n):
    list1.append(i + 1)

pointer = 0

ansList = []
for _ in range(n):  
    pointer += k - 1

    if(pointer >= n):
        pointer = pointer % n
             
    ansList.append(str(list1[pointer]))
    list1.pop(pointer)
    n -= 1

print("<", end='')
print(", ".join(ansList),">", sep="")
