#정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left,bisect_right
n,x = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

# def count_by_range(data,x):
#     if not data.__contains__(x):
#         return None
#     right = bisect_right(data,x)
#     left = bisect_left(data,x)
#     return right - left
#
# if count_by_range(data,x) == None:
#     print(-1)
# else:
#     print(count_by_range(data,x))

def count_by_range(data,x):
    right = bisect_right(data,x)
    left = bisect_left(data,x)
    return right - left

if count_by_range(data,x) == 0:
    print(-1)
else:
    print(count_by_range(data,x))