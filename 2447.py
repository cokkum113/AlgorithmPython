import sys
input = sys.stdin.readline

n = int(input())


def make_star(n):
    if n == 3:
        return ['***', '* *', '***']
    board = []
    make_board = make_star(n // 3)
    #이전 별모양

    one_three = []
    for i in range(n//3):
        x = make_board[i] * 3
        one_three.append(x)
    
    two = []
    for i in range(n//3):
        x = make_board[i] + ' ' * (n // 3) + make_board[i]
        two.append(x)
    
    return one_three + two + one_three

ans = make_star(n)
print('\n'.join(ans))
    




     
            