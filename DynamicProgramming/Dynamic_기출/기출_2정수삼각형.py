n = int(input())
d = []
for i in range(n):
    d.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(d[i])):
        if j == 0:
            d[i][j] = d[i][j] + d[i-1][j]
        elif j == len(d[i])-1:
            d[i][j] = d[i][j] + d[i-1][j-1]
        else:
            right = d[i - 1][j]
            left = d[i-1][j-1]
            d[i][j] = d[i][j] + max(right,left)
result = 0
for i in range(len(d[n-1])):
    result = max(result,d[n-1][i])
print(result)