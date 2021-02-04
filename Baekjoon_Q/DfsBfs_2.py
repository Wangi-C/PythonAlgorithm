#미로탈출
from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# count = [[0]*m for _ in range(n)]
# c = 0
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# queue = deque()
# queue.append((0,0))
#
# while queue:
#     x,y = queue.popleft()
#     count[x][y] = c
#     if x == n-1 and y == m-1:
#         print(count[x][y])
#         break
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < m:
#             if graph[nx][ny] == 1:
#                 c += 1
#                 queue.append((nx,ny))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((0, 0))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))