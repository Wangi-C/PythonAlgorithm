INF = int(1e9)
n = int(input())
m = int(input())

plo = [[INF]*(n+1) for _ in range(n+1)]
for a in range(n+1):
    for b in range(n+1):
        if a == b:
            plo[a][b] = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    if c < plo[a][b]:
        plo[a][b] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            plo[a][b] = min(plo[a][b], plo[a][k] + plo[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        print(plo[a][b],end= " ")
    print()
