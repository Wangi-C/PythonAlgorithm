# 정렬된 배열에서 특정 수의 개수 구하기
n, x = map(int, input().split())
num = list(map(int, input().split()))
num_max = max(num)
count = [0] * (num_max + 1)

for i in range(n):
    count[num[i]] += 1
if x >num_max or count[x] == 0:
    print(-1)
else:
    print(count[x])