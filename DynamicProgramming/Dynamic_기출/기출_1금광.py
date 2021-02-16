t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    d = []
    index = 0
    for i in range(n):
        d.append(array[index:index+m])
        index += m

    for i in range(1,m):
        for j in range(n):
            if j == 0:
                left_up = 0
            else:
                left_up = d[j-1][i-1]
            if j == n-1:
                left_down = 0
            else:
                left_down = d[j+1][i-1]

            left = d[j][i-1]
            d[j][i] = d[j][i] + max(left_down,left,left_up)
    result = 0
    for i in range(n):
        result = max(result,d[i][m-1])
    print(result)