n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
for i in range(1,n):
    for j in range(len(graph[i])):
        if (j-1) < 0:
            left = 0
        else:
            left = graph[i-1][j-1]
        if j >= len(graph[i-1]):
            right = 0
        else:
            right = graph[i-1][j]
        graph[i][j] = graph[i][j] + max(left,right)
print(max(graph[n-1]))