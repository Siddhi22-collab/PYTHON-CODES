import queue

q = queue.Queue(maxsize=3)

# Enqueue
q.put(10)
q.put(20)
q.put(30)

print("Full:", q.full())     # True
print("Size:", q.qsize())    # 3

# Dequeue
print("Removed:", q.get())
print("Size after dequeue:", q.qsize())  # 2
