#고정점 찾기
n = int(input())
data = list(map(int,input().split()))
data.sort()

start = 0
end = (n-1)

find = False
result = 0
while (start <= end):
    mid = (start + end) // 2
    if data[mid] == mid:
        find = True
        result = mid
        break
    if data[mid] > mid:
        end = mid - 1
    elif data[mid] < mid:
        start = mid + 1

if not find:
    print(-1)
else:
    print(result)