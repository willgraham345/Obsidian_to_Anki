---
type: note
---
Frames are only received when they match a filter

Here's how to receive frames by attaching filters

```c
void rx_callback_function(struct zcan_frame *frame, void *arg)
{
        ... do something with the frame ...
}
```
Shows a filter 


## `can_attach_isr` Example
This example shows how to attach a filter with an interrupt callback. This is the most efficient but also the most critical way to receive messages. Callback is called from an interrupt context, meaning that the callback function should be as short as possible and should not block. Attaching ISRs is not allowed from userspace context
```c
const struct zcan_filter my_filter = {
        .id_type = CAN_STANDARD_IDENTIFIER,
        .rtr = CAN_DATAFRAME,
        .id = 0x123,
        .rtr_mask = 1,
        .id_mask = CAN_STD_ID_MASK
};
int filter_id;
const struct device *can_dev;

can_dev = device_get_binding("CAN_0");

filter_id = can_attach_isr(can_dev, rx_callback_function, callback_arg, &my_filter);
if (filter_id < 0) {
  LOG_ERR("Unable to attach isr [%d]", filter_id);
}

```

## `can_attach_msgq` Example
This example shows how to attach a callback from a work-queue. In contrast to the [`can_attach_isr`](https://docs.zephyrproject.org/2.7.5/reference/networking/can_api.html#c.can_attach_isr "can_attach_isr") function, here the callback is called from the work-queue provided. In this case, it is the system work queue. Blocking is generally allowed in the callback but could result in a frame backlog when it is not limited. For the reason of a backlog, a ring-buffer is applied for every attached filter. The size of this buffer can be adjusted in Kconfig. This function is not yet callable from userspace context but will be in the future.
```c
const struct zcan_filter my_filter = {
        .id_type = CAN_STANDARD_IDENTIFIER,
        .rtr = CAN_DATAFRAME,
        .id = 0x120,
        .rtr_mask = 1,
        .id_mask = 0x7F0
};
struct zcan_work rx_work;
int filter_id;
const struct device *can_dev;

can_dev = device_get_binding("CAN_0");

filter_id = can_attach_workq(can_dev, &k_sys_work_q, &rx_work, callback_arg, callback_arg, &my_filter);
if (filter_id < 0) {
  LOG_ERR("Unable to attach isr [%d]", filter_id);
}
```
