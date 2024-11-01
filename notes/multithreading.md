# Multithreading

## Difference between concurrency and parallelism

Imagine a coffee shot

concurrency is 2 customer lines and one cashier, and parallelism is 2 customer lines and 2 cashiers.

More formal definition:

Concurrency is when two or more tasks can start, run, and complete in overlapping time periods. It doesn't necessarily mean they'll ever both be running at the same instant. For example, multitasking on a single-core machine.

Parallelism is when tasks literally run at the same time, e.g., on a multicore processor.

References:
[stackoverflow](https://stackoverflow.com/questions/1050222/what-is-the-difference-between-concurrency-and-parallelism)

```bash
sysctl -a | grep machdep.cpu
machdep.cpu.cores_per_package: 8
machdep.cpu.core_count: 8
machdep.cpu.logical_per_package: 8
machdep.cpu.thread_count: 8
machdep.cpu.brand_string: Apple M2
```

Multiprocessing: using different cpu cores. 
 
**Overhead in multiprocessing**

For simple tasks (like time.sleep), this overhead can make multiprocessing slower than multithreading.

**Threading and the GIL**

The GIL allows only one thread to execute Python bytecode at a time, which limits the speed of multithreading for CPU-bound tasks.

However, the GIL is released during I/O operations (like time.sleep), allowing multiple threads to execute "simultaneously" when they're primarily waiting. This is why multithreading works well for I/O-bound tasks in Python.

Note: The performance boost in multiprocessing can be seen for high CPU bound programs, for I/O and low CPU bound multithreading seems to perform better.