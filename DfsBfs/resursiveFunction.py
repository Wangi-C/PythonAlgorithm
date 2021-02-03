# #재귀함수
# def recursive_function(i):
#     if i == 100:
#         return
#     print(i, "번째 재귀함수에서 ",i + 1, "재귀함수를 호출합니다.")
#     recursive_function(i+1)
#     print(i,"번째에서 재귀를 종료합니다.")
# recursive_function(1)

# #팩토리얼 구현
# # # 0! = 1! = 1
# # #반복문
# # def factorial_iterative(n):
# #     result = 1
# #     for i in range(1, n+1):
# #         result *= i
# #     return result
# # #재귀
# # def factorial_recursive(n):
# #     if n <= 1:
# #         return 1
# #     return n * factorial_recursive(n-1)
# #
# # print("반복문 사용 : ",factorial_iterative(5))
# # print("재귀함수 사용 : ", factorial_recursive(5))

#유클리드 호제법(최대공약수 구하기기
def gcd(a, b):
    if a % b == 0:
        return b  
    else:
        return gcd(b, a%b)

print(gcd(192, 162))