# UART Bus Servo SDK User Manual (STM32F103)

## 1.Overview

This SDK provides STM32F103 API functions based on the [UART bus servo communication protocol](https://wiki.fashionstar.com.hk/protocols), It applies to all Fashion Star UART bus servo models.

### 1.1 PC Configuration Tool

The PC configuration tool can be used to debug bus servos and test their functions.

- PC Configuration Tool: [FashionStar UART Bus Servo PC Software](https://wiki.fashionstar.com.hk/download/1094/?tmstv=1765252343)

- User guide: [Bus Servo PC Software Manual](https://wiki.fashionstar.com.hk/pc-configuration-user-manual)

### 1.2 SDK

Example projects and APIs mentioned in this document can be downloaded here:

- STM32F103 SDK download link: [SDK for STM32F103](https://wiki.fashionstar.com.hk/download/1318/?tmstv=1765252679)

### 1.3 Development Tools

The UC-01 bus servo adapter board uses a `CH340` USB-to-TTL chip. You need to install its driver on Windows. [Check if the driver is installed correctly](https://jingyan.baidu.com/article/00a07f3872a90982d028dcb9.html)

+ keil5: [keil5下载链接](https://fashionrobo.com/wp-content/uploads/download/keil5.zip)
+ ST-Link driver: [ST-Link driver download link](https://fashionrobo.com/wp-content/uploads/download/STLinkV2.zip)
+ Serial debug assistant: [XCOM V2.2 download link](https://www.amobbs.com/forum.php?mod=attachment&aid=NDQxNzc5fDE5NzMzYjQ1fDE1NzY2NTQ4NTN8MHw1NzAzODMz)
+ USB-to-TTL driver: [CH340 driver download link](https://fashionrobo.com/wp-content/uploads/download/CH341SER.zip)

### 1.4 Illustrations

HP8-U45-M UART bus servo<img src="./images/u45-slide-01.png" style="zoom: 50%;" />

STM32 all-in-one main control board

<img src="./images/1.3.png" style="zoom: 33%;" />

`UC-01` bus servo adapter board

<img src="./images/1.4.png" style="zoom:50%;" />

STM32F103C8T6

<img src="./images/1.5.png" style="zoom:33%;" />



## 2.Wiring Instructions

### 2.1 Hardware Preparation

| Name                                   | Description                                                  | Notes                                                        |
| -------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Bus servo                              | All models share the same communication protocol.            |                                                              |
| UC-01 bus servo adapter board          | Provides the servo’s required **power interface** and **communication interface** | Required                                                     |
| STM32F103C8T6 dev board                | Used for MCU programming.                                    | Any dev board with the same MCU can be used.                 |
| PC                                     | Used for software development and printing debug logs.       |                                                              |
| ST-Link/v2                             | STM32 on-chip programmer / debugger                          | Other STM32 programmers/debuggers are also fine.             |
| USB-to-TTL module (optional)           | Connects PC and STM32 UART, used to print debug logs.        | Optional; mainly used for logging during development.        |
| STM32 all-in-one main board (optional) | Integrates both UC-01 and STM32F103C8T6 functions.           | Can directly replace the UC-01 + STM32F103C8T6 dev board combo. |

- For beginners, we recommend using the STM32 all-in-one main control board. It integrates the **UC-01 bus servo adapter board** and **STM32F103C8T6**, and exposes commonly used interfaces to significantly shorten development time.
- Using the **UC-01** together with an **STM32F103C8T6** dev board is more flexible for different environments.

### 2.2 Wiring STM32 to ST-Link V2

Use ST-Link V2 to download firmware to the STM32.

- STM32 ↔ ST-Link V2 wiring

| STM32       | STLinkV2 |
| ----------- | -------- |
| SWIO / IO   | SWDIO    |
| SWCLK / CLK | SWCLK    |
| GND         | GND      |
| 3V3         | 3.3v     |

![img](images/wW1fYSVX62cHDzg.jpg)

### 2.3 Hardware Wiring

The STM32F103 has three UART peripherals: UART1, UART2, and UART3. In this SDK, they are used as follows:

* `UART1` Connected to the UC-01 bus servo adapter board, used to control bus servos
* `UART2` Connected to a USB-to-TTL module for logging (optional)
* `UART3`Not used

**Wiring to the bus servo**

UART1 is connected to the TTL port of the UC-01 and used to control bus servos.

> [!NOTE]
>
> If using the **PTC-32** development board, you can use it directly without needing to set jumpers.

- STM32 ↔ UC-01 wiring

| STM32F103 GPIO    | UC-01 bus servo adapter |
| ----------------- | ----------------------- |
| PA_9   (UART1 Tx) | Rx                      |
| PA_10 (UART1 Rx)  | Tx                      |
| 5v                | 5v                      |
| GND               | GND                     |

![images-20210421174433503](images/PoXZktuvmW57Y9L.png)

![images-20210421174418516](images/ysrDXAGb52NcnzR.png)

**STM32 ↔ USB-to-TTL module (optional)**

UART2 on the STM32 is connected to the USB-to-TTL module, which sends log data to the PC.

- STM32 ↔ USB-to-TTL wiring


| STM32F103 GPIO  | USB-to-TTL module |
| --------------- | ----------------- |
| PA_2 (UART2 Tx) | Rx                |
| PA_3 (UART2 Rx) | Tx                |
| GND             | GND               |

The USB port of the USB-to-TTL module connects to a USB port on the PC.

![w](images/QzSpn52ZBRq7Afj.png)

### 2.4 Illustrations

<img src="./images/1.png" alt="1" style="zoom:67%;" />

![](./images/2.png)



## 3.Development Environment Setup

### 3.1.KEIL5 Configuration

Steps for configuring the software:

1. Download and install KEIL5 and the STM32F1 device pack.
2. Download the SDK and unzip it: **fashionstar-uart-servo-stm32f103-master**
3. Open the STM32 example project with KEIL5 (using the “communication check” example as reference).
    Project path:

```
fashionstar-uart-servo-stm32f103-master\UART总线伺服舵机STM32F103 SDK使用手册\2.1.舵机通讯检测\源代码\FashionStarUartServo\Project\FashionStarUartServo.uvprojx
```

![](./images/5.png)

![](./images/6.png)

Choose compiler: **Use default compiler version 5**

![](./images/7.png)

 

![](./images/8.png)

Select the actual debugger you are using. In this example, we use ST-Link.

![](./images/9.png)

### 3.2 Build and Download Firmware

![](./images/10.png)

Build the project and check the output.

![](./images/11.png)

Connect ST-Link to the PC via USB. Download the firmware to the STM32.

![](./images/12.png)

Press the **reset** button on the STM32 dev board. The STM32 will start executing the newly-programmed firmware.

<img src=".\images\reset.png" style="zoom: 50%;" />

### 3.3 Extra – Project Structure Overview

**Project structure**

* `Project` 

  KEIL5 project files. Double-click `FashionStarUartServo.uvprojx` to open.

* `User`

  Main program and user-defined libraries

  * `main.c` : User main program
  * User-defined libraries (for example: Servo driver library, etc.)

* `Libraries` 

  * `CMSIS`：ARM CM3 core support files from ARM
  * `FWLIB`：STM32 standard peripheral library

- `Listings`: This directory is the MDK-generated information output directory, storing code distribution files (.map and .lst).
- `Output`: This directory is the MDK-generated information output directory, storing object files (.o), debugging files (.axf), download files (.hex), dependency files (.d), etc.

**User-defined library files**

Overview of the User directory:

* `sys_tick` 

  Manages system time. Uses SysTick interrupts for delay and countdown logic.

* `ring_buffer` 

  A ring-buffer queue implemented in C. Used to store/manage UART data streams, and supports reading/writing various data types.

* `usart`

  UART communication library. Via macros you can enable/disable the three USART resources on the STM32F103C8 dev board.

* `fashion_star_uart_servo` 

  Encapsulates the `Fashion Star` bus servo communication protocol. This is the STM32F103-side SDK for bus servos.

* `main.c`

  Main program entry.

`User` directory tree:

```c
├── main.c
└── usart        //UART communication
    ├── usart.c
    └── usart.h
├── ring_buffer //Ring-buffer driver library
│   ├── ring_buffer.c
│   └── ring_buffer.h
├── sys_tick　 //System tick
│   ├── sys_tick.c
│   └── sys_tick.h
├── fashion_star_uart_servo //Code Prototype
│   ├── fashion_star_uart_servo.c
│   └── fashion_star_uart_servo.h
├── fashion_star_uart_servo //Example Code(Based on Prototype)
│   ├── fashion_star_uart_servo_examples.c
│   └── fashion_star_uart_servo_examples.h
```



## 4. Ping

### 4.1 Ping

To check whether a servo is online, use the `Ping` command.

- If a servo with that ID exists and is online, it will send a response packet after receiving the `Ping` command.

- If the servo ID does not exist or the servo is offline, no response packet will be received.

<img src="./images/3.1.png" alt="3.1" style="zoom: 33%;" />

**Code Prototype**

```C
FSUS_STATUS FSUS_Ping(Usart_DataTypeDef *usart, uint8_t servo_id);
```

- `usart` : Pointer to the UART data object used for servo control`Usart_DataTypeDef`
- `servo_id` 

**Usage example**

The Ping function `FSUS_Ping` takes the UART data structure pointer `servoUsart` and the servo ID `servoId`:

```c
statusCode = FSUS_Ping(servoUsart, servoId);
```

`statusCode` is of type `FSUS_STATUS`. If the request succeeds, it returns `0`. Any other value indicates a communication failure. You can check `fashion_star_uart_servo.h` for the meaning of each status code.

```C
// FSUS status codes
#define FSUS_STATUS uint8_t
#define FSUS_STATUS_SUCCESS 0               // Set/read success
#define FSUS_STATUS_FAIL 1                  // Set/read failure
#define FSUS_STATUS_TIMEOUT 2               // Wait timeout
#define FSUS_STATUS_WRONG_RESPONSE_HEADER 3 // Wrong response header
#define FSUS_STATUS_UNKOWN_CMD_ID 4         // Unknown control command
#define FSUS_STATUS_SIZE_TOO_BIG 5          // Parameter size exceeds the limit in FSUS_PACK_RESPONSE_MAX_SIZE
#define FSUS_STATUS_CHECKSUM_ERROR 6        // Checksum error
#define FSUS_STATUS_ID_NOT_MATCH 7          // Requested servo ID does not match the feedback servo ID
```

### 4.2 Example – Check if Servo is Online

**Function description**

Continuously sends a `Ping` command to `servo ID 0` and prints log messages on the logging UART according to the response.

**Example code**

```c
#include "fashion_star_uart_servo_examples.h"
#include "math.h"

// Use UART1 as the servo control port
// <Wiring Instructions>
// STM32F103 PA9(Tx)    <----> Servo Transceiver Board Rx
// STM32F103 PA10(Rx)   <----> Servo Transceiver Board Tx
// STM32F103 GND        <----> Servo Transceiver Board GND
// STM32F103 V5         <----> Servo Transceiver Board 5V
// <Notes>
// Make sure USART1_ENABLE is set to 1 in usart.h before use
Usart_DataTypeDef* servo_usart = &usart1; 

// Use UART2 as the logging output port
// <Wiring Instructions>
// STM32F103 PA2(Tx) <----> USB-TTL Rx
// STM32F103 PA3(Rx) <----> USB-TTL Tx
// STM32F103 GND     <----> USB-TTL GND
// STM32F103 V5      <----> USB-TTL 5V (optional)
Usart_DataTypeDef* logging_usart = &usart2;


// Redirect C library function printf to UART, after redirection you can use printf function
int fputc(int ch, FILE *f)
{
    while((logging_usart->pUSARTx->SR&0X40)==0){}
    /* Send one byte of data to UART */
    USART_SendData(logging_usart->pUSARTx, (uint8_t) ch);
    /* Wait for transmission to complete */
    // while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);       
    return (ch);
}


/* Servo Communication Test */
void FSUSExample_PingServo(void)
{

	FSUS_STATUS status_code; // Status code
	uint8_t servo_id = 0;	 // Servo ID = 0

	printf("===Test Uart Servo Ping===r\n");
	while (1)
	{
		// Servo communication test
		status_code = FSUS_Ping(servo_usart, servo_id);
		if (status_code == FSUS_STATUS_SUCCESS)
		{
			printf("Servo Online \r\n");
		}
		else
		{
			printf("Servo Offline,Error Code=%d \r\n", status_code);
		}
		// Delay for 1s
		SysTick_DelayMs(1000);
	}
}
```



## 5.Single-Turn Position Control

> [!NOTE]
>
> - The servo only responds to the latest angle control command.
>   If you need multiple commands in sequence, use delays or read the current angle to check whether the previous action has finished.
>
> - When continuously sending commands to the same servo, we recommend a command interval of at least `10 ms`.
>
> - If `power = 0` or power is greater than the holding power value, the servo uses the holding power value. The holding power value can be configured in the **PC configuration tool**.
>
> - Maximum achievable speed depends on servo model and load.

### 5.1 Single-Turn Position Control (Basic)

<img src="./images/5_1.png" style="zoom:33%;" />

**Code Prototype**

```c
FSUS_STATUS FSUS_SetServoAngle(Usart_DataTypeDef *usart, uint8_t servo_id, float angle, uint16_t interval, uint16_t power, uint8_t wait);
```

* `usart`: UART data object for servo control`Usart_DataTypeDef`
* `servo_id`: Servo ID
* `angle`: Target angle in degrees, resolution 0.1°, range [-180.0, 180.0]
* `interval`: Motion duration in `ms`; minimum > 100
* `power`: Servo drive power in mV; default 0

### 5.2 Single-Turn Position Control (Advanced-Time-based)

<img src="./images/5_2.png" style="zoom: 33%;" />

**Code Prototype**

```c
FSUS_STATUS FSUS_SetServoAngleByInterval(Usart_DataTypeDef *usart, uint8_t servo_id, \
                float angle, uint16_t interval, uint16_t t_acc, \
                uint16_t t_dec, uint16_t  power, uint8_t wait);
```

- `usart`: UART data object for servo control`Usart_DataTypeDef`
- `servo_id`: Servo ID
- `angle`: Target angle in degrees, resolution 0.1°, range [-180.0, 180.0]
- `interval`: Motion duration in `ms`; Must satisfy interval > `t_acc + t_dec`, and must be > `100`
- `t_acc`: The time for the servo to accelerate from startup to constant speed (ms), with a minimum value > 20.
- `t_dec`: The deceleration time of the servo when approaching the target position (ms), with a minimum value > 20.
- `power`: Servo drive power in mV; default 0

### 5.3 Single-Turn Position Control (Advanced-Speed-based)

<img src="./images/5_3.png" style="zoom: 33%;" />

**Code Prototype**

```c
FSUS_STATUS FSUS_SetServoAngleByVelocity(Usart_DataTypeDef *usart, uint8_t servo_id, \
                float angle, float velocity, uint16_t t_acc, \
                uint16_t t_dec, uint16_t  power, uint8_t wait);
```

* `usart`: UART data object for servo control`Usart_DataTypeDef`
* `servo_id`: Servo ID
* `angle`: Target angle in degrees, resolution 0.1°, range [-180.0, 180.0]
* `velocity`: Target rotational speed of the servo, in degrees per second (°/s), with a value range of [1, 750].
* `t_acc`: The time for the servo to accelerate from startup to constant speed (ms), with a minimum value > 20.
* `t_dec`: The deceleration time of the servo when approaching the target position (ms), with a minimum value > 20.
* `power`: Servo drive power in mV; default 0

### 5.4 Read Single-Turn Current Position

**Code Prototype**

```c
// Query the angle information of a single servo angle unit degree
FSUS_STATUS FSUS_QueryServoAngle(Usart_DataTypeDef *usart, uint8_t servo_id, float *angle);
```

* `usart` : UART data object for servo control`Usart_DataTypeDef`
* `servo_id`: Servo ID
* `angle` :Output pointer for current single-turn angle

### 5.5 Example--Single Servo

**Function description**

Test the servo's position control, demonstrating three types of APIs for position control. After executing each position control command, the current position query API is called to obtain the real-time position.

- Single-Turn Position Control (Basic) + Read Single-Turn Current Position
- Single-Turn Position Control (Advanced-Time-based) + Read Single-Turn Current Position
- Single-Turn Position Control (Advanced-Speed-based) + Read Single-Turn Current Position

**Example Code**

```c
/* Control Single Servo Angle */
void FSUSExample_SetServoAngle(void)
{
	// Servo control related parameters
	// Servo ID number
	uint8_t servo_id = 0;
	// Target angle for the servo
	// Servo angle range is -180 to 180 degrees, minimum unit 0.1
	float angle = 0;
	// Time interval in ms
	// You can try setting a smaller time interval, e.g. 500ms
	uint16_t interval;
	// Target speed
	float velocity;
	// Acceleration time
	uint16_t t_acc;
	// Deceleration time
	uint16_t t_dec;
	// Servo operating power in mV, default is 0
	uint16_t power = 0;
	// Read angle
	float angle_read;

	while (1)
	{
		printf("GOTO: 135.0f\r\n");
        // Simple angle control + current angle query
        angle = 135.0;
        interval = 2000;
        FSUS_SetServoAngle(servo_usart, servo_id, angle, interval, power);
        FSUS_QueryServoAngle(servo_usart, servo_id, &angle_read);
        printf("Cur Angle: %.1f\r\n", angle_read);

        // Wait for 2.5s
        SysTick_DelayMs(2500);

        // Angle control with acceleration/deceleration (specified period) + current angle query
        printf("GOTO+Interval: 0.0f\r\n");
        angle = 0.0f;
        interval = 1000;
        t_acc = 100;
        t_dec = 150;
        FSUS_SetServoAngleByInterval(servo_usart, servo_id, angle, interval, t_acc, t_dec, power);
        FSUS_QueryServoAngle(servo_usart, servo_id, &angle_read);
        printf("Cur Angle: %.1f\r\n", angle_read);

        // Wait for 2s
        SysTick_DelayMs(2000);

        // Angle control with acceleration/deceleration (specified speed) + current angle query
        printf("GOTO+Velocity: -135.0f\r\n");
        angle = -135.0f;
        velocity = 200.0f;
        t_acc = 100;
        t_dec = 150;
        FSUS_SetServoAngleByVelocity(servo_usart, servo_id, angle, velocity, t_acc, t_dec, power);
        FSUS_QueryServoAngle(servo_usart, servo_id, &angle_read);
        printf("Cur Angle: %.1f\r\n", angle_read);
				
				// Wait for 3s
        SysTick_DelayMs(3000);
	}
}
```

**Example log**

```
GOTO: 135.0f
Cur Angle: 134.7
GOTO+Interval: 0.0f
Cur Angle: 0.3
GOTO+Velocity: -135.0f
Cur Angle: -134.6
```

### 5.6 Example – Multiple Servos

**Function description**

Shows how to control multiple servos with `Single-Turn Position Control(Basic)` commands.

**Example Code**

```c
/* Control Multiple Servo Angles */
void FSUSExample_SetNServoAngle(void)
{
	//// Servo control related parameters
	// Time interval in ms
	// You can try setting a smaller time interval, e.g. 500ms
	uint16_t interval = 2000;
	// Servo operating power in mV, default is 0
	uint16_t power = 0;

	while (1)
	{
		// Simple angle control command, control servos 0 and 1
        FSUS_SetServoAngle(servo_usart, 0, 90.0, interval, power);
        FSUS_SetServoAngle(servo_usart, 1, 45.0, interval, power);
				
        // Wait for action to complete
        SysTick_DelayMs(interval);

        // Wait for 1s
        SysTick_DelayMs(1000);

        // Simple angle control command, control servos 0 and 1
        FSUS_SetServoAngle(servo_usart, 0, -90.0, interval, power);
        FSUS_SetServoAngle(servo_usart, 1, -45.0, interval, power);
        // Wait for action to complete
        SysTick_DelayMs(interval);

        // Wait for 1s
        SysTick_DelayMs(1000);
	}
}
```



## 6. Multi-Turn Position Control

> [!NOTE]
>
> - The servo only responds to the latest position control command. When multiple consecutive position control commands need to be executed, a delay can be used in the program or the current position can be read to determine whether the previous command has been completed.
> - It is recommended that the interval between consecutive commands sent to the same servo be more than 10 ms.
> - If the `power = 0` or greater than the power hold value, the operation will be performed according to the power hold value. The power hold value can be set via the PC Configuration Tool.
> - The maximum rotational speed of the servo varies depending on the servo model and load conditions.

### 6.1 Multi-Turn Position Control (Basic)  
<img src="./images/6_1.png" style="zoom: 33%;" />

**Code Prototype**

```c
FSUS_STATUS FSUS_SetServoAngleMTurn(Usart_DataTypeDef *usart, uint8_t servo_id, float angle, \
			uint32_t interval, uint16_t power, uint8_t wait);
```

* `usart`: UART data object for servo control`Usart_DataTypeDef`
* `servo_id`: Servo ID
* `angle`: Target angle in degrees, resolution 0.1°, range [-180.0, 180.0]
* `interval`: Motion duration in `ms`; minimum > 100
* `power`: Servo drive power in mV; default 0

### 6.2 Multi-Turn Position Control (Advanced-Time-based)
<img src="./images/6_2.png" style="zoom:33%;" />

**Code Prototype**

```c
FSUS_STATUS FSUS_SetServoAngleMTurnByInterval(Usart_DataTypeDef *usart, uint8_t servo_id, float angle, \
			uint32_t interval,  uint16_t t_acc,  uint16_t t_dec, uint16_t power, uint8_t wait);
```

* `usart`: UART data object for servo control`Usart_DataTypeDef`
* `servo_id`: Servo ID
* `angle`: Target angle in degrees, resolution 0.1°, range [-368,640.0° ,  368,640.0°]
* `interval`: Motion duration in `ms`; Must satisfy interval > `t_acc + t_dec`, and must be > `100`
* `t_acc`: The time for the servo to accelerate from startup to constant speed (ms), with a minimum value > 20.
* `t_dec`: The deceleration time of the servo when approaching the target position (ms), with a minimum value > 20.
* `power`: Servo drive power in mV; default 0

### 6.3 Multi-Turn Position Control (Advanced-Speed-based)

![](./images/6_3.png)

**Code Prototype**

```c
FSUS_STATUS FSUS_SetServoAngleMTurnByVelocity(Usart_DataTypeDef *usart, uint8_t servo_id, float angle, \
			float velocity, uint16_t t_acc,  uint16_t t_dec, uint16_t power, uint8_t wait);
```

* `usart`: UART data object for servo control`Usart_DataTypeDef`
* `servo_id`: Servo ID
* `angle`: Target angle in degrees, resolution 0.1°, range [-180.0, 180.0]
* `velocity`: Target rotational speed of the servo, in degrees per second (°/s), with a value range of [-368,640.0° ,  368,640.0°].
* `t_acc`: The time for the servo to accelerate from startup to constant speed (ms), with a minimum value > 20.
* `t_dec`: The deceleration time of the servo when approaching the target position (ms), with a minimum value > 20.
* `power`: Servo drive power in mV; default 0

### 6.4 Read Multi-Turn Current Position

**Code Prototype**

```c
FSUS_STATUS FSUS_QueryServoAngleMTurn(Usart_DataTypeDef *usart, uint8_t servo_id, float *angle);
```

* `usart` : UART data object for servo control`Usart_DataTypeDef`

* `servo_id`: Servo ID
* `angle` :Output pointer for current single-turn angle

### 6.5 Reset Loop

**Code Prototype**

```C
FSUS_STATUS FSUS_ServoAngleReset(Usart_DataTypeDef *usart, uint8_t servo_id);
```

* `usart`: UART data object for servo`Usart_DataTypeDef`
* `servo_id`: Servo ID

**Usage Example**

```C
uint8_t servoId = 0;    // servo_id
FSUS_ServoAngleReset(servoUsart, servoId); // Reset Loop
```

> [!CAUTION]
>
> Reset Loop must be used in the torque-released state.

### 6.6 Example

**Function description**

The routine demonstrates the usage of APIs for multi-turn position control and real-time multi-turn position query.

- Multi-Turn Position Control (Basic) + Read Multi-Turn Current Position

- Multi-Turn Position Control (Advanced-Time-based) + Read Multi-Turn Current Position

- Multi-Turn Position Control (Advanced-Speed-based) + Read Multi-Turn Current Position

**Example Code**

```c
/* Set Servo Angle (Multi-turn Mode) */
void FSUSExample_SetServoAngleMTurn(void)
{
	//// Servo control related parameters
	// Servo ID number
	uint8_t servo_id = 0;
	// Target angle for the servo
	// Servo angle range is -180 to 180 degrees, minimum unit 0.1
	float angle;
	uint32_t interval; // Time interval in ms
	float velocity;	   // Motor speed, in dps (degrees per second)
	// Servo operating power in mV, default is 0
	uint16_t power = 0;
	// Acceleration time (in ms)
	uint16_t t_acc;
	// Deceleration time
	uint16_t t_dec;
	// Read angle
	float angle_read;

	while (1)
	{
		printf("MTurn GOTO: 720.0f\r\n");
        // Simple multi-turn angle control + current multi-turn angle query
        angle = 720.0f;
        interval = 2000;
        FSUS_SetServoAngleMTurn(servo_usart, servo_id, angle, interval, power);
        FSUS_QueryServoAngleMTurn(servo_usart, servo_id, &angle_read);
        printf("Cur Angle: %.1f\r\n", angle_read);

        // Wait for 4s
        SysTick_DelayMs(4000);

			
        printf("MTurn GOTO: 0.0f\r\n");
        angle = 0.0;
        FSUS_SetServoAngleMTurn(servo_usart, servo_id, angle, interval, power);
        FSUS_QueryServoAngleMTurn(servo_usart, servo_id, &angle_read);
        printf("Cur Angle: %.1f\r\n", angle_read);

        // Wait for 3s
        SysTick_DelayMs(3000);


        // Multi-turn angle control with acceleration/deceleration (specified period) + current multi-turn angle query
        printf("MTurn+Interval GOTO: -180.0f\r\n");
        angle = 180.0f; 
        interval = 1000;
        t_acc = 100;
        t_dec = 200;
        FSUS_SetServoAngleMTurnByInterval(servo_usart, servo_id, angle, interval, t_acc, t_dec, power);
        FSUS_QueryServoAngleMTurn(servo_usart, servo_id, &angle_read);
        printf("Cur Angle: %.1f\r\n", angle_read);

        // Wait for 2s
        SysTick_DelayMs(2000);

        // Multi-turn angle control with acceleration/deceleration (specified speed) + current multi-turn angle query
        printf("MTurn+Velocity GOTO: -180.0f\r\n");
        angle = -180.0f;
        velocity = 100.0f;
        t_acc = 100;
        t_dec = 200;
        FSUS_SetServoAngleMTurnByVelocity(servo_usart, servo_id, angle, velocity, t_acc, t_dec, power);
        FSUS_QueryServoAngleMTurn(servo_usart, servo_id, &angle_read);
        printf("Cur Angle: %.1f\r\n", angle_read);

        // Wait for 4s
        SysTick_DelayMs(4000);
	}
}
```

**Example log**

```
MTurn GOTO: 720.0f
Cur Angle: 719.7
MTurn GOTO: 0.0f
Cur Angle: 0.4
MTurn+Interval GOTO: -180.0f
Cur Angle: 179.7
MTurn+Velocity GOTO: -180.0f
Cur Angle: -179.5
MTurn GOTO: 720.0f
Cur Angle: 719.5
MTurn GOTO: 0.0f
Cur Angle: 0.4
MTurn+Interval GOTO: -180.0f
Cur Angle: 179.7
MTurn+Velocity GOTO: -180.0f
Cur Angle: -179.5
```



## 7. Damping Control

### 7.1 Set the damping control and configure the power

**Code Prototype**

```c
/* Servo damping mode */
FSUS_STATUS FSUS_DampingMode(Usart_DataTypeDef *usart, uint8_t servo_id, uint16_t power);
```

* `usart`: UART data object for servo control`Usart_DataTypeDef`
* `servo_id`: Servo ID
* `power`: Servo drive power in mV; default 0

### 7.2 Example--Setting Power and Position Feedback

**Function description**

**Set different power** levels to experience changes in the servo's damping force; **request the servo position** simultaneously. When the servo is rotating, update its position at regular intervals. Serial Port 2 prints the servo position information at regular intervals.

**Example Code**

```c
/* Servo Damping Mode and Angle Feedback */
void FSUSExample_SetServoDamping(void)
{
	FSUS_STATUS status_code; // Status code for request packet
	uint8_t servo_id = 0;	 // Servo ID number connected to the transceiver board
	uint16_t power = 500;	 // Power in damping mode, higher power means more resistance
	float angle = 0;		 // Servo angle

	// Set servo to damping mode
	FSUS_DampingMode(servo_usart, servo_id, power);
	while (1)
	{
		// Read the servo angle
		status_code = FSUS_QueryServoAngle(servo_usart, servo_id, &angle);

		if (status_code == FSUS_STATUS_SUCCESS)
		{
			// Successfully read the servo angle
			printf("[INFO] servo id= %d ; angle = %f\r\n", servo_id, angle);
		}
		else
		{
			// Failed to read the servo angle
			printf("\r\n[INFO] read servo %d angle, status code: %d \r\n", servo_id, status_code);
			printf("[ERROR]failed to read servo angle\r\n");
		}
		// Wait for 1000ms
		SysTick_DelayMs(500);
	}
}
```



## 8.Synchronous Instruction

### 8.1 Control servos with synchronous instructions

**Code Prototype**

```c
FSUS_STATUS FSUS_SyncCommand(Usart_DataTypeDef *usart, uint8_t servo_count, uint8_t ServoMode, FSUS_sync_servo servoSync[])；
```

* `usart`: UART data object for servo control`Usart_DataTypeDef`
* `servo_count`: Number of servos
* `servomode`: Synchronous instruction mode selection
* `servoSync[]`: Servo control parameter structure array

### 8.2 Example

**Function description**

Control all servos simultaneously with high real-time performance.

**Example Code**

```c
/* Synchronous Command Control */
void FSUSExample_SYNC(void)
{
	/* Synchronous command mode selection
* 1: Set servo angle
* 2: Set servo angle (specified period)
* 3: Set servo angle (specified speed)
* 4: Set servo angle (multi-turn mode)
* 5: Set servo angle (multi-turn mode, specified period) 
* 6: Set servo angle (multi-turn mode, specified speed)
* 7: Read servo data*/
uint8_t sync_mode=1;// Synchronous command mode

uint8_t sync_count=5;// Number of servos

	while(1)
	{
		SyncArray[0].angle=90;
		SyncArray[0].id=0;SyncArray[0].interval_single=300;SyncArray[0].interval_multi=1000;SyncArray[0].velocity=100;SyncArray[0].t_acc=100;SyncArray[0].t_dec=100;
		SyncArray[1].angle=-90;
		SyncArray[1].id=1;SyncArray[1].interval_single=300;SyncArray[1].interval_multi=1000;SyncArray[1].velocity=100;SyncArray[1].t_acc=100;SyncArray[1].t_dec=100;
		SyncArray[2].angle=90;
		SyncArray[2].id=2;SyncArray[2].interval_single=300;SyncArray[2].interval_multi=1000;SyncArray[2].velocity=100;SyncArray[2].t_acc=100;SyncArray[2].t_dec=100;
		SyncArray[3].angle=-90;
		SyncArray[3].id=3;SyncArray[3].interval_single=300;SyncArray[3].interval_multi=1000;SyncArray[3].velocity=100;SyncArray[3].t_acc=100;SyncArray[3].t_dec=100;
		SyncArray[4].angle=-90;
		SyncArray[4].id=4;SyncArray[4].interval_single=300;SyncArray[4].interval_multi=1000;SyncArray[4].velocity=100;SyncArray[4].t_acc=100;SyncArray[4].t_dec=100;
		// Send synchronous command control
		FSUS_SyncCommand(servo_usart,sync_count,sync_mode,SyncArray);
		SysTick_DelayMs(1000);
		// Send synchronous command read
		FSUS_SyncCommand(servo_usart,sync_count,7,SyncArray);
		SysTick_DelayMs(200);

		SyncArray[0].angle=45;SyncArray[0].interval_single=300;SyncArray[0].velocity=20;
		SyncArray[1].angle=-45;SyncArray[1].interval_single=300;SyncArray[1].velocity=20;
		SyncArray[2].angle=45;SyncArray[2].interval_single=300;SyncArray[2].velocity=20;
		SyncArray[3].angle=-45;SyncArray[3].interval_single=300;SyncArray[3].velocity=20;
		SyncArray[4].angle=-45;SyncArray[4].interval_single=300;SyncArray[4].velocity=20;
		// Send synchronous command control
		FSUS_SyncCommand(servo_usart,sync_count,sync_mode,SyncArray);
		SysTick_DelayMs(1000);
		// Send synchronous command read
		FSUS_SyncCommand(servo_usart,sync_count,7,SyncArray);
		SysTick_DelayMs(200);
	}
}

/* Data Monitoring - Read Servo Parameters */
void FSUSExample_MONTIOR(void)
{
	/* Data monitoring data
* id: Servo ID number
* voltage: Servo voltage
* current: Servo current
* power: Servo operating power
* temperature: Servo temperature 
* status: Servo status
* angle: Servo angle
* circle_count: Servo rotation count*/
ServoData servodata_single[1];// Read data for one servo

// Servo ID number to read
uint8_t servo_id=0;
	
	FSUS_DampingMode(servo_usart,servo_id,500);
	while(1)
	{
			FSUS_ServoMonitor(servo_usart,servo_id,servodata_single);
			printf("read ID: %d\r\n", servodata_single[0].id);
			printf("read sucess, voltage: %d mV\r\n", servodata_single[0].voltage);
			printf("read sucess, current: %d mA\r\n", servodata_single[0].current);
			printf("read sucess, power: %d mW\r\n", servodata_single[0].power);
			printf("read sucess, temperature: %d \r\n", servodata_single[0].temperature);
			if ((servodata_single[0].status >> 3) & 0x01)
			printf("read sucess, voltage too high\r\n");
			if ((servodata_single[0].status >> 4) & 0x01)
			printf("read sucess, voltage too low\r\n");
			printf("read sucess, angle: %f\r\n", servodata_single[0].angle);
			printf("read sucess, circle_count: %d\r\n", servodata_single[0].circle_count);
			SysTick_DelayMs(1000);
	}
}
```



## 9.Data Monitor

### 9.1 Data Monitor

**Code Prototype**

```c
FSUS_STATUS FSUS_ServoMonitor(Usart_DataTypeDef *usart, uint8_t servo_id, ServoData servodata[]);
```

* `usart`: UART data object for servo control`Usart_DataTypeDef`
* `servo_id`: Servo ID
* `servodata[]`: Servo storage data structure array

### 9.2 Example

**Function description**

Read all parameters of the servos

**Example Code**

```c
/* Data Monitoring - Read Servo Parameters */
void FSUSExample_MONTIOR(void)
{
	/* Data monitoring data
* id: Servo ID number
* voltage: Servo voltage
* current: Servo current
* power: Servo operating power
* temperature: Servo temperature 
* status: Servo status
* angle: Servo angle
* circle_count: Servo rotation count*/
ServoData servodata_single[1];// Read data for one servo

// Servo ID number to read
uint8_t servo_id=0;
	
	FSUS_DampingMode(servo_usart,servo_id,500);
	while(1)
	{
			FSUS_ServoMonitor(servo_usart,servo_id,servodata_single);
			printf("read ID: %d\r\n", servodata_single[0].id);
			printf("read sucess, voltage: %d mV\r\n", servodata_single[0].voltage);
			printf("read sucess, current: %d mA\r\n", servodata_single[0].current);
			printf("read sucess, power: %d mW\r\n", servodata_single[0].power);
			printf("read sucess, temperature: %d \r\n", servodata_single[0].temperature);
			if ((servodata_single[0].status >> 3) & 0x01)
			printf("read sucess, voltage too high\r\n");
			if ((servodata_single[0].status >> 4) & 0x01)
			printf("read sucess, voltage too low\r\n");
			printf("read sucess, angle: %f\r\n", servodata_single[0].angle);
			printf("read sucess, circle_count: %d\r\n", servodata_single[0].circle_count);
			SysTick_DelayMs(1000);
	}
}
```



## 10.Read Data

### 10.1 Read Data

**Code Prototype**

```c
// Read Data
FSUS_STATUS FSUS_ReadData(Usart_DataTypeDef *usart, uint8_t servoId,  uint8_t address, uint8_t *value, uint8_t *size);
```

* `usart`: UART data object for servo control`Usart_DataTypeDef`
* `servo_id`: Servo ID
* `address` 只读参数或自定义参数地址
* `value` 读取到的数据存放指针
* `size` 读取到的数据的长度存放指针

**Example Code**

```c
/* Read Servo Status */
void FSUSExample_ReadData(void)
{
	uint8_t servo_id = 0;	// Servo ID number connected to the transceiver board
	FSUS_STATUS statusCode; // Status code

	// Data bytes length in the data table is generally 1 byte/2 bytes/4 bytes
	// According to the communication protocol, the servo angle upper limit data type is signed short integer (UShort, corresponding to int16_t in STM32), length is 2 bytes
	// So set the value data type to int16_t here
	int16_t value;
	uint8_t dataSize;
	// When passing parameters, cast the pointer of value to uint8_t

	// Read voltage
	statusCode = FSUS_ReadData(servo_usart, servo_id, FSUS_PARAM_VOLTAGE, (uint8_t *)&value, &dataSize);

	printf("read ID: %d\r\n", servo_id);

	if (statusCode == FSUS_STATUS_SUCCESS)
	{
		printf("read sucess, voltage: %d mV\r\n", value);
	}
	else
	{
		printf("fail\r\n");
	}

	// Read current
	statusCode = FSUS_ReadData(servo_usart, servo_id, FSUS_PARAM_CURRENT, (uint8_t *)&value, &dataSize);
	if (statusCode == FSUS_STATUS_SUCCESS)
	{
		printf("read sucess, current: %d mA\r\n", value);
	}
	else
	{
		printf("fail\r\n");
	}

	// Read power
	statusCode = FSUS_ReadData(servo_usart, servo_id, FSUS_PARAM_POWER, (uint8_t *)&value, &dataSize);
	if (statusCode == FSUS_STATUS_SUCCESS)
	{
		printf("read sucess, power: %d mW\r\n", value);
	}
	else
	{
		printf("fail\r\n");
	}
	// Read temperature
	statusCode = FSUS_ReadData(servo_usart, servo_id, FSUS_PARAM_TEMPRATURE, (uint8_t *)&value, &dataSize);
	if (statusCode == FSUS_STATUS_SUCCESS)
	{
		double temperature, temp;
		temp = (double)value;
		temperature = 1 / (log(temp / (4096.0f - temp)) / 3435.0f + 1 / (273.15 + 25)) - 273.15;
		printf("read sucess, temperature: %f\r\n", temperature);
	}
	else
	{
		printf("fail\r\n");
	}
	// Read working status
	statusCode = FSUS_ReadData(servo_usart, servo_id, FSUS_PARAM_SERVO_STATUS, (uint8_t *)&value, &dataSize);
	if (statusCode == FSUS_STATUS_SUCCESS)
	{
		// Servo working status flags
		// BIT[0] - Command execution flag, set to 1 when executing, cleared after completion.
		// BIT[1] - Command execution error flag, cleared after next correct execution.
		// BIT[2] - Stall error flag, cleared after stall is resolved.
		// BIT[3] - Overvoltage flag, cleared when voltage returns to normal.
		// BIT[4] - Undervoltage flag, cleared when voltage returns to normal.
		// BIT[5] - Current error flag, cleared when current returns to normal.
		// BIT[6] - Power error flag, cleared when power returns to normal.
		// BIT[7] - Temperature error flag, cleared when temperature returns to normal.

		if ((value >> 3) & 0x01)
			printf("read sucess, voltage too high\r\n");
		if ((value >> 4) & 0x01)
			printf("read sucess, voltage too low\r\n");
	}
	else
	{
		printf("fail\r\n");
	}
	printf("================================= \r\n");

	// Infinite loop
	while (1)
	{
	}
}
```

### 10.2 Write Custom Parameters

</td></tr></table><table><tr><td bgcolor=#DDDDDD>

It is recommended to use the PC configuration tool to write custom parameters.

</td></tr></table>

**Function Prototype**

```c
// 写入数据
FSUS_STATUS FSUS_WriteData(Usart_DataTypeDef *usart, uint8_t servoId, uint8_t address, uint8_t *value, uint8_t size);
```

* `usart`: UART data object corresponding to servo control `Usart_DataTypeDef`
* `servoId`: Servo ID
* `address`: Custom parameter address
* `value`: Pointer to the data to be written
* `size`: Length of the data to be written

**使用示例**

```c
uint8_t servoId = 0;  		// 连接在转接板上的总线伺服舵机ID号
float angleLimitLow = -90.0; 	// 舵机角度下限设定值
value = (int16_t)(angleLimitLow*10); // 舵机角度下限 转换单位为0.1度
statusCode = FSUS_WriteData(servoUsart, servoId, FSUS_PARAM_ANGLE_LIMIT_LOW, (uint8_t *)&value, 2);
```

### 10.3 Reset Servo Custom Parameters

**Function Prototype**

```c
FSUS_STATUS FSUS_ResetUserData(Usart_DataTypeDef *usart, uint8_t servoId);
```

* `usart`: UART data object corresponding to servo control `Usart_DataTypeDef`
* `servoId`: Servo ID

**使用示例**

```c
uint8_t servoId = 0;  		// 连接在转接板上的总线伺服舵机ID号
FSUS_ResetUserData(servoUsart, servoId);
```



**Function Description**

读取舵机的实时状态，并且给出了判断工作状态异常的示例

- 电压
- 电流
- 功率
- 温度
- 工作状态标志位

**Example Log**

```C
read ID: 0                                      //舵机id
read success, voltage: 8905 mv                 //当前电压
read success, current: 0 ma                    //当前电流
read success, power: 0 mw                      //当前功率
read success, temperature: 32.240993           //当前温度
read success, voltage too high                 //如果当前电压超过舵机参数设置的舵机高压保护值，可以读到标志位
```



## 12. Stop Command

</td></tr></table><table><tr><td bgcolor=#DDDDDD>

**Notes:**

- In the torque-released state, the servo will still respond to commands.

</td></tr></table>

**Function Prototype**

```c
FSUS_STATUS FSUS_StopOnControlMode(Usart_DataTypeDef *usart, uint8_t servo_id, uint8_t mode, uint16_t power)；
```

* `usart`: UART data object corresponding to servo control `Usart_DataTypeDef`
* `servo_id` 舵机的ID
* `mode` 舵机停止指令编号
* `power` 舵机的功率  单位mW

**使用示例**

```c
/* 舵机控制模式停止指令*/
//mode 指令停止形式
//0-停止后卸力(失锁)
//1-停止后保持锁力
//2-停止后进入阻尼状态
uint8_t stopcolmode=0;
uint8_t servo_id = 0; 	// 连接在转接板上的总线伺服舵机ID号
uint16_t power = 500;  //功率
FSUS_StopOnControlMode(servoUsart, servo_id, stopcolmode, power);
```

### 12.1 Example – Enter Damping Mode After Command Execution



**Function Description**

Enter damping mode after executing the control command.



**源代码**

```c
/********************************************************
* 控制舵机执行完指令进入阻尼状态
 ********************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)    <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx)   <----> 总线伺服舵机转接板 Tx
// STM32F103 GND        <----> 总线伺服舵机转接板 GND
// STM32F103 V5         <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
Usart_DataTypeDef* servo_usart = &usart1; 

// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND     <----> USB转TTL GND
// STM32F103 V5      <----> USB转TTL 5V (可选)
Usart_DataTypeDef* logging_usart = &usart2;

// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
    while((logging_usart->pUSARTx->SR&0X40)==0){}
    /* 发送一个字节数据到串口 */
    USART_SendData(logging_usart->pUSARTx, (uint8_t) ch);
    /* 等待发送完毕 */
    // while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);       
    return (ch);
}


//0-停止后卸力(失锁)
//1-停止后保持锁力
//2-停止后进入阻尼状态
uint8_t stopcolmode=0;
	
float	angle = 135.0;// 舵机的目标角度
uint16_t interval = 1000;// 时间间隔ms
uint16_t	power = 500;// 舵机执行功率
uint8_t servo_id=0;// 舵机的ID号

int main (void)
{
    // 嘀嗒定时器初始化
    SysTick_Init();
    // 串口初始化
    Usart_Init();

  	FSUS_SetServoAngle(servo_usart, servo_id, angle, interval, power);
	SysTick_DelayMs(2000);
	
	//停止后进入对应状态
	FSUS_StopOnControlMode(servo_usart, servo_id, stopcolmode, power);
	SysTick_DelayMs(1000);
    while (1){
			
  }
}
```



## 13. Origin Point Setting

</td></tr></table><table><tr><td bgcolor=#DDDDDD>

**注意事项**：

- Applicable only to brushless magnetic encoder servos.
- This API must be used in the torque-released state.

</td></tr></table>

**Function Prototype**

```C
FSUS_STATUS FSUS_SetOriginPoint(Usart_DataTypeDef *usart, uint8_t servo_id);
```

* `usart`: UART data object corresponding to servo control `Usart_DataTypeDef`

* `servo_id` 舵机的ID

**使用示例**

```C
uint8_t servoId = 0;    // 舵机的ID号
FSUS_SetOriginPoint(servoUsart, servoId); // 设置当前舵机角度为原点
```



## 14. Asynchronous Commands

### 14.1 Asynchronous Write

**Function Prototype**

```c
FSUS_STATUS FSUS_BeginAsync(Usart_DataTypeDef *usart)；
```

* `usart`: UART data object corresponding to servo control `Usart_DataTypeDef`

**使用示例**

```c
FSUS_BeginAsync(servo_usart);
```

### 14.2 Asynchronous Execute

**Function Prototype**

```c
FSUS_STATUS FSUS_EndAsync(Usart_DataTypeDef *usart,uint8_t mode)；
```

* `usart`: UART data object corresponding to servo control `Usart_DataTypeDef`
* `mode` 舵机执行方式

**使用示例**

```c
uint8_t async_mode=0; //0:执行存储的命令  1:取消存储的命令
FSUS_EndAsync(servo_usart,async_mode);
```

### 14.3 Example – Asynchronous Command

**Function Description**

Store a command and execute it only when the asynchronous execute command is received next time.

**源代码**

```c
/********************************************************
 * 存储一次命令，在下次发送命令的时候才执行 
 ********************************************************/
#include "stm32f10x.h"
#include "usart.h"
#include "sys_tick.h"
#include "fashion_star_uart_servo.h"

// 使用串口1作为舵机控制的端口
// <接线说明>
// STM32F103 PA9(Tx)    <----> 总线伺服舵机转接板 Rx
// STM32F103 PA10(Rx)   <----> 总线伺服舵机转接板 Tx
// STM32F103 GND        <----> 总线伺服舵机转接板 GND
// STM32F103 V5         <----> 总线伺服舵机转接板 5V
// <注意事项>
// 使用前确保已设置usart.h里面的USART1_ENABLE为1
Usart_DataTypeDef* servo_usart = &usart1; 

// 使用串口2作为日志输出的端口
// <接线说明>
// STM32F103 PA2(Tx) <----> USB转TTL Rx
// STM32F103 PA3(Rx) <----> USB转TTL Tx
// STM32F103 GND     <----> USB转TTL GND
// STM32F103 V5      <----> USB转TTL 5V (可选)
Usart_DataTypeDef* logging_usart = &usart2;



// 重定向c库函数printf到串口，重定向后可使用printf函数
int fputc(int ch, FILE *f)
{
    while((logging_usart->pUSARTx->SR&0X40)==0){}
    /* 发送一个字节数据到串口 */
    USART_SendData(logging_usart->pUSARTx, (uint8_t) ch);
    /* 等待发送完毕 */
    // while (USART_GetFlagStatus(USART1, USART_FLAG_TC) != SET);       
    return (ch);
}


#define ID 0 // 舵机的ID号
float angle;           //舵机角度设置
float angle_read;			 // 读取的角度
uint16_t power = 1000; // 舵机执行功率 单位mV 默认为0
uint16_t interval = 0; // 舵机旋转的周期

uint8_t async_mode=0; //0:执行存储的命令  1:取消存储的命令

int main (void)
{
    // 嘀嗒定时器初始化
    SysTick_Init();
    // 串口初始化
    Usart_Init();

    while (1){
			
    //异步写入
		FSUS_BeginAsync(servo_usart);
	
		printf("GOTO: 135.0f\r\n");
    // 简易角度控制 + 当前角度查询
    angle = 135.0;
    interval = 2000;
    FSUS_SetServoAngle(servo_usart, ID, angle, interval, power);
    FSUS_QueryServoAngle(servo_usart, ID, &angle_read);
    printf("Cur Angle: %.1f\r\n", angle_read);
		
		printf("*******************\n");
		
	//第一次发送上面的命令是不会动的，只是存储了命令
	//等待5秒
		SysTick_DelayMs(5000);
		
		//异步执行
		FSUS_EndAsync(servo_usart,async_mode);
  }
}
```





## Appendix 1 - Read-Only Parameter Table

| address | 参数<br/>名称<br/>(en) | 参数<br/>名称<br/>(cn) | 字节<br/>类型 | 字节<br/>长度 | 说明                                                         | 单位 |
| :-----: | ---------------------- | ---------------------- | ------------- | ------------- | ------------------------------------------------------------ | ---- |
|    1    | voltage                | 舵机电压               | uint16_t      | 2             |                                                              | mV   |
|    2    | current                | 舵机电流               | uint16_t      | 2             |                                                              | mA   |
|    3    | power                  | 舵机功率               | uint16_t      | 2             |                                                              | mW   |
|    4    | temprature             | 舵机温度               | uint16_t      | 2             |                                                              | ADC  |
|    5    | servo_status           | 舵机工作状态           | uint8_t       | 1             | BIT[0] - 执行指令置1，执行完成后清零。<br>BIT[1] - 执行指令错误置1，在下次正确执行后清零。<br>BIT[2] - 堵转错误置1，解除堵转后清零。<br>BIT[3] - 电压过高置1，电压恢复正常后清零。<br>BIT[4] - 电压过低置1，电压恢复正常后清零。<br>BIT[5] - 电流错误置1，电流恢复正常后清零。<br>BIT[6] - 功率错误置1，功率恢复正常后清零。<br>BIT[7] - 温度错误置1，温度恢复正常后清零。 |      |
|    6    | servo_type             | 舵机型号               | uint16_t      | 2             |                                                              |      |
|    7    | firmware_version       | 舵机固件版本           | uint16_t      | 2             |                                                              |      |
|    8    | serial_number          | 舵机序列号             | uint32_t      | 4             | 舵机序列号(serial_number)并不是舵机ID，它是舵机的唯一识别符。 |      |

------

## Appendix 2 - Custom Parameter Table

| address | 参数<br/>名称<br/>(en) | 参数<br/>名称<br/>(cn) | 字节<br>类型 | 字节<br/>长度 | 说明                                                         | 单位  |
| :-----: | ---------------------- | ---------------------- | ------------ | ------------- | ------------------------------------------------------------ | ----- |
|   32    |                        | <预留>                 | uint8_t      |               |                                                              |       |
|   33    | response_switch        | 响应开关               | uint8_t      | 1             | 0 - 舵机控制指令执行可以被中断，新的指令覆盖旧的指令，无反馈数据 <br>1 - 舵机控制指令不可以被中断，指令执行结束之后发送反馈数据 |       |
|   34    | servo_id               | 舵机ID                 | uint8_t      | 1             | 舵机的ID号初始默认设置为0。修改此值可以修改舵机的ID号        |       |
|   35    |                        | <预留>                 | uint8_t      |               |                                                              |       |
|   36    | baudrate               | 波特率选项             | uint8_t      | 1             | 1 - 9600<br>2 - 19200<br>3 - 38400<br>4 - 57600<br>5 - 115200<br>6 - 250000<br>7 - 500000<br>8 - 1000000 |       |
|   37    | stall_protect_mode     | 舵机堵转保护模式       | uint8_t      | 1             | 0 - 将舵机功率降低到功率上限<br>1 - 释放舵机锁力（舵机卸力） |       |
|   38    | stall_power_limit      | 舵机堵转功率上限       | uint16_t     | 2             |                                                              | mW    |
|   39    | over_volt_low          | 舵机电压下限           | uint16_t     | 2             |                                                              | mV    |
|   40    | over_volt_high         | 舵机电压上限           | uint16_t     | 2             |                                                              | mV    |
|   41    | over_temprature        | 温度上限               | uint16_t     | 2             | 见附表3                                                      | ADC   |
|   42    | over_power             | 功率上限               | uint16_t     | 2             |                                                              | mW    |
|   43    | over_current           | 电流上限               | uint16_t     | 2             |                                                              | mA    |
|   44    | accel_switch           | 加速度处理开关         | uint8_t      | 1             | 舵机目前必须设置启用加速度处理，即只能设置0x01这个选项。     |       |
|   45    |                        | <预留>                 | uint8_t      | 1             |                                                              |       |
|   46    | po_lock_switch         | 舵机上电锁力开关       | uint8_t      | 1             | 0 - 上电舵机释放锁力<br>1 - 上电舵机保持锁力                 |       |
|   47    | wb_lock_switch         | 轮式刹车锁力开关       | uint8_t      | 1             | 0 - 停止时释放舵机锁力<br>1 - 停止时保持舵机锁力             |       |
|   48    | angle_limit_switch     | 角度限制开关           | uint8_t      | 1             | 0 - 关闭角度限制<br>1 - 开启角度限制                         |       |
|   49    | soft_start_switch      | 上电首次缓慢执行       | uint8_t      | 1             | 0 - 关闭上电首次缓慢执行<br>1 - 开启上电首次缓慢执行         |       |
|   50    | soft_start_time        | 上电首次执行时间       | uint16_t     | 2             |                                                              | ms    |
|   51    | angle_limit_high       | 舵机角度上限           | int16_t      | 2             |                                                              | 0.1度 |
|   52    | angle_limit_low        | 舵机角度下限           | int16_t      | 2             |                                                              | 0.1度 |
|   53    | angle_mid_offset       | 舵机中位角度偏移       | int16_t      | 2             |                                                              | 0.1度 |

------

## Appendix 3 - Temperature ADC Conversion Table

Temperature is represented as ADC values and needs to be converted.

![](./images/ADC.png)

The following is the temperature/ADC reference table for 50–79°C.


| 温度(℃) | ADC  | 温度(℃) | ADC  | 温度(℃) | ADC  |
| :-----: | :--: | :-----: | :--: | :-----: | :--: |
|   50    | 1191 |   60    | 941  |   70    | 741  |
|   51    | 1164 |   61    | 918  |   71    | 723  |
|   52    | 1137 |   62    | 897  |   72    | 706  |
|   53    | 1110 |   63    | 876  |   73    | 689  |
|   54    | 1085 |   64    | 855  |   74    | 673  |
|   55    | 1059 |   65    | 835  |   75    | 657  |
|   56    | 1034 |   66    | 815  |   76    | 642  |
|   57    | 1010 |   67    | 796  |   77    | 627  |
|   58    | 986  |   68    | 777  |   78    | 612  |
|   59    | 963  |   69    | 759  |   79    | 598  |

