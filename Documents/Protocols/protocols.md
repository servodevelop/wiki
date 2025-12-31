---
layout: default
title: UART/RS485 Bus Servo Communication Protocol
parent: Protocols
grand_parent: Documents
nav_order: 1
---

# UART/RS485 Bus Servo Communication Protocol

**v1.0.25**

## 1. Introduction

This document introduces the **UART/RS485** Bus servo communication protocol. The protocol uses **asynchronous serial** communication technology, providing a standardized solution for the transmission of control commands and status feedback between the master device and multiple servos.

### **1.1 Communication Mechanism**

This protocol is based on **half-duplex asynchronous serial communication**, using **8 data bits**, **1 stop bit**, and no parity bit. During communication, TxD and RxD cannot be used simultaneously; therefore, only one device can transmit data at a time, while the other devices remain in receiving mode. This half-duplex communication mode is suitable for scenarios where multiple devices share the same communication bus.

### 1.2 Servo ID

In the entire communication system, each servo motor is assigned a unique **ID** for effective device addressing on the bus. The communication protocol uses a **command-response** mechanism to ensure reliable interaction in multi-device environments. The protocol defines the packet structure, parameter fields, checksum rules, and error handling methods in detail to ensure stable operation of the servos in various applications.

> [!NOTE]
>
> The **default** factory servo ID is **0**.



### 1.3 Command Interval

To ensure stable communication, it is recommended that the **command interval** be between **5-10ms**.

By ensuring a sufficient time interval, communication timeouts or errors can be effectively avoided, and reliable transmission of data packets is ensured.



## 2. Control Commands

| Command Name                                          |   Command ID   | Response Packet Type |
| ----------------------------------------------------- | :------------: | -------------------- |
| Ping                                                  | **01** (0x01)  | Fixed                |
| Single-Turn Position Control (Basic)                  | **08**  (0x08) | Optional             |
| Single-Turn Position Control (Advanced - Time-based)  | **11**  (0x0b) | Optional             |
| Single-Turn Position Control (Advanced - Speed-based) | **12**  (0x0c) | Optional             |
| Read Single-Turn Current Position                     | **10**  (0x0a) | Fixed                |
| Multi-Turn Position Control (Basic)                   | **13**  (0x0d) | Optional             |
| Multi-Turn Position Control (Advanced - Time-based)   | **14**  (0x0e) | Optional             |
| Multi-Turn Position Control (Advanced - Speed-based)  | **15**  (0x0f) | Optional             |
| Read Multi-Turn Current Position                      | **16**  (0x10) | Fixed                |
| Stop Instructions                                     | **24**  (0x18) | Optional             |
| Reset Loop                                            | **17**  (0x11) | Optional             |
| Damping Control                                       | **09**  (0x09) | Optional             |
| Set Origin Point                                      | **23**  (0x17) | Optional             |
| Synchronous Instruction                               | **25**  (0x19) | /                    |
| Asynchronous Write Instruction                        | **18**  (0x12) | Optional             |
| Asynchronous Activate Instruction                     | **19**  (0x13) | /                    |
| Read Data                                             | **03**  (0x03) | Fixed                |
| Data Monitor                                          | **22**  (0x16) | Fixed                |
| Customize Configuration Parameters                    | **04**  (0x04) | Optional             |



## 3. Packet Structure

### 3.1 Command Packet

**Command Packet** is the standard data structure used by the master control to send control or query commands to the servo.

- **header:** Fixed as `0x12 0x4C`, used to identify the start of the command packet.
- **cmd_id:** The control command for this packet.
- **length:** Indicates the number of bytes of the subsequent data (content), used for packet parsing.

- **content:** Stores control parameters (e.g., servo ID, target position, motion time, power, etc.), depending on the control command.
- **checksum:** The result of adding all bytes and taking the modulo 256, used to check data integrity.

**Communication Mechanism:**
The master control sends a command packet to the servo to send control or read requests. After receiving a valid command packet, the servo parses the parameters and returns the corresponding **Response Packet**.

![command package](images_rs485/command_package.png)



### 3.2 Response Packet

**Response Packet** is the standard data structure returned by the servo to the master control after receiving and parsing a valid **Command Packet**. It contains the execution result and related data. The overall structure is the same as the command packet, but the starting position identifier and data content definitions differ.

- **header:** Fixed as `0x05 0x1C`, used to identify the start of the response packet.
- **cmd_id:** The control command for this packet.
- **length:** Indicates the number of bytes of the subsequent data (content), used for packet parsing.  

- **content:** Returns the execution result or corresponding data (e.g., current angle, voltage, temperature, version, read-back parameters, etc.), depending on the control command.
- **checksum:** The result of adding all bytes and taking the modulo 256, used to check data integrity.

![response_package](images_rs485/response_package.png)

> [!NOTE]
>
> **Response Packet Types**
>
> - **Fixed Response: **Response packet is always returned.
> - **Optional Response:** Whether a response is returned depends on the PC configuration parameter `Response after action`(default = No).
> - **Recommendation:** For time-sensitive batch control scenarios (e.g., multi-servo synchronous control), it is recommended to disable configurable responses to reduce bus occupation. However, during debugging and fault diagnosis, enabling them is recommended for quick issue identification.



## 4. Data Types

| Data Types | Data Name                  | Length |  Minimum Value | Maximum Value |
| :--------- | :------------------------- | :----: | -------------: | ------------: |
| uint8_t    | Signed Short Int           |   1    |              0 |           255 |
| uint16_t   | Unsigned Short Int         |   2    |              0 |        65,535 |
| int16_t    | Signed Short Int           |   2    |        -32,768 |        32,767 |
| uint32_t   | Unsigned Long Int          |   4    |              0 | 4,294,967,295 |
| int32_t    | Signed Long Int            |   4    | -2,147,483,648 | 2,147,483,647 |
| uint8_t[n] | Variable-Length Byte Array |   n    |                |               |

