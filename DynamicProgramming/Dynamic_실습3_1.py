#효율적인 화폐구성
n,m = map(int,input().split())
num = []
for i in range(n):
    num.append(int(input()))
d = [10001] * (m+1)
d[0] = 0
for i in range(n):
    money = num[i]
    for j in range(money,m+1):
        if (d[j-money] != 10001):
            d[j] = min(d[j],d[j-money]+1)

if d[m] != 10001:
    print(d[m])
else:
    print(-1)