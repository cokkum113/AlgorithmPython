import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

k = int(input())

inputlist = list(map(int, input().split()))

tree = [[] for _ in range(k)]

# root = len(inputlist)//2

def inorder(inputlist, index):
    root = len(inputlist)//2
    tree[index].append(inputlist[root])

    if len(inputlist) == 1:
        return

    inorder(inputlist[:root], index + 1)
    inorder(inputlist[root+1:], index + 1)

inorder(inputlist, 0)
for i in tree:
    print(*i)
