# import threading as th
# import time

# def worker(task_id):
#     print(f'Worker {task_id} started')
#     time.sleep(1)  # Simulate work
#     print(f'Worker {task_id} done')
#     return f'Result of worker {task_id}'


# threads = []
# for i in range(10):
#     t = th.Thread(target=worker, args=(i, ))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()

# print('Main')

import threading as th
import time
import math


def worker(task_id):
    print(f"Worker {task_id} started")
    # Perform a CPU-bound task: calculate factorial of a large number
    result = 0
    for i in range(5000000):  # Loop to add computational load
        result += i*i
    print(f"Worker {task_id} done")
    return result


start = time.perf_counter()

threads = []
for i in range(4):
    t = th.Thread(target=worker, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.perf_counter()
print(f"Multithreading completed in {end - start:.2f} seconds")
