# GPU and CUDA Interview Preparation

---

### 1. How many different kinds of memories are in a GPU?
A GPU typically has several types of memory, including:
   - **Global Memory**: The largest memory on a GPU, accessible by all threads, but with higher latency.
   - **Shared Memory**: Memory shared among threads within the same block; it has much lower latency and is faster than global memory.
   - **Registers**: Private to each thread; extremely fast but limited in quantity.
   - **Constant Memory**: Read-only memory, cached, and accessible to all threads; optimized for data that doesn’t change frequently.
   - **Texture Memory**: Optimized for certain types of read operations, especially for 2D spatial locality.

---

### 2. What means coalesced/uncoalesced?
   - **Coalesced memory access**: Threads within a warp access consecutive global memory addresses, leading to more efficient memory transactions.
   - **Uncoalesced memory access**: Threads access non-sequential or scattered addresses, resulting in slower memory access due to multiple transactions.

---

### 3. Can you implement a matrix transpose kernel?
   - Yes, a matrix transpose kernel can be implemented in CUDA using shared memory to optimize for coalesced memory access. Shared memory allows threads to load values, avoid uncoalesced accesses, and then write them back in transposed order, significantly improving performance.

---

### 4. What is a warp?
   - A **warp** is a group of typically 32 threads in CUDA (on NVIDIA GPUs) that execute the same instruction at the same time. All threads in a warp execute in a SIMD (Single Instruction, Multiple Data) fashion, although they may take different code paths due to conditional statements.

---

### 5. How many warps can run simultaneously inside a multiprocessor?
   - The number of warps that can run concurrently in a multiprocessor depends on the GPU architecture. For example, on an NVIDIA GPU with a certain CUDA Compute Capability, you might have a maximum of 64 active warps per streaming multiprocessor (SM).

---

### 6. What is the difference between a block and a thread?
   - A **thread** is the smallest unit of execution within a GPU kernel. Threads are grouped into **blocks**, which share certain resources like shared memory and can synchronize within a block. Each kernel is made up of multiple blocks that together execute in parallel on the GPU.

---

### 7. Can threads communicate between them? And blocks?
   - **Threads within the same block** can communicate through shared memory and synchronize with each other using `__syncthreads()`.
   - **Threads across different blocks** generally cannot communicate directly. Inter-block communication requires global memory or multi-kernel approaches.

---

### 8. Can you describe how a cache works?
   - A cache temporarily stores frequently accessed data to reduce the latency of accessing that data from main (global) memory. When a thread accesses memory, the cache first checks if the data is available. If it is (a “cache hit”), it retrieves it much faster than from global memory. If not (a “cache miss”), it fetches it from global memory and stores it in the cache for potential future access.

---

### 9. What is the difference between shared memory and registers?
   - **Shared memory** is accessible to all threads within a block and is useful for data that needs to be shared among those threads.
   - **Registers** are private to each thread, very fast, but are limited in number. Registers are not shared and cannot be accessed by other threads.

---

### 10. Which algorithms perform better on the GPU? Data-bound or CPU-bound?
   - **Data-bound** algorithms, especially those that can be highly parallelized, generally perform better on GPUs. GPU performance excels with algorithms that require many parallel operations on large datasets, like matrix operations, neural networks, or image processing. CPU-bound algorithms with heavy branching or low parallelism often perform better on CPUs.
    - data bound = involve large data sets and heavy parallel operations.

---

### 11. Which steps will you perform to port an application to CUDA?
   - Identify parallelizable parts of the code.
   - Allocate memory on the GPU for data to be processed.
   - Copy data from the CPU to the GPU.
   - Launch the kernel(s) on the GPU with appropriately chosen grid and block sizes.
   - Copy results from the GPU back to the CPU.
   - Free allocated memory on the GPU after computations are completed.

---

### 12. What is a barrier?
   - A **barrier** is a synchronization point where threads wait until all threads in a block have reached this point before continuing. In CUDA, `__syncthreads()` is an example of a barrier within a block.

---

### 13. What is a Stream?
   - In CUDA, a **stream** is a sequence of operations (kernel launches, memory copies, etc.) that execute in order on the GPU. Streams allow for concurrent execution and are used to overlap kernel execution with memory transfers or run multiple kernels in parallel.

