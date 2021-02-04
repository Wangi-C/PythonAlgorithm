#안테나
# n = int(input())
# num = list(map(int,input().split()))
# num.sort()
# result = 0
# min_score = 1e9
# h = 0
# for i in range(n):
#     for j in num:
#         if num[i] > j:
#             h += (num[i] - j)
#         else:
#             h += (j - num[i])
#     min_score = min(min_score,h)
#     if min_score == h:
#         result = num[i]
#     h = 0
#
# print(result)

# #답
# n = int(input())
# data = list(map(int,input().split()))
# data.sort()
#
# print(data[(n-1) // 2])

import time

  # 시작 시간 저장

n = int(input())
num = list(map(int,input().split()))
start = time.time()
num.sort()
result = 0
min_score = 1e9
h = 0
for i in range(n):
    for j in num:
        if num[i] > j:
            h += (num[i] - j)
        else:
            h += (j - num[i])
    min_score = min(min_score,h)
    if min_score == h:
        result = num[i]
    h = 0

print(result)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간