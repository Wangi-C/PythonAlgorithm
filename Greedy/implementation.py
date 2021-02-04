# #문제/ 시각
# h = int(input())
#
# count = 0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
#
# print(count)

# #p.115/ 왕실의 나이트
# #현재 나이트의 위치
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord("a")) + 1
#
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
#          (2, 1), (1, 2), (-1, 2), (-2, 1)]
#
# #8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     #이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     #해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row <= 8 and next_row >= 1 and next_column <=8 and next_column >= 1 :
#         result += 1
#
# print(result)

#p.322 / 문자열 재정렬
input_data = input()
count = 0
str_array = []

for data in input_data:
    if data.isalpha(): #알파벳인 경우 결과 리스트에 삽입
        str_array.append(data)
    else:
        count += int(data)

str_array.sort()

if count != 0:
    str_array.append(str(count))

print(''.join(str_array)) #최종 결과 출력(리스트를 문자열로 변환하여 출력)