---

### 14. Can you describe what occupancy of a kernel means?
   - **Occupancy** is the ratio of active warps to the maximum possible warps on a streaming multiprocessor (SM). High occupancy can improve performance by keeping the GPU fully utilized, though it isn’t the only factor affecting performance.

---

### 15. What means structure of array vs. array of structures?
   - **Structure of Array (SoA)**: Each array holds a single attribute for all elements. This is often preferred in GPU programming because it enables coalesced memory access.
   ```
   struct Position {
        float* x;
        float* y;
        float* z;
    };
   ```
   - **Array of Structures (AoS)**: Each array element is a structure holding multiple attributes. This can lead to uncoalesced memory access and is generally less efficient for parallel processing.
    ```
    struct Position {
        float x;
        float y;
        float z;
    };
    Position pos[N];
    ```
  
---
"You have N vectors of length M (N>>M). Tell me how you would go about designing a kernel to evaluate the distance matrix. Pay special attention to the way the problem is sub-divided and to the way the thread co-operation can be used to improve occupancy.

How would your answer to this question change if M>>N?"

The idea here is not to get you writing code, but to get you thinking out loud. This shows that you really know how to use GPGPU technology and are not merely regurgitating the user guide.

---
### How to improve memory access in CUDA

To optimize memory access in a CUDA program, the following steps can be taken:

Use coalesced memory access by making sure that threads within a warp access contiguous memory locations. This can be achieved using data layout optimization and thread block size selection.
Reduce bank conflicts by ensuring that data within a shared memory bank is not accessed by multiple threads simultaneously.
Minimize global memory access by maximizing the usage of shared memory and register files.
Use asynchronous data transfer to overlap data transfer time with kernel execution time.
Use texture memory for read-only data as it provides caching and filtering functionalities.
Implement memory access patterns using CUDA streams to increase concurrency

---
### Describe and write an implementation of memcopy function and suggest improvements (SSE copying using assembly and the 128 bit register)

---

### How would you sum a billion long array of half precision numbers to achieve best possible accuracy

--- 

### Write an implementation of malloc in C (referring to the stack and heap).
--- 

### Describe an algorithm to find a missing number in a sequence of integers stored in a file
--- 

### Write two classes in C++ where one inherits from the other and where the inheriting class is a template classs
--- 

### How would you compute the factorial of a given small number at compile time rather than runtime?
--- 

### How would you sum a billion long array of floating point numbers to achieve best possible accuracy
--- 

### The basic knowledge of C++. 2. New feature of latest C++. 3. Basic knowledge of CUDA. Including synchronize, reduction(how to realize it), memory hierarchy.

# CUDA Reduction

In CUDA, **reduction** is a common parallel algorithm used to reduce an array of elements to a single result, typically by performing an operation like sum, min, or max. Efficient reduction is essential for performance in parallel computing, and CUDA’s reduction techniques make extensive use of **shared memory** and **synchronization**.

** Steps to Realize Reduction in CUDA**

1. **Divide Data Among Threads**: Each thread initially operates on a portion of the array.
2. **Use Shared Memory for Efficiency**: Shared memory is used to store intermediate results for each block, as it's much faster than global memory.
3. **Iteratively Reduce Within Each Block**: Threads within a block reduce their partial results iteratively.
4. **Final Reduction Across Blocks**: The final result is computed by reducing results from each block in a secondary kernel or on the host.

---

## CUDA Reduction Code Example

This example shows how to sum an array using CUDA reduction:

```cpp
#include <cuda_runtime.h>
#include <iostream>

// Kernel for reduction
__global__ void reduceKernel(int* d_in, int* d_out, int size) {
    extern __shared__ int sdata[];  // Shared memory for block

    int tid = threadIdx.x;
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    // Load elements from global memory to shared memory
    sdata[tid] = (i < size) ? d_in[i] : 0;
    __syncthreads();

    // Perform reduction in shared memory
    for (int s = blockDim.x / 2; s > 0; s >>= 1) {
        if (tid < s) {
            sdata[tid] += sdata[tid + s];
        }
        __syncthreads();  // Ensure all threads have updated sdata
    }

    // Write the result of this block to global memory
    if (tid == 0) {
        d_out[blockIdx.x] = sdata[0];
    }
}

