import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())

tree = [-1] * 100001
heap_size = 0

def push(x):
    global tree
    global heap_size
    heap_size += 1
    tree[heap_size] = x
    parent = heap_size // 2
    child = heap_size

    while(child > 1) and tree[parent] > tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]
        child = parent
        parent = child //2

def pop():
    global tree
    global heap_size
    res = tree[1]
    tree[1] = tree[heap_size]
    tree[heap_size] = 0
    heap_size -= 1
    parent = 1
    child = 2

    if child + 1 < heap_size and tree[child] > tree[child + 1]:
        child = child + 1
    while child <= heap_size and tree[parent] > tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]
        parent = child
        child = parent * 2
        if child + 1 < heap_size and tree[child] > tree[child + 1]:
            child = child + 1
    return res

for i in range(n):
    x = int(input())
    if x == 0:
        if heap_size > 0:
            ans = pop()
            print(ans)
        else:
            print(0)
    else:
        push(x)