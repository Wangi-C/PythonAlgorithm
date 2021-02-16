#정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left,bisect_right

n,x = map(int,input().split())
data = list(map(int,input().split()))

def count(data,x):
    left = bisect_left(data,x)
    right = bisect_right(data,x)
    return right - left

if count(data,x) == 0:
    print(-1)
else:
    print(count(data,x))