> [!CAUTION]
>
> The byte order used in the servo communication protocol is **Little Endian**. For example, a `uint16_t` value of `4,660`, represented in hexadecimal as `0x1234`, will be sent/received in the order of `0x34 0x12`, with the low byte first and the high byte last.



## 5. Ping

### 5.1 Overview

- By sending the **Ping** command for the corresponding servo motor ID, the status of whether the servo is online can be determined based on the response packet.

- Command ID: **01** (0x01)

  

### 5.2 Command

| Byte Name  | Length | Data Type | Description                      |
| ---------- | :----: | :-------: | -------------------------------- |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**) |
| `cmd_id`   |   1    |  uint8_t  | Ping (**0x01**)                  |
| `length`   |   1    |  uint8_t  | 1 byte (**0x01**)                |
| `servo_id` |   1    |  uint8_t  | servo ID (range 0 ~ 254)         |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..4]) % 256   |

![command_0x01](images_rs485/command_0x01.png)

```
0x12 0x4c 0x01 0x01 0x00 0x60
```

**Example Explanation:**

- Check if the servo with **ID 0** is online.



### 5.3 Response

| Byte Name  | Length | Data Type | Description                      |
| ---------- | :----: | :-------: | -------------------------------- |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x05 0x1c**) |
| `cmd_id`   |   1    |  uint8_t  | Ping (**0x01**)                  |
| `length`   |   1    |  uint8_t  | 1 byte (**0x01**)                |
| `servo_id` |   1    |  uint8_t  | servo ID (range 0 ~ 254)         |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..4]) % 256   |

![response_0x01](./images_rs485/response_0x01.png)

```
0x05 0x1c 0x01 0x01 0x00 0x23
```

**Example Explanation:**

- Calculate and compare the theoretical `checksum` with the `checksum` in the response packet: If they match, then **Servo with ID 0 is online**.
- It is recommended to set a maximum wait time `timeout`. If no response is received within this time, it indicates that the servo is offline.



## 6. Single-Turn Position Control (Basic)

### 6.1 Overview

- Control the specified ID servo (or all servos) via the command to move to the **target position** (±180°) within the set **motion time**, and the **execution power** can also be set.

- Command ID: **08** (0x08)

  

### 6.2 Command

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Single-Turn Position Control (Basic) (**0x08**)              |
| `length`   |   1    |  uint8_t  | 7 bytes (**0x07**)                                           |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )<BR/>0xff represents all online servos |
| `position` |   2    |  int16_t  | Target position, **unit: 0.1°**<BR/>range : +1800 ~ -1800 (+CW / −CCW) |
| `time`     |   2    | uint16_t  | Motion time, **unit: ms**                                    |
| `power`    |   2    | uint16_t  | execution power, **unit: mW**<BR/>If `power = 0` or exceeds the `power protection value`, the execution will follow the `power protection value` |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..10]) % 256                              |

![command_0x08](images_rs485/command_0x08.png)

```
0x12 0x4c 0x08 0x07 0x00 0x84 0x03 0xf4 0x01 0x00 0x00 0xe9
```

**Example Explanation:**

- Set servo **ID 0**,
- Move to the target position of **+90°** within **500ms**,
- Configure the `power protection value` to the maximum execution power, operating at **maximum power**.



### 6.3 Response (Optional)

| Byte Name  | Length | Data Type | Description                                     |
| ---------- | :----: | :-------: | ----------------------------------------------- |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x05 0x1c**)                |
| `cmd_id`   |   1    |  uint8_t  | Single-Turn Position Control (Basic) (**0x08**) |
| `length`   |   1    |  uint8_t  | 2 bytes (**0x02**)                              |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )          |
| `result`   |   1    |  uint8_t  | **0x01:** Success execution\| **0x00:** Failure |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..5]) % 256                  |

![response_0x08](images_rs485/response_0x08.png)

```
0x05 0x1C 0x08 0x02 0x00 0x01 0x2c
```

**Example Explanation:**

- The **ID 0** servo returns a value of **0x01**, indicating **successful execution**.

> [!CAUTION]
>
> By default, no response packet is returned. A response will only be sent if the servo configuration parameter `Respond after action` is set to Yes in the PC configuration.



## 7. Single-Turn Position Control (Advanced - Time-based)

### 7.1 Overview

- Control the specified servo ID (or all servos) via command to move to the **target position** (±180°) within the set **motion time**. The **execution power** can be configured, and **acceleration/deceleration** parameters are supported to achieve trapezoidal speed profile motion.

- Command ID: **11** (0x0b)

  

### 7.2 Command

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Single-Turn Position Control (Basic) (**0x0b**)              |
| `length`   |   1    |  uint8_t  | 11 bytes (**0x0b**)                                          |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )<BR/>0xff represents all online servos |
| `position` |   2    |  int16_t  | Target position, **unit: 0.1°**<BR/>range : +1800 ~ -1800 (+CW / −CCW) |
| `time`     |   2    | uint16_t  | Motion time, **unit: ms**                                    |
| `accel`    |   2    | uint16_t  | Acceleration time, **unit: ms**                              |
| `decel`    |   2    | uint16_t  | Deceleration time, **unit: ms**                              |
| `power`    |   2    | uint16_t  | execution power, **unit: mW**<BR/>If `power = 0` or exceeds the `power protection value`, the execution will follow the `power protection value` |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..14]) % 256                              |

> [!WARNING]
>
> The acceleration and deceleration time settings **cannot be less than 20 ms**, otherwise they will not take effect.

![command_0x0b](images_rs485/command_0x0b.png)

```
0x12 0x4c 0x0b 0x0b 0x00 0x84 0x03 0x58 0x02 0x64 0x00 0xc8 0x00 0x00 0x00 0x81
```

