# U35H Serial Bus Servo Specifications

{% include-markdown "snippets/uart_servo/specs_example.md" start="<!--start:version_intro-->"  end="<!--end:version_intro-->" %}

<div class="fs-buy-grid" markdown="1">

<div class="fs-buy-card" markdown="1">
<img src="https://store.fashionstar.com.hk/wp-content/uploads/2025/09/RA8-U35H-M-1536x1536.webp" alt="RA8-U35H-M">
<div class="fs-product-name">RA8-U35H-M</div>
</div>

<div class="fs-buy-card" markdown="1">
<img src="https://store.fashionstar.com.hk/wp-content/uploads/2025/09/HA8-U35H-M-1536x1536.webp" alt="HA8-U35H-M">
<div class="fs-product-name">HA8-U35H-M</div>
</div>
</div>

---

## Product Features

- Integrated design of brushed motor, gearbox, position encoder, and controller
- UART communication protocol, baud rate up to 1 Mbps
- 12-bit absolute position encoder; supports setting any angle as the origin
- Supports arbitrary angle control within ±368,640°
- Power-off angle memory; angle data is retained after power loss
- Built-in trapezoidal accel/decel control for smooth motion profiles
- Automatically detects power thresholds and reduces to a safe power level during operation
- Three stop modes: hold lock, release lock, damping control
- Integrated five-layer protection: temperature, voltage, stall, power, and current
- Provides a visual Master / PC Software tool and supports firmware upgrades

## Model Definition

![Product naming - model rules](./images/产品命名-型号规则.png)

| Appearance   | Motor Type  | Size              | Communication Protocol  | Voltage   | Position Sensor                         |
| ------------ | ----------- | ----------------- | ----------------------- | --------- | --------------------------------------- |
| R: Dual-shaft | X: Brushless | 6: 31.5×21×27.6mm | U: UART/TTL             | [-]: 7.4V | [-]: Potentiometer                      |
| H: Single-shaft | P: Coreless | 8: 40×20×40mm     | S: Distributed Serial Bus | H: 12V  | M: Absolute position encoder (magnetic) |
|              | A/L: Iron-core | 18: 63×34×47mm    | R: RS-485               | W: 24V    |                                         |
|              |             |                   | A: PWM (Servo parameters adjustable) |           |                                         |
|              |             |                   | C: CAN                  |           |                                         |
|              |             |                   | P: PWM                  |           |                                         |

**Ordering Model**

- **RA8-U35H-M|HA8-U35H-M**

## Product Specifications

### Basic Parameters

| Parameter                 | Specification                          |
| ------------------------- | -------------------------------------- |
| **Operating Voltage**     | 9.0-12.6v                              |
| **Motor Type**            | Iron-core motor                        |
| **Position Sensor**       | 12-bit non-contact absolute encoder (magnetic) |
| **Effective Angle (Travel Range)** | ±180° (single-turn angle)     |
| **Resolution**            | 2048 steps/360° (0.176°)               |
| **Processor**             | 32-bit MCU                             |
| **Communication Type**    | UART/TTL half-duplex                   |
| **Baud Rate**             | 9,600bps~1Mbps                         |
| **ID Range**              | 0~254                                  |
| **Gear Ratio**            | 378:1                                  |
| **Output Spline Spec**    | Aluminum / Ø6mm / 25T                  |
| **Gear Material**         | Full metal copper-aluminum combination |
| **Connector Type**        | PH2.0-3Pin                             |
| **Housing Material**      | Aluminum alloy mid-frame / upper and lower engineering plastic shells |
| **Size**                  | 40×20×40mm                             |
| **Weight**                | 53g                                    |
| **Operating Temperature** | -10~60℃                                |
| **Operating Mode**        | Single-turn angle                      |

### Performance Parameters

| Parameter                 | Specification (12V)    |
| ------------------------ | ---------------------- |
| Max static torque (stall) | 3.43N·m (35kg-cm)      |
| Max dynamic torque        | 1.27N·m (13kg-cm)      |
| Rated torque              | 0.54N·m (5.5kg-cm)     |
| Rated speed               | 16rpm (0.625sec@60°)   |
| No-load speed             | 34rpm (0.298sec@60°)   |
| No-load current           | ＜200mA                |
| Standby current           | ＜30mA                 |
| Peak current              | 3A                     |
| Axial load                | 20N                    |
| Radial load               | 40N                    |

### Performance Curves

![U35 performance curve](./images/U35特性曲线.png)

### Overload Curve

![U35 overload curve](./images/U35过载曲线.png)

## Drawings and Installation

### Dimensions

![U35 3D drawing](./images/U35_3D图.png)

### Connector Definition

![U35](./images/U35.png)

### Wiring

**Series**

![U35 series wiring](./images/U35串联.png)

**Parallel**

