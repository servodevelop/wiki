# Bus Servo PC configuration tool User Manual

## 1. Software Introduction

This software is a bus servo PC configuration tool used for ID configuration, Parameter setting, real-time motion control, and other functions. It is suitable for development, debugging, and teaching demonstration scenarios.



## 2. Download and Run

-   [Click to Download](https://fashionrobo.com/wp-content/uploads/download/Develop-US_1.0.9.266.rar) the latest PC configuration tool software (1.0.9.266).
    
-   Extract it to any directory, no installation required, simply double-click `Develop.exe` to start the software.
    
- If blocked by the system or an error occurs, refer to the [Startup Troubleshooting Guide](https://wiki.fashionrobo.com/dbsppc/software-install/#2).


![](./assets_EN/上位机布局.png)



## 3. Servo Connection and Identification

### 3.1 Physical Wiring Instructions

Connection order:

1.  Connect the servo to the adapter board (any port is fine);
2.  Turn on the external power supply (voltage range as per servo
    specifications);
3.  Connect the adapter board to the computer via USB cable.

> [!NOTE]
>
> - For first-time use, it is recommended to connect only one servo (default ID is 0);
> - If connecting multiple servos in series, ensure each servo is assigned a unique ID to avoid conflicts.

![](./assets_EN/物理连线.png)

### 3.2 UART Connection

-   After opening the software, click the **Refresh **button in the upper left corner to refresh the COM port list;
-   Select the automatically detected adapter board port (e.g., COM10);
-   Click the **Toggle** button and configure serial communication parameters;
-   Click **OK** to create the connection.

> [!NOTE]
>
> If the COM port is not shown, it may be due to Driver issues. Please install the [CH340 Driver](https://www.wch.cn/downloads/CH341SER_EXE.html).

![](./assets_EN/串口连接.png)

### 3.3 Servo Scanning

-   Manually set the baud rate or select **Auto Scanning**;

-   After scanning, the detected number of servos will be displayed;

    ![](./assets_EN/扫描.png)

-   To increase scan speed, go to "Tools \> Program Settings >ServoPanel" and reduce the Maximum Scan Number (default is 254).
    
    ![](./assets_EN/提高扫描.png)

#### Common Troubleshooting:

| Issue                         | Possible Cause                                               |
| ----------------------------- | ------------------------------------------------------------ |
| Servo not detected            | Power not connected, insufficient voltage, low battery       |
| Software freeze / no response | Duplicate servo IDs, connect servos one by one and set unique IDs |



## 4. Basic Servo Operations

### 4.1 Change Servo ID

-   Select the target servo from the list;
-   Click the **Write ID** icon;
-   Enter the new ID, click **OK**, and the ID will be updated in
    real-time.

![](./assets_EN/修改舵机ID.png)

### 4.2 Change Baud Rate

-   Select the servo, click the **Write Baud** icon;
-   Choose the new baud rate, click **OK**;
-   The servo will immediately apply the new communication speed.

![](./assets_EN/修改波特率.png)

### 4.3 Set Origin

-   Select the target servo, click the **Set Origin Point** icon;
-   Choose to set the current angle as Origin Position or restore factory default;
-   Re-scan the servo to confirm Origin Position setup success.

> [!NOTE]
>
> **Only magnetic encoder series support this feature** (model number includes `-M`).

![](./assets_EN/原点设置.png)



## 5. Parameter Adjustment

### 5.1 Parameter Modification Process

-   Switch to the 【**Parameters** 】tab, current parameters are shown on the left, modification area on the right;
-   Select the target servo from the list;
-   Adjust values via dropdown or slider;
-   Changed Parameters appear in orange, click **Write Parameters** to turn green (indicating successful write).

![](./assets_EN/修改参数.png)

### 5.2 Basic Parameter Description

| Parameter        | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| Command Response | Default **No**: new commands interrupt current commands. **Yes**: new commands execute only after current command completes |
| Stall Protection | Releases torque when power exceeds threshold                 |
| Power Protection | When stall protection is off, power exceeding threshold runs at stall power limit |

### 5.3 Internal Parameter Description

| Parameter       | Description                                                  |
| --------------- | ------------------------------------------------------------ |
| Servo Direction | Default clockwise forward, counterclockwise reverse (top view) |
| PID Adjustment  | Refer to [PID Adjustment Guide](https://fashionrobo.com/pid/28072/) |



## 6. Real-Time Motion Control

### 6.1 Single-Turn Position Control Mode

-   Set target angle (default range -180° \~ +180°);
-   Set motion by time interval or speed (min acceleration/deceleration 20ms);
-   Power default **0** (max power), adjustable as needed;
-   Enable "**Real-Time**" to dynamically adjust angle with slider;
-   Stop modes: Free Mode, Lock Mode, damping; set **Power** and
    click **Stop** to send.

> [!NOTE]
>
> Consider servo's mechanical and physical limits when setting angles.

![](./assets_EN/单圈角度控制.png)

### 6.2 Multi-Turn Position Control Mode

-   Control range up to ±1024 turns (\~368,640°);
-   **Update Turns** to view current accumulated turns;
-   **Reset Turns** sets current turns to zero (Origin Position unchanged);
-   Control method same as single-turn mode.

> [!NOTE]
>
> Only supported on servos with magnetic encoders.

![](./assets_EN/多圈角度控制.png)

### 6.3 Damping Mode

-   Set power to adjust damping strength (e.g., set to 500 to feel increased resistance when rotating manually).

![](./assets_EN/阻尼模式.png)

------------------------------------------------------------------------

## 7. UART Monitor

### 7.1 Enable Monitor

-   Switch to the **Serial Monitor** tab;
-   If missing, click the gear icon, enable "**Auto Star**",restart software.

![](./assets_EN/打开串行端口监视器.png)

### 7.2 Data Send Example

Example: send single-turn command to servo ID 2 from 0° to 90°:

``` text
0x12 0x4c 0x08 0x07 0x02 0x84 0x03 0xf4 0x01 0x00 0x00 0xeb
```

For details, see [Bus Servo Communication Protocol](https://wiki.fashionrobo.com/uartbasic/uart-protocol/).

![](./assets_EN/发送数据包.png)

### 7.3 Data Monitoring Example

Example: equivalent single-turn command sent from control panel to servo ID 2 from 0° to 90°:

![](./assets_EN/等效.png)



## 8. Appendix & FAQ

### 8.1 FAQ

| Issue                 | Suggested Solution                           |
| --------------------- | -------------------------------------------- |
| COM port not detected | Check CH340 Driver, change USB port or cable |
| Servo no response     | Check power, voltage, COM connection         |
| Software crash/freeze | Ensure unique servo IDs                      |

### 8.2 Resources

-   [PC configuration tool software Download](https://fashionrobo.com/wp-content/uploads/download/Develop-US_1.0.9.266.rar)
-   [CH340 Driver Download](https://www.wch.cn/downloads/CH341SER_EXE.html)
-   [Bus Servo Communication Protocol](https://wiki.fashionstar.com.hk/protocols)