**Example Explanation:**

-  Set servo **ID 0**,

-  Move to the target position of **+90°** within **500ms**,

-  Acceleration time: **100 ms**, deceleration time: **200 ms**,

- Configure the `power protection value` to the maximum execution power, operating at **maximum power**.

  

### 7.3 Response (Optional)

- For details, please refer to Section [6.3. Respond (Optional)](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-16).




## 8. Single-Turn Position Control (Advanced - Speed-based)

### 8.1 Overview

- Control the specified servo ID (or all servos) via command to move to the **target position** (±180°) within the set **motion speed**. The **execution power** can be configured, and **acceleration/deceleration** parameters are supported to achieve trapezoidal speed profile motion.

- Command ID: **12** (0x0b)

  

### 8.2 Command

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Single-Turn Position Control (Advanced - Speed-based) (**0x0c**) |
| `length`   |   1    |  uint8_t  | 11 bytes (**0x0b**)                                          |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )<BR/>0xff represents all online servos |
| `position` |   2    |  int16_t  | Target position, **unit: 0.1°**<BR/>range : +1800 ~ -1800 (+CW / −CCW) |
| `speed`    |   2    | uint16_t  | Motion speed, **unit: 0.1°/s**                               |
| `accel`    |   2    | uint16_t  | Acceleration time, **unit: ms**                              |
| `decel`    |   2    | uint16_t  | Deceleration time, **unit: ms**                              |
| `power`    |   2    | uint16_t  | execution power, **unit: mW**<BR/>If `power = 0` or exceeds the `power protection value`, the execution will follow the `power protection value` |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..14]) % 256                              |

> [!WARNING]
>
> The acceleration and deceleration time settings **cannot be less than 20 ms**, otherwise they will not take effect.

![command_0x0b](images_rs485/command_0x0c.png)

```
0x12 0x4c 0x0c 0x0b 0x00 0x84 0x03 0xd0 0x07 0x64 0x00 0xc8 0x00 0x00 0x00 0xff
```

**Example Explanation:**

- Set servo **ID 0**,

- Move to the target position of **+90°** at a motion speed of **200°/s**,

- Acceleration time: **100 ms**, deceleration time: **200 ms**,

- Configure the `power protection value` to the maximum execution power, operating at **maximum power**.

  

### 8.3 Response (Optional)

- For details, please refer to Section [6.3. Respond (Optional)](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-16).




## 9. Read Single-Turn Current Position

### 9.1 Overview

- Read the **current position** of the servo with a specified ID via command. The returned value represents the **single-turn current position** (±180°) of the servo. This function can be used for real-time monitoring of the servo's motion status.

- Command ID: **10** (0x0a)

  

### 9.2 Command

| Byte Name  | Length | Data Type | Description                                  |
| ---------- | :----: | :-------: | -------------------------------------------- |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)             |
| `cmd_id`   |   1    |  uint8_t  | Read Single-Turn Current Position (**0x0a**) |
| `length`   |   1    |  uint8_t  | 1 byte (**0x01**)                            |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )       |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..4]) % 256               |

![command_0x08](images_rs485/command_0x0a.png)

```
0x12 0x4c 0x0a 0x01 0x00 0x69
```

**Example Explanation:**

- Read Single-Turn Current Position of the servo with **ID 0**.



### 9.3 Response

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x05 0x1c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Read Single-Turn Current Position (**0x0a**)                 |
| `length`   |   1    |  uint8_t  | 3 bytes (**0x03**)                                           |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )                       |
| `position` |   2    |  int16_t  | Target position, **unit: 0.1°**<BR/>range : +1800 ~ -1800 (+CW / −CCW) |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..6]) % 256                               |

![response_0x08](images_rs485/response_0x0a.png)

```
0x05 0x1C 0x0a 0x03 0x00 0x86 0x03 0xb7
```

**Example Explanation:**

- The position value returned by the servo with **ID 0** is **0x86 0x03**. After unpacking, the obtained value is **+902**,
- After converting it to the angular system, it indicates that the single-turn current position of the servo is **+90.2°**.



## 10. Multi-Turn Position Control (Basic)

### 10.1 Overview

- Control the specified ID servo (or all servos) via command to move to the **target position** (±3,686,400°/1,024 turns) within the set **motion time**, and the **execution power** can also be set.

- Command ID: **13** (0x0d)

  

### 10.2 Command

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Multi-Turn Position Control (Basic) (**0x0d**)               |
| `length`   |   1    |  uint8_t  | 11 bytes (**0x0b**)                                          |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254(0x00 ~ 0xfc )<BR/>0xff represents all online servos |
| `position` |   4    |  int32_t  | Target position, unit: 0.1°<BR/>range : +3,686,400 ~ -3,686,400 (+CW / −CCW) |
| `time`     |   4    | uint32_t  | Motion time, **unit: ms**                                    |
| `power`    |   2    | uint16_t  | execution power, **unit: mW**<BR/>If `power = 0` or exceeds the `power protection value`, the execution will follow the `power protection value` |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..14]) % 256                              |

![command_0x08](images_rs485/command_0x0d.png)

```
0x12 0x4c 0x0d 0x0b 0x00 0xa0 0x0f 0x00 0x00 0x88 0x13 0x00 0x00 0x00 0x00 0xc0
```

**Example Explanation:**

- Set servo **ID 0**,


- Move to the target position of **+400°** within **5000ms**,

- Configure the `power protection value` to the maximum execution power, operating at **maximum power**.

  

### 10.3 Response (Optional)

- For details, please refer to Section [6.3. Respond (Optional)](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-16).




## 11. Multi-Turn Position Control (Advanced - Time-based)

### 11.1 Overview

