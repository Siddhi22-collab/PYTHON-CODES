


import heapq

# Create an empty list to use as a heap
min_heap = []

# Add elements using heappush
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 7)

print("Min Heap:", min_heap)

# Remove elements using heappop (always removes the smallest)
print("Smallest element:", heapq.heappop(min_heap))
print
