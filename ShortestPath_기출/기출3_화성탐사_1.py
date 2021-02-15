import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
distance = [[INF] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

q = [(graph[0][0], 0, 0)]
distance[0][0] = graph[0][0]
while q:
    dist, x, y = heapq.heappop(q)
    if dist > distance[x][y]:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if distance[nx][ny] > dist + graph[nx][ny]:
                distance[nx][ny] = dist + graph[nx][ny]
                heapq.heappush(q, (distance[nx][ny], nx, ny))
print(distance[n-1][n-1])