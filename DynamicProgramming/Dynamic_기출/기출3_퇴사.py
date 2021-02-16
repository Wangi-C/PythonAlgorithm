n = int(input())
t = [] #각 상담을 완료하는데 걸리는 기간
p = [] #각 강담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n+1)
max_value = 0
for _ in range(n):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)

for i in range(n-1,-1,-1):
    time = t[i] + 1
    #상담이 기간 안에 끝나는 경우
    if time <= n:
        #현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    #기간을 벗어나는 경우
    else:
        dp[i] = max_value
print(max_value)