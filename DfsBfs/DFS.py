# #dfs
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=" ")   #방문 순서대로
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#     # print(v, end=" ")  # stack에서 나온 순으로
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
# dfs(graph, 1, visited)

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
visited = [False]*9

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, i, visited)

dfs(graph, 1, visited)