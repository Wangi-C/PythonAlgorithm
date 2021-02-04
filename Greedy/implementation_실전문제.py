# #실전1 / 상하좌우 *
# n = int(input())
# x, y = 1, 1
# plans = input().split()
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move = ['L', 'R', 'U', 'D']
#
# for plan in plans:
#     for i in range(len(move)):
#         if plan == move[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx >n or ny > n:
#         continue
#
#     x, y = nx, ny
#
# print(x, y)

# #실전2 / 시각
# n = int(input())
#
# count = 0
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
# print(count)

#실전3 / 왕실의 나이트
order = input()
row = int(order[1])
column = int(ord(order[0]) - ord('a')) + 1

moves = [(-2, -1), (-2, 1), (-1,2), (1,2), (2,-1), (2,1), (-1,-2), (1,-2)]

count = 0
for move in moves:
    next_row = row + move[0]
    next_column = column + move[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        count += 1

print(count)