- Control the specified servo ID (or all servos) via command to move to the **target position**(±3,686,400°/1,024 turns) within the set **motion time**. The **execution power** can be configured, and **acceleration/deceleration** parameters are supported to achieve trapezoidal speed profile motion.

- Command ID: **14** (0x0e)

  

### 11.2 Command

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Multi-Turn Position Control (Advanced - Time-based) (**0x0e**) |
| `length`   |   1    |  uint8_t  | 15 bytes (**0x0f**)                                          |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254(0x00 ~ 0xfc )<BR/>0xff represents all online servos |
| `position` |   4    |  int32_t  | Target position, unit: 0.1°<BR/>range : +3,686,400 ~ -3,686,400 (+CW / −CCW) |
| `time`     |   4    | uint32_t  | Motion time, **unit: ms**                                    |
| `accel`    |   2    | uint16_t  | Acceleration time, **unit: ms**                              |
| `decel`    |   2    | uint16_t  | Deceleration time, **unit: ms**                              |
| `power`    |   2    | uint16_t  | execution power, **unit: mW**<BR/>If `power = 0` or exceeds the `power protection value`, the execution will follow the `power protection value` |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..18]) % 256                              |

> [!WARNING]
>
> The acceleration and deceleration time settings **cannot be less than 20 ms**, otherwise they will not take effect.

![command_0x0e](./images_rs485/command_0x0e.png)

```
0x12 0x4c 0x0e 0x0f 0x00 0x70 0x17 0x00 0x00 0xb0 0x04 0x00 0x00 0x64 0x00 0x64 0x00 0x00 0x00 0x7e
```

**Example Explanation:**

- Set servo **ID 0**,
- Move to the target position of **+600°** within **1200ms**,
- Acceleration time: **100 ms**, deceleration time: **100 ms**,
- Configure the `power protection value` to the maximum execution power, operating at **maximum power**.



### 11.3 Response (Optional)

- For details, please refer to Section [6.3. Respond (Optional)](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-16).




## 12. Multi-Turn Position Control (Advanced - Speed-based)

### 12.1 Overview

- Control the specified servo ID (or all servos) via command to move to the **target position** (±368,640°) within the set **motion speed**. The **execution power** can be configured, and **acceleration/deceleration** parameters are supported to achieve trapezoidal speed profile motion.
- Command ID: **15** (0x0f)



### 12.2 Command

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Multi-Turn Position Control (Advanced - Speed-based) (**0x0f**) |
| `length`   |   1    |  uint8_t  | 13 bytes (**0x0d**)                                          |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )<BR/>0xff represents all online servos |
| `position` |   4    |  int32_t  | Target position, unit: 0.1°<BR/>range : +3,686,400 ~ -3,686,400 (+CW / −CCW) |
| `speed`    |   4    | uint32_t  | Motion speed, **unit: 0.1°/s**                               |
| `accel`    |   2    | uint16_t  | Acceleration time, **unit: ms**                              |
| `decel`    |   2    | uint16_t  | Deceleration time, **unit: ms**                              |
| `power`    |   2    | uint16_t  | execution power, **unit: mW**<BR/>If `power = 0` or exceeds the `power protection value`, the execution will follow the `power protection value` |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..16]) % 256                              |

> [!WARNING]
>
> The acceleration and deceleration time settings **cannot be less than 20 ms**, otherwise they will not take effect.

![command_0x0b](images_rs485/command_0x0f.PNG)

```
0x12 0x4c 0x0f 0x0d 0x00 0x70 0x17 0x00 0x00 0xd0 0x07 0x64 0x00 0x64 0x00 0x00 0x00 0xa0
```

**Example Explanation:**

- Set servo **ID 0**, 
- Move to the target position of **+600°** at a motion speed of **200°/s**,
- Acceleration time: **100 ms**, deceleration time: **100 ms**, 
- Configure the `power protection value` to the maximum execution power, operating at **maximum power**.



### 12.3 Response (Optional)

- For details, please refer to Section [6.3. Respond (Optional)](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-16).

  


## 13. Read Multi-Turn Current Position

### 13.1 Overview

- Read the **current angle** of the servo with a specified ID via command. The returned angle value represents the servo's **multi-turn current position** (±3,686,400°), along with **information on the number of turns** (±1,024 turns). This function can be utilized for real-time monitoring of the servo's motion status.
- Command ID: **16** (0x10)



### 13.2 Command

| Byte Name  | Length | Data Type | Description                                |
| ---------- | :----: | :-------: | ------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)           |
| `cmd_id`   |   1    |  uint8_t  | Read Multi-Turn Current Position(**0x10**) |
| `length`   |   1    |  uint8_t  | 1 byte (**0x01**)                          |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254(0x00 ~ 0xfc )      |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..4]) % 256             |

![command_0x08](images_rs485/command_0x10.png)

```
0x12 0x4c 0x10 0x01 0x00 0x6f
```

**Example Explanation:**

- Read Multi-Turn Current Position of the servo with **ID 0**.



### 13.3 Response

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x05 0x1c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Read Multi-Turn Current Position (**0x10**)                  |
| `length`   |   1    |  uint8_t  | 7 bytes (**0x07**)                                           |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )                       |
| `position` |   4    |  int32_t  | Target position, **unit: 0.1°**<BR/>range :+3,686,400 ~ -3,686,400 (+CW / −CCW) |
| `turns`    |   2    |  int16_t  | Lap information, **unit: turn**<BR/>range : -1024 ~ 1,024    |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..6]) % 256                               |

![response_0x08](images_rs485/response_0x10.png)

```
0x05 0x1c 0x10 0x07 0x00 0x23 0x13 0x00 0x00 0x01 0x00 0x6f
```

**Example Explanation:**

