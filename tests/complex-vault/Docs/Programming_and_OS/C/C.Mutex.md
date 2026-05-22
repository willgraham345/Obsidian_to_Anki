---
type: note
---
# Background
- A mutex, short for "mutual exclusion," is a synchronization primitive used to control access to a shared resource by multiple threads in a concurrent program. It ensures that only one thread can access the protected resource (or section of code) at a time, preventing race conditions and maintaining data integrity.
# How to Define in C
- Defined and managed using the POSIX threads library `pthread`

```c
#include <stdio.h>
#include <pthread.h>

pthread_mutex_t myMutex = PTHREAD_MUTEX_INITIALIZER;

void* threadFunction(void* arg) {
    // Lock the mutex before accessing the shared resource
    pthread_mutex_lock(&myMutex);

    // Critical section: Access the shared resource

    // Unlock the mutex after finishing the critical section
    pthread_mutex_unlock(&myMutex);

    return NULL;
}

int main() {
    // ...

    pthread_t thread;
    pthread_create(&thread, NULL, threadFunction, NULL);

    // ...

    return 0;
}

```

- `pthread_mutex_t`: Data type representing the mutex
- `PTHREAD_MUTEX_INITIALIZER`: macro that initializes the mutex with default attributes. 
- To use the mutex, you lock it using `pthread_mutex_lock` before entering the critical section and unlock it using `pthread_mutex_unlock` after leaving the critical e