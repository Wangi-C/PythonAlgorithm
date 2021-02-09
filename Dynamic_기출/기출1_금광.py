INF = int(1e9)
n,m = map(int,input().split())
num = list(map(int,input().split()))
graph = []
index = 0
for j in range(n):
    graph.append(num[index:index+m])
    index += m
for i in range(n):
    for j in range(1,m):
        if (i-1) < 0:
            left_up = 0
        else:
            left_up = graph[i-1][j-1]
        if (i+1) >= n:
            left_down = 0
        else:
            left_down = graph[i+1][j-1]
        left = graph[i][j-1]
        graph[i][j] = max(left_down,left,left_up) + graph[i][j]
result = 0
for i in range(n):
    result = max(result,graph[i][m-1])
print(result)