![U35 parallel wiring](./images/U35并联.png)

### Installation

- **Single-shaft**

  ![U35 single-shaft installation](./images/U35单轴安装.png)

- **Dual-shaft**

![U35 dual-shaft installation](./images/U35双轴安装.png)

## Development and Compatibility

The Bus Servo series uses a unified hardware platform and system architecture, fully balancing diversity and flexibility. Different models are fully compatible and uniformly support standard protocols and control instructions, significantly simplifying system integration and development.

To accelerate deployment, we provide a complete SDK (Software Development Kit) with abundant sample code, drivers, and detailed technical documentation, supporting multiple mainstream development environments and programming languages. See the table below for support details.

Visit the official website www.fashionrobo.com for more technical resources.

![development environment](./images/development environment.png)

## Protection Functions

- All protection parameters can be set and modified through Master / PC Software.
- Status flag definitions: 1 indicates protection active; 0 indicates normal operation.

![protection](./images/protection.png)

> [!WARNING]
> Any parameter changes may damage the product or affect normal operation. Proceed with caution and ensure potential risks are fully evaluated before making changes.

### Temperature Protection

- Set the `temperature protection` parameter through Master / PC Software. Protection triggers when the range is exceeded.
- Factory default protection temperature is 70℃.
- When temperature protection is triggered, the Servo automatically switches to low power to maintain basic motion.
- You can check the corresponding servo status flag [bit7] to determine whether temperature protection is active.
- When the temperature drops to 10℃ below the configured protection value, the Servo automatically resumes normal power operation, and the corresponding flag is reset to 0.

### Voltage Protection

- Set the `high voltage protection` and `low voltage protection` parameters through Master / PC Software. Protection triggers when the range is exceeded.
- Factory default operating voltages:

  - 7.4V version: 6.0-8.4V
  - 12V version: 9.0-12.6V
  - 24V version: 20.0-25.2V

- When voltage protection is triggered, the Servo automatically releases holding torque.
- You can check the corresponding servo status flags [bit3]/[bit4] to determine whether voltage protection is active.
- **You must power-cycle the unit and ensure the operating voltage is within the normal range** before the Servo can resume operation.

### Stall Protection

- Set `stall unlock protection` to ON.
- Set the `power protection value` parameter. Protection triggers when the value is exceeded.
- When stall protection is triggered, the Servo automatically releases holding torque.
- You can check the corresponding servo status flag [bit2] to determine whether stall protection is active.
- No power cycle is required. Send a stop command to restore normal operation.

### Power Protection

- Set `stall unlock protection` to OFF.
- Set the `stall power upper limit` parameter. This parameter is the reference operating power after power protection is triggered.
- Set the `power protection value` parameter. Protection triggers when the value is exceeded.
- When power protection is triggered, the Servo automatically reduces power and operates at the stall power upper limit value.
- You can check the corresponding servo status flag [bit6] to determine whether power protection is active.

### Current Protection

- Set the `current protection` parameter. Protection triggers when the value is exceeded.
- When current protection is triggered, the Servo automatically releases holding torque.
- You can check the corresponding servo status flag [bit5] to determine whether current protection is active.
- When operating current falls below the current protection value, the Servo automatically resumes operation.
- This parameter can be combined with stall or power protection as a safeguard when neither of those protections is triggered.

## Command Functions

### Control Commands

| Command ID | Command Name                          | Function Description                                |
| ---------- | ------------------------------------- | --------------------------------------------------- |
| 01         | Communication Check                   | Check whether the Servo between specified IDs is online |
| 08         | Simple Single-turn Angle Control      | Motion time and output power are configurable       |
| 11         | Advanced Single-turn Angle Control (time-based) | Motion time, accel/decel time, output power are configurable |
| 12         | Advanced Single-turn Angle Control (speed-based) | Motion speed, accel/decel time, output power are configurable |
| 10         | Single-turn Angle Read                | Within ±180° range                                  |
| 13         | Simple Multi-turn Angle Control       | Motion time and output power are configurable       |
| 14         | Advanced Multi-turn Angle Control (time-based) | Motion time, accel/decel time, output power are configurable |
| 15         | Advanced Multi-turn Angle Control (speed-based) | Motion speed, accel/decel time, output power are configurable |
| 16         | Multi-turn Angle Read                 | Within ±368,640° range                               |
| 17         | Clear Current Turns                   |                                                     |
| 09         | Damping Mode                          |                                                     |
| 24         | Stop Command                          | After stopping, enter hold, release, or damping state |
| 25         | Sync Command                          |                                                     |
| 18         | Asynchronous Write Command            |                                                     |
| 19         | Asynchronous Execute Command          |                                                     |
| 02         | Custom Parameter Reset                | Restore factory default parameter settings          |
| 03         | Parameter & Status Data Read          | Read parameters and operating status data one by one |
| 04         | Custom Parameter Write                | Write Servo parameters one by one                   |
| 22         | Data Monitoring                       | Batch read operating status data                    |
| 23         | Origin Setting                        | Set current angle as origin (0°)                    |

