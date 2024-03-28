import heapq
 
 
array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
heap = []

for value in array:
    heapq.heappush(heap, value)

print(heap[0])

heap_sort = [heapq.heappop(heap) for _ in range(len(heap))]
print(heap_sort) 

heapq.heapify(array)
print(heapq.nlargest(2, array))
print(heapq.nsmallest(3,array))


array_a = [10, 7, 15, 8]
array_b = [17, 3, 8, 20, 13]

array_merge = heapq.merge(sorted(array_a), sorted(array_b))

print(list(array_merge))

array_c = [10, 7, 15, 8]
heapq.heapify(array_c)
print("before:", array_c)

item = heapq.heappushpop(array_c, 5)
print("after:", array_c)
print(item)

array_d = [10, 7, 15, 8]
heapq.heapify(array_d)

print("before:", array_d)

item = heapq.heapreplace(array_d, 5)
print("after:", array_d)
print(item)
