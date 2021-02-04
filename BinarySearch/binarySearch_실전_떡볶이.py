#떡볶이 떡 만들기
n,m = map(int,input().split())

data = list(map(int,input().split()))

# end = max(data)
#
# def cut(data,start,end,m):
#     global result
#     cr = []
#     mid = (start + end) // 2
#     for i in data:
#         r = i - mid
#         if r > 0:
#             cr.append(r)
#
#     if sum(cr) > m:
#         result = mid
#         return cut(data,mid+1,end,m)
#     elif sum(cr) < m:
#         return cut(data,start,mid-1,m)
#     elif sum(cr) == m:
#         result = mid
#     return result
#
# cut(data,0,end,m)
# print(result)

#정답
start = 0
end = max(data)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in data:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)