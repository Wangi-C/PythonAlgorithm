# 특정 거리의 도시 찾기 #2
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

countlist = [-1] * (n + 1)
countlist[x] = 0

queue = deque([x])

while queue:
    v = queue.popleft()
    for i in graph[v]:
        if countlist[i] == -1:
            queue.append(i)
            countlist[i] = countlist[v] + 1

check = False
for i in range(1, n + 1):
    if countlist[i] == k:
        print(i, end=" ")
        check = True
if check == False:
    print(-1)
