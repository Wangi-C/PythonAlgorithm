# from collections import deque
#
# graph = [[],
#          [2,3,8],
#          [1,7],
#          [1,4,5],
#          [3,5],
#          [3,4],
#          [7],
#          [2,6,8],
#          [1,7]
# ]
# visited = [False] * 9 #각 노드가 방문된 정보를 표현(1차원 리스트)
#
# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True #현재 노드 방문 처리
#     while queue:
#         v = queue.popleft()
#         print(v, end=" ")
#         for i in graph[v]: #아직 방문하지 않은 인접한 원소들을 큐에 삽입
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# bfs(graph, 1, visited)

from collections import deque
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)