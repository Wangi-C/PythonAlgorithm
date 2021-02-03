#개미전사
n = int(input())
num = list(map(int,input().split()))
d = [0]*3000
d[1] = num[0]
for i in range(2,n+1):
    d[i] = max(d[i-1],num[i-1]+d[i-2])
print(d[n])