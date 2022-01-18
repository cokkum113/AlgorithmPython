from cProfile import label
import sys

input = sys.stdin.readline

trees = {}
tree_cnt = 0

while True:
    tree = input().rstrip()
    if tree == '':
        break
    
    if tree in trees:
        trees[tree] += 1
        tree_cnt += 1
    else:
        trees[tree] = 1
        tree_cnt += 1
ans = []
for i in trees:
    # i = i[:-1]
    ans.append(i)
ans.sort()

res = []
for i in ans:
    j = i
    # i = i + '\n'
    x = trees[i]
    print(j, "%.4f" %(x*100/tree_cnt))