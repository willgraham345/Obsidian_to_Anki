---
type: note
---

# [Example](https://docs.zephyrproject.org/2.7.5/reference/networking/can_api.html#id2)
This basic sample sends a CAN frame with standard identifier 0x123 and eight bytes of data. When passing NULL as the callback, as shown in this example, the send function blocks until the frame is sent and acknowledged by at least one other node or an error occurred. The timeout only takes effect on acquiring a mailbox. When a transmitting mailbox is assigned, sending cannot be canceled.
```c
struct zcan_frame frame = {
        .id_type = CAN_STANDARD_IDENTIFIER,
        .rtr = CAN_DATAFRAME,
        .id = 0x123,
        .dlc = 8,
        .data = {1,2,3,4,5,6,7,8}
};
const struct device *can_dev;
int ret;

can_dev = device_get_binding("CAN_0");

ret = can_send(can_dev, &frame, K_MSEC(100), NULL, NULL);
if (ret != CAN_TX_OK) {
        LOG_ERR("Sending failed [%d]", ret);
}
```
This example shows how to send a frame with extended identifier 0x1234567 and two bytes of data. The provided callback is called when the message is sent, or an error occurred. Passing [`K_FOREVER`](https://docs.zephyrproject.org/2.7.5/reference/kernel/timing/clocks.html#c.K_FOREVER "K_FOREVER") to the timeout causes the function to block until a transfer mailbox is assigned to the frame or an error occurred. It does not block until the message is sent like the example above.
```c
void tx_irq_callback(int error, void *arg)
{
        char *sender = (char *)arg;

        if (error != 0) {
                LOG_ERR("Sendig failed [%d]\nSender: %s\n", error, sender);
        }
}

int send_function(const struct device *can_dev)
{
        struct zcan_frame frame = {
                .id_type = CAN_EXTENDED_IDENTIFIER,
                .rtr = CAN_DATAFRAME,
                .id = 0x1234567,
                .dlc = 2
        };

        frame.data[0] = 1;
        frame.data[1] = 2;

        return can_send(can_dev, &frame, K_FOREVER, tx_irq_callback, "Sender 1");
}
```