- The position value returned by the servo with ID 0 is **0x23 0x13 0x00 0x00**. After unpacking, the obtained value is **+4,899**,
- After converting it to the angular system, it indicates that the multi-turn current position of the servo is **+489.9°**,
- The circle value returned by the servo with **ID 0** is **0x10 0x00**. After unpacking, the obtained value is **1**，
- Combined with the direction of the position value returned previously, it indicates that the current number of circles of the servo is **1 positive circle**.



## 14. Stop Instructions

### 14.1 Overview

- The stop instruction is utilized for rapid halting in servo motion control. Users can select different **stop types** according to their needs. This instruction can also be applied to **restore the locking force** after stall protection is triggered, as well as to **re-establish the locking force** at the current position when the locking force has been released.
- Command ID: **24** (0x18)

### 14.2 Command

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Stop Instructions (**0x18**)                                 |
| `length`   |   1    |  uint8_t  | 4 bytes (**0x04**)                                           |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )                       |
| `mode`     |   1    |  uint8_t  | Release locking force after stopping: **0x10**<br/>Maintain locking force after stopping: **0x11**<br/>Enter damping control after stopping: **0x12** |
| `power`    |   2    | uint16_t  | execution power, **unit: mW**<BR/>If `power = 0` or exceeds the `power protection value`, the execution will follow the `power protection value` |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..7]) % 256                               |

![command_0x01](images_rs485/command_0x18.png)

```
0x12 0x4c 0x18 0x04 0x00 0x11 0x70 0x17 0x12
```

**Example Explanation:**

- Set servo with **ID 0** to enter the **"stop motion"** state,
- With the stop mode set to **0x11**, **maintaining the locking force** after stopping. The execution power is maintained at **6,000 mW** (if the set power exceeds the `power protection value`, it will be executed according to the `power protection value`).



### 14.3 Response (Optional)

- For details, please refer to Section [6.3. Respond (Optional)](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-16).



## 15. Reset Loop

### 15.1 Overview

- **Reset loop** of the servo via command, and re-record the current absolute position as the present position.
- Command ID: **17** (0x11)



### 15.2 Command

| Byte Name  | Length | Data Type | Description                            |
| ---------- | :----: | :-------: | -------------------------------------- |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)       |
| `cmd_id`   |   1    |  uint8_t  | Reset Loop (**0x11**)                  |
| `length`   |   1    |  uint8_t  | 1 byte (**0x01**)                      |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc ) |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..4]) % 256         |

> [!WARNING]
>
> The command to reset loop is only effective when the servo is in the **released state**. To ensure proper execution, it is recommended to first issue a **stop instruction** before performing the resetting loop.

![command_0x01](images_rs485/command_0x11.png)

```
0x12 0x4c 0x11 0x01 0x00 0x70
```

**Example Explanation:**

- Assuming the current position is **+489.9°**,
- Reset loop of the servo with **ID 0**, and re-record the **current absolute position** as the present position,
- If we then send a read position command, the position read will be +489.9° - 360° = **+129.9°**.



### 15.3 Response (Optional)

- For details, please refer to Section [6.3. Respond (Optional)](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-16).




## 16. Damping Control

### 16.1 Overview

- Allow the servo to adjust to different positions under the action of external forces, and enable the setting of its **execution power**.
- Command ID: **09** (0X09)



### 16.2 Command

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Damping Control (**0x09**)                                   |
| `length`   |   1    |  uint8_t  | 3 bytes (**0x03**)                                           |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )                       |
| `power`    |   2    | uint16_t  | execution power, **unit: mW**<BR/>If `power = 0` or exceeds the `power protection value`, the execution will follow the `power protection value` |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..6]) % 256                               |

> [!WARNING]
>
> The damping control command is only effective when the servo is in the **released state** or **damping state**. To ensure proper execution, it is recommended to first issue a **"Stop Instruction"** before performing damping control operations.

![](images_rs485/command_0x09.png)

```
0x12 0x4c 0x09 0x03 0x00 0xf4 0x01 0x5f
```

**Example Explanation:**

- Set the servo with **ID 0** to damping control,
- Set its execution power to **500 mW**.(If power exceeds the `power protection value`, the execution will follow the `power protection value`)



### 16.3 Response (Optional)

- For details, please refer to Section [6.3. Respond (Optional)](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-16).



## 17. Set Origin Point

### 17.1 Overview

- Set the current position as the **Origin Point** of the servo via the command.
- Command ID: **23** (0x17)



### 17.2 Command

| Byte Name  | Length | Data Type | Description                            |
| ---------- | :----: | :-------: | -------------------------------------- |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)       |
| `cmd_id`   |   1    |  uint8_t  | Set Origin Point (**0x17**)            |
| `length`   |   1    |  uint8_t  | 2 bytes (**0x02**)                     |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc ) |
| `reset`    |   1    |  uint8_t  | **0x00** (Default)                     |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..5]) % 256         |

> [!WARNING]
>
> The set origin point command is only effective when the servo is in the **released state**. To ensure proper execution, it is recommended to first issue a **"Stop Instruction"** before performing setting origin point operations.

![command_0x03](images_rs485/command_0x17.png)

```
0x12 0x4c 0x17 0x02 0x00 0x00 0x77
```

**Example Explanation:**

- Set the current position of the servo with **ID 0** as its origin point.



### 17.3 Response (Optional)

- For details, please refer to Section [6.3. Respond (Optional)](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-16).

  

## 18. Synchronous Instruction

### 18.1 Overview

- The synchronous instruction is used to simultaneously send control information for multiple servos in a single command. Each servo matches and parses the corresponding parameters based on its unique **ID**, and only executes the content relevant to itself. After all servos have received the information, they start simultaneously, achieving coordinated and synchronized movement of multiple servos.
- Command ID: **25** (0x19)



