#경쟁적 전염
from collections import deque

n,k = map(int,input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j))
data.sort()
q = deque(data)

ts, tx, ty = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    virus, s, x, y = q.popleft()
    if ts == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny < n:
            graph[nx][ny] = virus
            q.append((virus,s+1,nx,ny))

print(graph[tx-1][ty-1])