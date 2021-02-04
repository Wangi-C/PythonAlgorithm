# #실전2 : 큰 수의 법칙
# n, m , k = map(int,input().split())
#
# num_array = list(map(int,input().split()))
# num_array.sort()
#
# firstnum = num_array[n-1]
# secondnum = num_array[n-2]
#
# Count = (m // (k+1)) * k
# Count += m % (k+1)
#
#
# result = 0
# result += (Count) * firstnum
# result += (m - Count) * secondnum
#
# print(result)

# # 실전3 / 숫자 카드 게임
# # n, m = map(int, input().split())
# # result = 0
# #
# # for i in range(n):
# #         data = list(map(int, input().split()))
# #         min_value = min(data)
# #         result = max(result,min_value)
# #
# # print(result)

# 실전4 / 1이 될 때까지
n, k = map(int, input().split())

OneCount = (n % k)
n -= (1 * OneCount)
count = 0
while True:
    if (n == 1):
        break
    n //= k
    count += 1

result = count + OneCount
print(result)