### 18.2 Command

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Synchronous Instruction (**0x19**)                           |
| `length`   |   1    |  uint8_t  | (%d*%n+3) bytes                                              |
| `cmd_id`   |   1    |  uint8_t  | **[Effective Synchronous Command](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-64)** id |
| `length`   |   1    |  uint8_t  | **[Effective Synchronous Command](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-64)** `length` : **%d** |
| `count`    |   1    |  uint8_t  | the count of servo : **%n**                                  |
| `content`  |   1    |  uint8_t  | the `content` of effective command                           |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..%d%n+6]) % 256                          |

> [!WARNING]
>
> - Synchronous Instruction are only applicable to the commands within the **[Effective Synchronous Commands](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-64)**.

![command_0x01](images_rs485/command_0x19.png)

```
0x12 0x4c 0x19 0x11 0x08 0x07 0x02 0x01 0x2c 0x01 0xe8 0x03 0x00 0x00 0x02 0x58 0x02 0xd0 0x07 0x00 0x00 0xe5
```

**Example Explanation:**

- Send **synchronous instruction** to the servos with **ID 1** and **ID 2**,
- Set the servo motor with **ID 1** to move to the target position of **+30°** within **1000ms**, configure the `power protection value` to the maximum execution power, operating at **maximum power**.
- Set the servo motor with **ID 2** to move to the target position of **+60°** within **2000ms**, configure the `power protection value` to the maximum execution power, operating at **maximum power**. 
- Both servos will execute the commands simultaneously after receiving them.



### 18.3 Effective Synchronous Command

| Command Name                                          |  Command ID   |   Length:%d   |
| ----------------------------------------------------- | :-----------: | :-----------: |
| Single-Turn Position Control (Basic)                  | **08** (0x08) | **7** (0x07)  |
| Single-Turn Position Control (Advanced - Time-based)  | **11** (0x0b) | **11** (0x0b) |
| Single-Turn Position Control (Advanced - Speed-based) | **12** (0x0c) | **11** (0x0b) |
| Multi-Turn Position Control (Basic)                   | **13** (0x0d) | **11** (0x0b) |
| Multi-Turn Position Control (Advanced - Time-based)   | **14** (0x0e) | **15** (0x0f) |
| Multi-Turn Position Control (Advanced - Speed-based)  | **15** (0x0f) | **15** (0x0f) |
| Data Monitor                                          | **22** (0x16) |               |



### 18.4 Response

- The Synchronous Instruction does not have a response packet.
- If the Effective Synchronous Command received by the servo with the corresponding **ID** has a response packet, then return the respective response data.



## 19. Asynchronous Write Instruction

### 19.1 Overview

- Asynchronous writing is composed of a combination of an **asynchronous write instruction** and a **effective synchronous command**.
- After the command is issued, the online servo will write the next **[Effective Asynchronous Command](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-64)** into its own buffer zone and execute it immediately upon receiving the **[Asynchronous Activate Instruction](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-71)**.
- Command ID: **18** (0x12)



### 19.2 Command

| Byte Name | Length | Data Type | Description                               |
| --------- | :----: | :-------: | ----------------------------------------- |
| `header`  |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)          |
| `cmd_id`  |   1    |  uint8_t  | Asynchronous Write Instruction (**0x12**) |
| `length`  |        |           |                                           |

> [!IMPORTANT]
>
> - The instruction takes effect on **all servos on the bus**, and upon receipt, the buffer zone is activated.
> - The buffer zone is only permitted to store one **[Effective Asynchronous Command](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-64)** at a time.
> - If a servo with the **same ID** receives an instruction **again**, it will be executed as a regular instruction.

![command_0x12](images_rs485/command_0x12.png)

```
0x12 0x4c 0x12 0x00 0x70
0x12 0x4c 0x08 0x07 0x00 0x84 0x03 0xf4 0x01 0x00 0x00 0xe9
```

**Example Explanation:**

- Step 1: Issue an asynchronous write instruction, and all online servos activate their buffer zones.
- Issue a control instruction with **ID 0**, and write the content into the buffer zone.
  - Set the servo motor with **ID 0** to move to the target position of **+90°** within **500ms**；
  - configure the `power protection value` to the maximum execution power, operating at **maximum power**.



### 19.3 Effective Asynchronous Command

| Command Name                                          |  Command ID   |    Length     |
| ----------------------------------------------------- | :-----------: | :-----------: |
| Single-Turn Position Control (Basic)                  | **08** (0x08) | **7** (0x07)  |
| Single-Turn Position Control (Advanced - Time-based)  | **11** (0x0b) | **11** (0x0b) |
| Single-Turn Position Control (Advanced - Speed-based) | **12** (0x0c) | **13** (0x0d) |
| Multi-Turn Position Control (Basic)                   | **13** (0x0d) | **11** (0x0b) |
| Multi-Turn Position Control (Advanced - Time-based)   | **14** (0x0e) | **15** (0x0f) |
| Multi-Turn Position Control (Advanced - Speed-based)  | **15** (0x0f) | **15** (0x0f) |



### 19.4 Response

- There is no response packet for the asynchronous write instruction.
- For the specific content of the response packet for a effective asynchronous command, please refer to [6.3. Response (Optional)](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-16).



## 20. Asynchronous Activate Instruction

### 20.1 Overview

- The asynchronous activate instruction is used to trigger the execution of commands stored in the buffer zone. Upon completion, the buffer zone is cleared and closed.
- Command ID: **19** (0x13)



### 20.2 Command

| Byte Name  | Length | Data Type | Description                                  |
| ---------- | :----: | :-------: | -------------------------------------------- |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)             |
| `cmd_id`   |   1    |  uint8_t  | Asynchronous Activate Instruction (**0x13**) |
| `length`   |   1    |  unit8_t  | 1 byte (**0x01**)                            |
| `action`   |   1    |  unit8_t  | **0x01:** Cancel \| **0x00:** Execute        |
| `checksum` |   1    |  unit8_t  | checksum = Σ(Byte[0..4]) % 256               |

