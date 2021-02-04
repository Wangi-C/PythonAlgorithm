# 경쟁적 전염
from collections import deque

n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus_data = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus_data.append((graph[i][j], 0, i, j))

virus_data.sort()
queue = deque(virus_data)

while queue:
    virus,s,x,y = queue.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                queue.append((virus,s + 1,  nx, ny))
                graph[nx][ny] = virus

print(graph[target_x-1][target_y-1])