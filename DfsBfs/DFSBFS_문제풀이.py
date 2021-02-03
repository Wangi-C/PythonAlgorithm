# #문제1 / 음료수 얼려 먹기 _ 연결요소찾기
# #dfs 또는 bfs로 해결
# n,m = map(int, input().split())
#
# graph = [] #2차원 리스트의 맵 정보 입력
# for i in range(n):
#     graph.append(list(map(int,input())))
#
# def dfs(x,y):
#     if x <= -1 or x >= n or y <= -1 or y >= m: # 주어진 범위를 벗어나는 경우 즉시 종료
#         return False
#     if graph[x][y] == 0: #현재 노드를 아직 방문하지 않았다면
#         graph[x][y] = 1 #현재 노드 방문처리
#         # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1
#
# print(result)

#문제2 / 미로 탈출
from collections import deque

n,m = map(int,input().split())

game = []
for i in range(n):
    game.append(list(map(int, input())))
#이동할 네 가지 방향 정의 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #벽인 경우 무시
            if game[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if game[nx][ny] == 1:
                game[nx][ny] = game[x][y] + 1
                queue.append((nx, ny))
    return game[n-1][m-1]

print(bfs(0,0))