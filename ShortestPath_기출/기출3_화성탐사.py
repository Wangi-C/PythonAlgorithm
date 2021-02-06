INF = int(1e9)
n = int(input())
plo = [[INF]*n for _ in range(n)]
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
plo[0][0] = 0
for k in range(n):
    for a in range(n):
        for b in range(n):
            plo[a][b] = min(plo[a][b],graph[a][k] + graph[k][b])
print(plo[n-1][n-1])