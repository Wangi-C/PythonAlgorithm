#경쟁적 전염 #2
from collections import deque

n,k = map(int,input().split())
data = []
virus_m = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] != 0:
            virus_m.append((data[i][j], 0, i, j))

virus_m.sort()
q = deque(virus_m)

ts, tx, ty = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    virus, s, x, y = q.popleft()
    if s == ts:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(data[tx-1][ty-1])