import threading
import time

def worker(task):
    print(f"Starting {task}")
    time.sleep(2)
    print(f"Finished {task}")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Task-{i}",))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All tasks completed.")
