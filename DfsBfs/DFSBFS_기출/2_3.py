#연구소 #3
n,m = map(int,input().split())
lib = []
test = [[0]*m for _ in range(n)]
for i in range(n):
    lib.append(list(map(int,input().split())))

result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if test[nx][ny] == 0:
                test[nx][ny] = 2
                virus(nx,ny)

def getscore():
    score = 0
    for i in range(n):
        for j in range(m):
            if test[i][j] == 0:
                score += 1
    return score

def process(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                test[i][j] = lib[i][j]
        for i in range(n):
            for j in range(m):
                if test[i][j] == 2:
                    virus(i,j)
        result = max(result,getscore())
        return result

    for i in range(n):
        for j in range(m):
            if lib[i][j] == 0:
                lib[i][j] = 1
                count += 1
                process(count)
                count -= 1
                lib[i][j] = 0

process(0)
print(result)