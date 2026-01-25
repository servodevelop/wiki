# UART Bus Servo 25KG 1111
---
{% include-markdown "snippets/shop-info/product-primary-simple.md"
   start="<!--start:HA8/RA8-U25H-M-->"
   end="<!--end:HA8/RA8-U25H-M-->" %}

## 1. Features

<div class="cards" markdown>

-   __🔁 Two-Way Bus Communication__
    
    Bi-directional UART protocol with baud rates up to 1 Mbps, supporting fast control commands and feedback data such as position and other operating status.

-   __🛡️ Complete Protection & Smart Power Limiting__

    Built-in safeguards for temperature, voltage, stall, power, and current, with automatic power limiting to keep operation within a safe range.

-   __🧭 Advanced Modes & Stop Behaviors__
    
    - Single-Turn: ±180° range for standard rotary joints
    - Multi-Turn: ±368,640° (1,024turns) range, with multi-turn count saved after power-off.
    - Damping Mode: controlled resistance for smooth, compliant motion
    - 3 Stop Modes: Free, Lock, and Damp for different holding/release needs

-   __🎛️ Rich Motion Commands & Profiles__
    
    Configure speed, time, and power per application, with sync/async command options and built-in trapezoidal accel/decel profiles for smooth motion and customizable ramp intervals.

-   __📍 Custom Home Position__
    
    A 12-bit absolute position encoder (4,096 steps) lets you define any point as the home position, simplifying assembly, reducing software offset adjustments, and improving position control accuracy.

-   __🔗 Unified Ecosystem & Daisy-Chain Ready__

    All servos share the same protocol for high compatibility, allowing different models to be daisy-chained on the same bus. Within each series, the housing and mounting hole patterns are standardized for easy swaps and consistent mechanical integration.

</div>

## 2. Model definition

![产品命名-型号规则](image/产品命名-型号规则.png)

| Appearance | R：Dual-shaft | H：Single-shaft | |
| :--- | :--- | :--- | :--- |
| Motor type | X：Brushless | P：Coreless | A/L：Cored |
| Dimension | 6：31.5×21×27.6mm | 8：40×40×20mm | 18：63×34×47mm |
| Protocols | U：UART/TTL | R：RS-485 | C：CAN |
| Voltage | [-]：7.4V | H：12V | W：24V |
| Position Sensor | [-]：Potentiometer | M:12-bit magnetic absolute encoder | |

**Models available for order**
- **RA8-U25(H)-M|HA8-U25(H)-M**

## 3. Specifications

### 3.1 Basic Specifications
| Item | Specification |
| :--- | :--- |
| Input Voltage | 6.0-8.4V \| 9.0–12.6 V |
| Resolution | 2048/360° (0.176°) |
| Baud Rate | 9,600 bps–1 Mbps |
| Gear Material | All-metal copper-aluminum composite |

### 3.2 Characteristics
| Item | **Specifications（7.4V\|12V）** |
| :--- | :--- |
| Max Stall Torque | 2.54 N·m (25 kg·cm) |
| Max Continuous Torque | 0.88 N·m (9 kg·cm) |
| No‑load Speed | 51 rpm (0.198 sec@60°) |
| Peak Current | 3 A |

### 3.3 Performance Graph
![U25特性曲线](image/U25特性曲线.png)

### 3.4 Overload Graph
![U25过载曲线](image/U25过载曲线.png)

## 4. Drawings and Installation Instructions

### 4.1 CAD Dimensional Drawing
![U25_3D图](image/U25_3D图.png)

### 4.2 Interface Definition
![U25接口图](image/U25接口图.png)

### 4.3 Wiring Diagram 
- **Series Connection**
![U25串联](image/U25串联.png)

- **Parallel Connection**
![U25并联](image/U25并联.png)

### 4.4 Installation Instruction
- **Single-shaft**
![U25单轴安装](image/U25单轴安装.png)

- **Dual-shaft**
![U25双轴安装](image/U25双轴安装.png)

## 5. Development & Compatibility
The bus servo series adopts a unified hardware platform.
![development environment](image/development environment.png)

## 6. Protections
- All protection parameters can be set and modified by our PC configuration tool.
- The status flag bits are defined as follows: 1 represents Protection triggered，0 represents normal operation.

![protection](image/protection.png)

> [!WARNING]
> Modification towards any protection parameters may cause damage to the production.

## 7. Control & Modes

### 7.2 Communication Format 
- **Transmit Packet Format**
![transmit_command](image/transmit_command.png)

- **Response Packet Format**
![respond_command](image/respond_command.png)

### 7.6 Single-Turn Position Control
![Velocity Profile](image/Velocity Profile.png)

### 7.7 Multi-Turn Position Control
- **Multi-turn Position Reset** ![多圈重置](image/多圈重置.png)

- **Power-off Position Retention**
![掉电记忆](image/掉电记忆.png)

## 8. Configuration Parameters
| Number | Parameter Name | Write | Unit | Default |
| :---: | :--- | :---: | :---: | :--- |
| 34 | Servo ID | ● | - | 1 |
| 36 | Baud Rate | ● | bps | 1Mbps |
| 41 | Protection Temp | ● | ADC | 70°C |

### 8.1 Read Data
![protection](image/protection.png)
