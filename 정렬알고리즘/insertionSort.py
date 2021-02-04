array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # j : 삽입하고자 하는 원소의 위치
        if array[j]<array[j-1]: #왼쪽 원소와 비교
            array[j],array[j-1] = array[j-1],array[j] #스와프
        else:
            break
print(array)