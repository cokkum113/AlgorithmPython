import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []

#입력이 몇개 들어오는지 모를때 사용하는 방법!
cnt = 0
while cnt < 10001:
    try:
        x = int(input())
        arr.append(x)
    except:
        break
    cnt += 1

#50 /////30 24 5 28 45 //////   98 52 60

# 5 28 24 45 30 60 52 98 50 

root = arr[0]
def postorder(st, end):
    if st > end:
        return

    root = arr[st]
    index = st + 1

    while index <= end:
        if arr[index] > root:
            break
        index += 1
    
    postorder(st + 1, index - 1) #l
    postorder(index, end) #r
    print(root) #v

postorder(0, len(arr) - 1)



    

    
