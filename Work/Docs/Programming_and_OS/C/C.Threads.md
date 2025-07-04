---
type: note
---
# Background
Creating threads instead of using a series of functions offers several advantages:
1. **Concurrency:** Threads enable concurrent execution of tasks, which can improve the overall performance and responsiveness of your program, particularly on multi-core processors.
2. **Asynchronous Operations:** Threads allow you to perform tasks asynchronously, which means that your program can continue executing other tasks while waiting for certain operations to complete.
3. **Modularity:** Threads can be used to separate different tasks into different threads, leading to better code organization and maintainability.
4. **Parallelism:** Threads enable parallel processing, where tasks are divided into smaller parts and executed simultaneously on different cores.

# Example
```C
#include <stdio.h>
#include <pthread.h>

void* threadFunction(void* arg) {
    // Code to be executed in the thread
    printf("Thread is running\n");
    return NULL;
}

int main() {
    pthread_t thread;
    
    // Create a new thread and associate it with the threadFunction
    pthread_create(&thread, NULL, threadFunction, NULL);
    
    // Wait for the thread to finish
    pthread_join(thread, NULL);

    printf("Thread has finished\n");

    return 0;
}

```