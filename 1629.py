import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

#pow는 솔루션을 봐서 알았고 내가 생각했던 방식
#B를 계속 -1 씩 해주면 된다고 생각을 했음 -> 아님

def recursion(A, B):
    if B == 1:
        return A % C

    temp = recursion(A, B//2)

    #짝수일때는 temp * temp
    if B % 2 == 0:
        return temp * temp % C
    
    else:
        return temp * temp * A % C

print(recursion(A,B))
    