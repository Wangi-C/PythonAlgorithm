# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2

import heapq
import sys

INF = int(1e9)
start = 1
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(n+1):
    i,j = map(int,input().split())
    graph[i].append((j,1))
    graph[j].append((i,1))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

max_node = 0
max_distance = 0
result = []
for i in range(1,n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
print(max_node, max_distance, len(result))