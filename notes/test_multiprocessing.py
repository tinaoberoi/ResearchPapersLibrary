# import time
# import multiprocessing as mp

# # Define the function for each process to execute
# def worker(task_id):
#     print(f'Worker {task_id} started')
#     time.sleep(1)  # Simulate work
#     print(f'Worker {task_id} done')
#     return f'Result of worker {task_id}'

# if __name__ == '__main__':
#     start = time.perf_counter()

#     p_lst = []
#     with mp.Pool(processes=4) as pool:
#         results = pool.map(worker, range(4))

#     print('Main')
#     print(results)

import multiprocessing as mp
import time
import math

def worker(task_id):
    print(f'Worker {task_id} started')
    result = 0
    for i in range(5000000):
        result += i*i
    print(f'Worker {task_id} done')
    return result

if __name__ == '__main__':
    start = time.perf_counter()
    
    with mp.Pool(processes=4) as pool:
        results = pool.map(worker, range(4))

    end = time.perf_counter()
    print(f"Multiprocessing completed in {end - start:.2f} seconds")
    print(results)
