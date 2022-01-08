import sys
input = sys.stdin.readline

n = int(input())

tree = {}
for _ in range(n):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right]

def preorder(start):
    print(start, end='')
    if tree[start][0] != '.':
        preorder(tree[start][0])
    if tree[start][1] != '.':
        preorder(tree[start][1])

def inorder(start):
    if tree[start][0] != '.':
        inorder(tree[start][0])
    print(start, end='')
    if tree[start][1] != '.':
        inorder(tree[start][1])

def postorder(start):
    if tree[start][0] != '.':
        postorder(tree[start][0])
    if tree[start][1] != '.':
        postorder(tree[start][1])
    print(start, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
