import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, B = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

def make_matrix(A, matrix):
    new_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp  = 0
            for k in range(N):
                tmp += matrix[i][k] * A[k][j]
            new_matrix[i][j] = tmp % 1000
    return new_matrix
# make_matrix(A, A)
# print(new_matrix)
# a, b랑 곱해서 나온 새로운 new_matrix

#이제 이걸 b만큼 하면되는 분할 정복하기
def recursion(A, B):
    if B == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] = A[i][j] % 1000
        return A
    
    #짝수, 제곱수로 계속 곱해주고
    elif B % 2 == 0:
        n = B // 2
        new_matrix2 = recursion(A, n)
        return make_matrix(new_matrix2, new_matrix2)
        
    #홀수, A를 마지막에 곱해주고
    elif B % 2 == 1:
        n = B - 1
        new_matrix2 = recursion(A, n)
        return make_matrix(A, new_matrix2)
        
res = recursion(A, B)

for i in range(N):
    for j in range(N):
        res[i][j] = res[i][j]
for i in res:
    print(*i, sep= ' ')