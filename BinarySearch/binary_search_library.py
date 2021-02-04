#값이 특정 범위에 속하는 데이터 개수 구하기

from bisect import bisect_left, bisect_right
def count_by_range(a, left, right):
    right = bisect_right(a, right)
    left = bisect_left(a, left)
    return right - left

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))