> [!CAUTION]
>
> - Regardless of whether the instruction is executed or canceled, the servo buffer will be cleared and closed.
>
> - After power-off, the buffer content automatically becomes invalid.

![command_0x01](images_rs485/command_0x13.png)

```
0x12 0x4c 0x13 0x01 0x00 0x72
```

**Example Explanation:**

- Execute **[Asynchronous Activate Instruction](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-71)**, 
- Clear and close all servo registers.



### 20.3 Response

- There is **no** response packet for this instruction.

  

## 21. Read Data

### 21.1 Overview

- By sending instructions, you can **individually** obtain the working status parameters (such as voltage, current, temperature, etc.) and configuration parameters of the servo; the relevant information is returned via response data packets.
- Command ID: **03** (0x03)



### 21.2 Command

| Byte Name  | Length | Data Type | Description                                                  |
| ---------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)                             |
| `cmd_id`   |   1    |  uint8_t  | Read Data (**0x03**)                                         |
| `length`   |   1    |  uint8_t  | 2 bytes (**0x02**)                                           |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )                       |
| `data_id`  |   1    |  uint8_t  | Please refer to the [working status parameters]() and [servo configuration parameters](). |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..5]) % 256                               |

![command_0x03](images_rs485/command_0x03.png)

```
0x12 0x4c 0x03 0x02 0x00 0x03 0x66
```

**Example Explanation:**

- Read the current power of the servo with **ID 0**.



### 21.3 Response

