n = int(input())
array = list(map(int,input().split()))
max_score = 1
for i in range(n):
    if (i+1) < n:
        if array[i] < array[i+1]:
            continue
        elif array[i] > array[i+1]:
            max_score += 1
print(n-max_score)