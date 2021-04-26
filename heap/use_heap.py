import random
from heap import MinHeap

heap = MinHeap(500)
rand_arr = set()

for i in range(20):
    rand_arr.add(random.randint(0, 999))

print(rand_arr)

for i in rand_arr:
    heap.insert(i)

print(heap.heap_array)

for i in range(5):
    print(heap.remove())

print(heap.heap_array)