| Byte Name      | Length | Data Type | Description                                                  |
| -------------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`       |   2    | uint16_t  | Fixed identifier (**0x05 0x1c**)                             |
| `cmd_id`       |   1    |  uint8_t  | Read Data (**0x03**)                                         |
| `length`       |   1    |  uint8_t  | 3 bytes (**0x03**)                                           |
| `servo_id`     |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )                       |
| `data_content` |  1/2   | int8/16_t | Based on the return values of the parameters read from the instructions, Please refer to the [operating status parameters](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-88) and [servo configuration parameters](https://wiki.fashionstar.com.hk/protocols#elementor-toc__heading-anchor-89). |
| `checksum`     |   1    |  uint8_t  | checksum = Σ(Byte[0..6]) % 256                               |

![response_0x03](./images_rs485/response_0x03.png)

```
0x05 0x1C 0x03 0x04 0x00 0x03 0x62 0x01 0x8e
```

**Example Explanation:**

- The power value returned by the servo with **ID 0** is **0x62 0x01**. After unpacking, the obtained value is **+354**, indicating that the current servo power is **354mW**.



## 22. Data Monitor

### 22.1 Overview

- By sending instructions, the operating status parameters (such as angle, voltage, current, temperature, etc.) of servos can be obtained **in batches**; the relevant information is returned via response data packets.
- Command ID: **22** (0x16)



### 22.2 Command

| Byte Name  | Length | Data Type | Description                            |
| ---------- | :----: | :-------: | -------------------------------------- |
| `header`   |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)       |
| `cmd_id`   |   1    |  uint8_t  | Data Monitor (**0x16**)                |
| `length`   |   1    |  uint8_t  | 1 byte (**0x01**)                      |
| `servo_id` |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc ) |
| `checksum` |   1    |  uint8_t  | checksum = Σ(Byte[0..4]) % 256         |

![command_0x01](images_rs485/command_0x16.png)

```
0x12 0x4c 0x16 0x01 0x00 0x75
```

**Example Explanation:**

- Obtain the operating status data of the servo with **ID 0**.



### 22.3 Response

| Byte Name     | Length | Data Type | Description                                                  |
| ------------- | :----: | :-------: | ------------------------------------------------------------ |
| `header`      |   2    | uint16_t  | Fixed identifier ( **0x05 0x1c** )                           |
| `cmd_id`      |   1    |  uint8_t  | Data Monitor (**0x16**)                                      |
| `length`      |   1    |  uint8_t  | 16 bytes (**0x10**)                                          |
| `servo_id`    |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )                       |
| `voltage`     |   2    | uint16_t  | Current operating voltage, **unit: mV**                      |
| `current`     |   2    | uint16_t  | Current operating current, **unit: mA**                      |
| `power`       |   2    | uint16_t  | Current operating power, **unit: mW**                        |
| `temperature` |   2    | uint16_t  | Current operating temperature, please refer to the [ADC-temperature mapping table](). |
| `status`      |   1    |  uint8_t  | Status indicator bit                                         |
| `position`    |   4    | uint32_t  | Current position, **unit: 0.1°**                             |
| `turns`       |   2    |  int16_t  | Current number of revolutions, **unit:turn**                 |
| `checksum`    |   1    |  uint8_t  | checksum = Σ(Byte[0..19]) % 256                              |

> [!TIP]
>
> It is recommended to set a maximum waiting time, `timeout`. If no response is received within this time, it indicates that the servo is not online.

![response_0x01](images_rs485/response_0x16.png)

```
0x05 0x1c 0x16 0x10 0x00 0x83 0x1e 0x1e 0x00 0xea 0x00 0x2c 0x07 0x00 0xaf 0x0b 0x00 0x00 0x00 0x00 0xdd
```

**Example Explanation:**

- By unpacking the response data of the **servo with ID 0**, the obtained operating status data is as follows:
  - ID: `0x00 = 0`
  - Voltage: `0x1e 0x83 = 7811` mV
  - Current: `0x00 0x1e = 30` mA
  - Power:`0x00 0xea = 234` mW
  - Temperature:`0x07 0x2C = 1836` adc value
  - Status:`0x00 = 0`
  - Posotion：`0x00 0x00 0x0b 0xaf = 2991` 299.1degrees
  - Turn：`0x00 0x00 = 0`



## 23. Customize Configuration Parameters

### 23.1 Overview

- Write the servo's configuration parameters via commands.
- Command ID: **04** (0x04)



### 23.2  Command

| Command        | Length | Data Type | Description                                             |
| -------------- | :----: | :-------: | ------------------------------------------------------- |
| `header`       |   2    | uint16_t  | Fixed identifier (**0x12 0x4c**)                        |
| `cmd_id`       |   1    |  uint8_t  | Customize Configuration Parameters (**0x04**)           |
| `length`       |   1    |  uint8_t  | 2 bytes (**0x02**)                                      |
| `servo_id`     |   1    |  uint8_t  | servo ID, range 0 ~ 254 (0x00 ~ 0xfc )                  |
| `data_id`      |   1    |  uint8_t  | Please refer to the [servo configuration parameters](). |
| `data_content` |   n    | int8/16_t | Please refer to the [servo configuration parameters](). |
| `checksum`     |   1    |  uint8_t  | checksum = Σ(Byte[0..n+6]) % 256                        |



### 23.3 Response (Optional)

- For details, please refer to Section[6.3. Respond (Optional)](https://wiki.fashionrobo.com/uartbasic/uart_rs485_protocols/#63).



## Appendix

### A. operating status parameters

| data_id | Parameter Name        | Data Type | Unit | Notes                                                        |
| :-----: | :-------------------- | :-------: | :--: | ------------------------------------------------------------ |
|    1    | Voltage               | uint16_t  |  mV  |                                                              |
|    2    | Current               | uint16_t  |  mA  |                                                              |
|    3    | Power                 | uint16_t  |  mW  |                                                              |
|    4    | Temperature           | uint16_t  | ADC  | Please refer to the **ADC-temperature mapping table**        |
|    5    | Status indicator bits |  uint8_t  |      | BIT[0] - Set to 1 when instruction is being executed, clear to 0 after execution is complete<BR>BIT[1] - Set to 1 for instruction execution error, clear to 0 after next correct execution<BR>BIT[2] - Set to 1 for stall protection, clear to 0 after stall is resolved<BR>BIT[3] - Set to 1 for overvoltage protection, clear to 0 after voltage returns to normal<BR>BIT[4] - Set to 1 for undervoltage protection, clear to 0 after voltage returns to normal<BR>BIT[5] - Set to 1 for overcurrent protection, clear to 0 after current returns to normal<BR>BIT[6] - Set to 1 for overpower protection, clear to 0 after power returns to normal<BR>BIT[7] - Set to 1 for overtemperature protection, clear to 0 after temperature returns to normal |

**ADC-temperature mapping table**

| Temperature(℃) | ADC  | Temperature(℃) | ADC  | Temperature(℃) | ADC  |
| :------------: | :--: | :------------: | :--: | :------------: | :--: |
|       50       | 1191 |       60       | 941  |       70       | 741  |
|       51       | 1164 |       61       | 918  |       71       | 723  |
|       52       | 1137 |       62       | 897  |       72       | 706  |
|       53       | 1110 |       63       | 876  |       73       | 689  |
|       54       | 1085 |       64       | 855  |       74       | 673  |
|       55       | 1059 |       65       | 835  |       75       | 657  |
|       56       | 1034 |       66       | 815  |       76       | 642  |
|       57       | 1010 |       67       | 796  |       77       | 627  |
|       58       | 986  |       68       | 777  |       78       | 612  |
|       59       | 963  |       69       | 759  |       79       | 598  |

### B. servo configuration parameters

| data_id | Parameter Name                   | Data Type | Unit | Notes                                                        |
| :-----: | :------------------------------- | :-------: | :--: | :----------------------------------------------------------- |
|   33    | Command Response Switch          |  uint8_t  |      | **0x00:** Do not send response packet (**default**)<br>**0x01:** Send response packet |
|   34    | Servo ID                         |  uint8_t  |      | Range 0 ~ 254                                                |
|   36    | Baud Rate Configuration          |  uint8_t  |      | 0x01 - 9,600<br>0x02 - 19,200<br>0x03 - 38,400<br>0x04 - 57,600<br>**0x05 - 115,200 (default)**<br>0x06 - 250,000<br>0x07 - 500,000<br>0x08 - 1,000,000 |
|   37    | Stall Protection Switch          |  uint8_t  |      | When the servo operates beyond the `Power Protection Value`<br>**0x00:** (Stall protection OFF) Reduce output to the power protection value (**default**)<br>**0x01:** (Stall protection ON) Release holding torque |
|   38    | Stall Power Upper Limit          | uint16_t  |  mW  |                                                              |
|   39    | Voltage Protection Lower Limit   | uint16_t  |  mV  |                                                              |
|   40    | Voltage Protection Upper Limit   | uint16_t  |  mV  |                                                              |
|   41    | Temperature Protection Threshold | uint16_t  | ADC  |                                                              |
|   42    | Power Protection Value           | uint16_t  |  mW  |                                                              |
|   43    | Current Protection Value         | uint16_t  |  mA  |                                                              |
|   46    | Power‑On Holding Torque Switch   |  uint8_t  |      | **0x00:** Release torque (**default**)<br>**0x01:** Maintain torque |
|   48    | Angle Limit Switch               |  uint8_t  |      | **0x00:** Off (**default**)<br>**0x01:** On                  |
|   49    | Power‑On Soft‑Start Switch       |  uint8_t  |      | **0x00:** Off (**default**)<br>**0x01:** On                  |
|   50    | Power‑On Soft‑Start Time         | uint16_t  |  ms  |                                                              |
|   51    | Servo Angle Upper Limit          |  int16_t  | 0.1° |                                                              |
|   52    | Servo Angle Lower Limit          |  int16_t  | 0.1° |                                                              |
