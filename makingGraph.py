v = 6
graph1 =[[0 for _ in range(v+1)] for _ in range(v+1)]
edge = [[1, 5], [1, 2],[2, 3],[2, 5],[3, 4],[4, 6]]

for start, end in edge:
    graph1[start][end] = 1
    graph1[end][start] = 1

print(graph1)


graph2 = [[] for _ in range(7)]

for start, end in edge:
    graph2[start].append(end)
    graph2[end].append(start)

print(graph2)