### Protocol Format

- **Transmit Frame Format**

| **Byte Position** | **0~1**                          | **2**        | **3**        | **4~N+3** | **N+4** |
| ----------------- | -------------------------------- | ------------ | ------------ | --------- | ------- |
| Content           | Header identifier<br>0x12 0x4c   | Command ID   | Length N     | Data      | Checksum |

Example: Servo ID2 rotates to the 90° position at maximum power in 500 ms.

![transmit_command](./images/transmit_command.png)

- **Response Frame Format**

| **Byte Position** | **0~1**                          | **2**        | **3**        | **4~N+3** | **N+4** |
| ----------------- | -------------------------------- | ------------ | ------------ | --------- | ------- |
| Content           | Header identifier<br>0x05 0x1c   | Command ID   | Length N     | Data      | Checksum |

*Unpacking: 0x86 0x03 is the current servo angle. After decoding, it becomes 902, which converts to 90.2°.*

![respond_command](./images/respond_command.png)

### Recommended Command Interval

- The product supports multiple control commands with different lengths. To avoid control exceptions caused by packet loss, **it is recommended to add at least 10 ms of delay after each command transmission**.

  Example: Command 1 (sent) → Delay 10 ms → Command 2 (sent) → Delay 10 ms → Command 3

### Command Interruption

- With default settings, if the Servo receives a new control command while the current command is executing, it will immediately interrupt the current command and execute the new one first. The original command will not continue.

### Communication Check [01]

- Send the Ping command to the target ID and determine whether the Servo is online based on the response.

### Single-turn Angle Control

**Control range**: In single-turn mode, the control range is ±180°.

**Control unit**: All angle control uses degrees (°) as the unit, with a minimum control resolution of 0.1°.

**Control commands**: The product provides multiple control commands. Users can flexibly configure motion speed, time, and output power according to application needs. It also supports trapezoidal accel/decel smoothing, with customizable accel/decel intervals to achieve smoother and more stable motion.

| **Command Type**                         | **Parameters**                                  |
| ---------------------------------------- | ----------------------------------------------- |
| Simple single-turn angle control [8]     | Target angle, motion time, output power         |
| Advanced single-turn angle control (time-based) [11] | Target angle, motion time, accel time, decel time, output power |
| Advanced single-turn angle control (speed-based) [12] | Target angle, motion speed, accel time, decel time, output power |

![Velocity Profile](./images/Velocity Profile.png)

**Angle readback** [10]: Send the single-turn angle read command to the target ID to receive the current angle data.

### Multi-turn Angle Control

**Control range**: In multi-turn mode, the control range is ±368,640° (±1,024 turns).

**Control unit**: All angle control uses degrees (°) as the unit, with a minimum control resolution of 0.1°.

**Control commands**: The product provides multiple control commands. Users can flexibly configure motion speed, time, and output power according to application needs. It also supports trapezoidal accel/decel smoothing, with customizable accel/decel intervals to achieve smoother and more stable motion.

| **Command Type**                         | **Parameters**                                  |
| ---------------------------------------- | ----------------------------------------------- |
| Simple multi-turn angle control [13]     | Target angle, motion time, output power         |
| Advanced multi-turn angle control (time-based) [14] | Target angle, motion time, accel time, decel time, output power |
| Advanced multi-turn angle control (speed-based) [15] | Target angle, motion speed, accel time, decel time, output power |

![Velocity Profile](./images/Velocity Profile.png)

**Multi-turn angle read** [16]: Send the multi-turn angle read command to the target ID to receive the current angle data.

**Absolute angle reset** [17]

- When the Servo is in the torque-released state, you can reset the current angle data via Master / PC Software or a specified command.
- After reset, the Servo uses the current absolute position as the reference. The newly set initial angle will fall within the -180° to +180° range.

  Example: As shown in the figure, point A1 is at 6,880°. After reset, the angle becomes θ1. Point A2 is at 6,800°. After reset, the angle becomes -θ2.

![Multi-turn reset](./images/多圈重置.png)

**Power-off angle memory**

- Supports power-off angle memory.
- After power loss, if the **servo angle does not change**, the angle read after power-on remains unchanged.

  Example: Point A is at 6,800° before power loss. If the angle does not change during power loss and the Servo remains at point A, the angle read after power-on is still 6,800°.

- After power loss, if external force causes the **servo angle to change**, the angle read after power-on will fall within ±180° of the memorized angle.

  Example: As shown, point A is at 6,800° before power loss. If the Servo is rotated by external force during power loss and ends at point B1, the angle read after power-on is 6,920°. If it ends at point B2, the angle read is 6,680°.

