#음료수 얼려 먹기
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())) )

dx = [-1,1,0,0]
dy = [0,0,-1,1]

count = 0
def dfs(x,y):
    graph[x][y] = 2
    for i in range(4):  
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                dfs(nx,ny)
            else:
                continue

for i in range(n):
    for j in range(m):
        num = graph[i][j]
        if num == 0:
            dfs(i,j)
            count += 1
print(count)