#최소힙
import heapq

#오름차순 힙 정렬
def heapsort(iterable):
    h = []
    rh = []
    result = []
    reverse_result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
        heapq.heappush(rh,-value) #내림차순
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
        reverse_result.append(-heapq.heappop(rh)) #내림차순
    return result,reverse_result

result = heapsort([1, 3, 5, 4, 6, 7, 8, 0, 9, 2])
print(result)