#예제3-1
# n = 1260
# count = 0
#
# array = [500, 100, 50, 10]
#
# for coin in array:
#     count += n//coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기 (몫)
#     n %= coin
#
# print(count)
#복잡도 (시간) : O(k),화폐의 단위 갯수만큼



# #문제4
# #n,k를 공백을 기준으로 구분하여 입력
# n , k = map(int, input().split())
#
# result = 0
#
# while True:
#     #n이 k로 나누어 떨어지는 수가 될때까지 빼기
#     target = (n // k) * k #k의 배수 중 n에 가장 가까운 수
#     result += (n - target)
#     n = target
#
#     if(n<k): #n이 k보다 작을 때 탈출(더 이상 나눌 수 없을 때)
#         break
#     # k로 나누기
#     result += 1
#     n //= k
#
# # 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n - 1)
# print(result)



# #p.312 / 곱하기 혹은 더하기
# data = input()
#
# result = int(data[0])
#
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
#
# print(result)



#p.311 / 모험가 길드
n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: #공포도가 낮은 것부터 하나씩 확인
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 #총 그룹의 수 증가
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력