![Power-off memory](./images/掉电记忆.png)

### Damping Mode [9]

- Allows the Servo to be adjusted to different angle positions under external force while maintaining a certain damping effect.
- Damping coefficient can be customized.

### Stop Command [24]

- Users can select an appropriate stop command type based on motion control requirements. See the table below for details.
- The stop command can also be used to restore normal operation after the Servo enters stall protection.
- When the Servo is in the unlocked state, sending the "hold torque" command rebuilds holding torque from the current position.

| **Stop Command Type** | **Motion Mode**                                                  |
| --------------------- | ---------------------------------------------------------------- |
| Release torque        | The Servo stops immediately and **releases** holding torque.     |
| Hold torque           | The Servo stops immediately and **maintains** holding torque, or restores torque if it is currently released. |
| Hold damping          | The Servo stops immediately and enters damping mode; external force can adjust the angle. |

### Sync Command [25]

- A single command can contain control instructions for multiple Servos, suitable for coordinated motion scenarios.
- Each Servo matches its ID to the parameters in the command and only parses/acts on the control data related to its own ID.
- After all Servos receive the command, they execute simultaneously to achieve synchronized motion.

### Asynchronous Commands [18] [19]

- Asynchronous commands consist of **asynchronous write** and **asynchronous execute**.
- After sending the asynchronous write command, send the motion command to be executed. The motion command is temporarily stored in the register of the target ID Servo and will not execute immediately. It must be started by the asynchronous execute command.
- When the asynchronous execute command is issued, all Servos with cached motion commands will execute simultaneously, enabling synchronized control.
- Cached motion commands remain stored unless rewritten or powered off; they are not overwritten or cleared by other commands.
- After asynchronous commands are executed, related parameters are automatically cleared and no longer retained.

### Parameter Customization

- All Servo parameters in the table below support single read [03], write [04], and reset [02].
- It is recommended to use Master / PC Software for configuration.

> [!WARNING]
>
> Any parameter changes may damage the product or affect normal operation. Proceed with caution and ensure potential risks are fully evaluated before making changes.

| **Parameter No.** | **Parameter Name**      | **Read** | **Write** | **Unit** | **Notes** |
| ----------------- | ----------------------- | -------- | --------- | -------- | --------- |
| 33                | Command response switch | ●        | ●         |          | Default: Off |
| 34                | Servo ID                | ●        | ●         |          | 0~254     |
| 36                | Baud rate option        | ●        | ●         |          | 9,600bps~1Mbps |
| 37                | Stall protection switch | ●        | ●         |          |           |
| 38                | Stall power upper limit | ●        | ●         | mW       |           |
| 39                | Protection voltage lower limit | ● | ● | mV | |
| 40                | Protection voltage upper limit | ● | ● | mV | |
| 41                | Protection temperature  | ●        | ●         | ADC      |           |
| 42                | Power protection value  | ●        | ●         | mW       |           |
| 43                | Current protection value | ●       | ●         | mA       |           |
| 46                | Power-on torque switch  | ●        | ●         |          | Default: Off |
| 48                | Angle limit switch      | ●        | ●         |          | Default: Off |
| 49                | Power-on soft-start switch | ●     | ●         |          | Default: Off |
| 50                | Power-on soft-start time | ●       | ●         | ms       |           |
| 51                | Servo angle upper limit | ●        | ●         | 0.1°     |           |
| 52                | Servo angle lower limit | ●        | ●         | 0.1°     |           |

### Operating Status Data Read

- **Single read** [03]: The operating status data in the table below can be read individually via command [03].

| **Parameter No.** | **Parameter Name** | **Unit** |
| ----------------- | ------------------ | -------- |
| 01                | Current operating voltage | mV  |
| 02                | Current operating current | mA  |
| 03                | Current operating power | mW |
| 04                | Current operating temperature | ADC |
| 05                | Servo status         |        |
| 06                | Firmware version     |        |

- **Batch read** [22]: The operating status data in the table below can be batch read using the data monitoring command.

| **Byte No.** | **Parameter Name** | **Unit** |
| ------------ | ------------------ | -------- |
| [04]         | Servo ID           |          |
| [5, 6]       | Current operating voltage | mV |
| [7, 8]       | Current operating current | mA |
| [9, 10]      | Current operating power | mW |
| [11, 12]     | Current operating temperature | ADC |
| [13]         | Servo status        |        |
| [14, 17]     | Current servo angle | 0.1°   |
| [18, 19]     | Current turns       |        |

- **Servo status**

  ![protection](./images/protection.png)

### Arbitrary Origin Setting [23]

- When the Servo is in the torque-released state, use Master / PC Software or a specified command to reset the current Servo angle to zero. This is convenient for zero-point calibration after assembly and provides the starting angle for subsequent motion.
