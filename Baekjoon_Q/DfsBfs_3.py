#특정 거리의 도시 찾기
from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
dis = [0] * (n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

queue = deque()
queue.append(x)

while queue:
    q = queue.popleft()
    for i in range(len(graph[q])):
        num = graph[q][i]
        if dis[num] == 0:
            dis[num] = dis[q] + 1
            queue.append(num)

find = False
for i in range(n+1):
    if dis[i] == k:
        find = True
        print(i)
if find == False:
    print(-1)