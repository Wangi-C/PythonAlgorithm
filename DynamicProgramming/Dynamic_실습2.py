#1로 만들기
n = int(input())
# count = 0
# def one_made(n):
#     global count
#     if n == 1:
#         return count
#     if(n % 5 == 0):
#         num = n // 5
#         count+=1
#         one_made(num)
#     elif(n % 3 == 0):
#         num = n // 3
#         count += 1
#         one_made(num)
#     elif(n % 2 == 0):
#         num = n // 2
#         count += 1
#         one_made(num)
#     else:
#         num = n - 1
#         count += 1
#         one_made(num)
#
# print(one_made(n))
d = [0]*30001
for i in range(2,n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i],d[i//5] + 1)
print(d[n])