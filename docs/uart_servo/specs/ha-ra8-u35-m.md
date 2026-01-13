# UART Bus Servo 35KG Series 

![U35产品图片](img/U35产品图片.png)

## 1. Features

- Integrated design: brushed motor, reducer, 12‑bit magnetic absolute encoder, and controller
- UART/TTL half‑duplex protocol up to **1 Mbps**
- Resolution **4096 counts/360° (0.088°)**; min control step **0.1°**
- Control range: **±180°** (single‑turn) or **±368,640° / ±1024 turns** (multi‑turn)
- Power‑off position retention
- Trapezoidal accel/decel trajectory for smooth motion
- Auto power threshold detection with adaptive reduction
- Three stop modes: **Free / Lock / Damping**
- Five protections: **temperature / voltage / stall / power / current**
- PC configuration tool; firmware upgradable

## 2. Model definition

![产品命名-型号规则](img/产品命名-型号规则.png)

| Appearance      | R：Dual-shaft      | H：Single-shaft                    |                                  |
| --------------- | ------------------ | ---------------------------------- | -------------------------------- |
| Motor type      | X：Brushless       | P：Coreless                        | A/L：Cored                       |
| Dimension       | 6：31.5×21×27.6mm  | 8：40×40×20mm                      | 18：63×34×47mm                   |
| Protocols       | U：UART/TTL        | R：RS-485<br/>P：PWM               | C：CAN <br/>A：PWM(programmable) |
| Voltage         | [-]：7.4V          | H：12V                             | W：24V                           |
| Position Sensor | [-]：Potentiometer | M:12-bit magnetic absolute encoder |                                  |

**Models available for order**
- **RA8-U35(H)-M|HA8-U35(H)-M**

## 3. Specifications

### 3.1 Basic Specifications

| Item | Specification |
| --- | --- |
| Input Voltage | 6.0-8.4V \| 9.0–12.6 V |
| Motor Type | Iron motor |
| Position Sensor | 12‑bit magnetic absolute encoder |
| Effective Position Range | ±180° (single‑turn); ±368,640° (multi‑turn) |
| Resolution | 2048/360° (0.176°) |
| Reduction Ratio | 378:1 |
| Output Spline | Copper/ Ø6mm / 25T |
| Gear Material | All-metal copper-aluminum composite gear material |
| Case Material | Aluminum alloy middle frame with upper/lower engineering plastic housings |

### 3.2 Characteristics

| Item | **Specifications（7.4V\|12V）** |
| --- | --- |
| Max Stall Torque | 3.43 N·m (35 kg·cm) |
| Max Continuous Torque | 1.27 N·m (13 kg·cm) |
| Rated Torque | 0.54 N·m (5.5 kg·cm) |
| No‑load Speed | 34 rpm (0.298 sec@60°) |
| Peak Current | 3 A |

### 3.3 Performance Graph
![U35特性曲线](img/U35特性曲线.png)

### 3.4 Overload Graph
![U35过载曲线](img/U35过载曲线.png)

## 4. Drawings and Installation Instructions

### 4.1 CAD Dimensional Drawing
![U35_3D图](img/U35_3D图.png)

### 4.2 Interface Definition
![U35接口图](img/U35接口图.png)

### 4.3 Wiring Diagram 
- **Series Connection** ![U35串联](img/U35串联.png)

- **Parallel Connection**
![U35并联](img/U35并联.png)

### 4.4 Installation Instruction
- **Single-shaft**
![U35单轴安装](img/U35单轴安装.png)

- **Dual-shaft**
![U35双轴安装](img/U35双轴安装.png)

## 5. Development & Compatibility
![development environment](img/development environment.png)

## 6. Protections
![protection](img/protection.png)

> [!WARNING]
> Modification towards any protection parameters may cause damage to the production.

## 7. Control & Modes

### 7.2 Communication Format 
- **Transmit Packet Format**
![transmit_command](img/transmit_command.png)

- **Response Packet Format**
![respond_command](img/respond_command.png)

### 7.6 Single-Turn Position Control
![Velocity Profile](img/Velocity Profile.png)

### 7.7 Multi-Turn Position Control
- **Multi-turn Position Reset** ![多圈重置](img/多圈重置.png)

- **Power-off Position Retention**
![掉电记忆](img/掉电记忆.png)

## 8. Configuration Parameters
| Number | Parameter Name | Write | Unit | Default |
| :---: | :--- | :---: | :---: | :--- |
| 34 | Servo ID | ● | - | 1 |
| 41 | Protection Temp | ● | ADC | 70°C |

### 8.1 Read Data
![protection](img/protection.png)
