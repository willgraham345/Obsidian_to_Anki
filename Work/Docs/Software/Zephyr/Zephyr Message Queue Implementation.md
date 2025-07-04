---
type: note
---
# Two ways to do it
## 1
```c
struct data_item_type {
    uint32_t field1;
    uint32_t field2;
    uint32_t field3;
};

char my_msgq_buffer[10 * sizeof(struct data_item_type)];
struct k_msgq my_msgq;

k_msgq_init(&my_msgq, my_msgq_buffer, sizeof(struct data_item_type), 10);
```

## 2
```
K_MSGQ_DEFINE(my_msgq, sizeof(struct data_item_type), 10, 1);
```