# 연구소
n, m = map(int, input().split())
graph = []
event = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if event[i][j] == 0:
                score += 1
    return score


def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if event[nx][ny] == 0:
                event[nx][ny] = 2
                virus(nx, ny)


def process(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                event[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if event[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                process(count)
                graph[i][j] = 0
                count -= 1


process(0)
print(result)
