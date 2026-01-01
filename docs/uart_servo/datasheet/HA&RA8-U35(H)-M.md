# UART Bus Servo 35KG Series 

![U35产品图片](img/U35产品图片.png){: width="60%" }

## 1. Features

- **Integrated design**: brushed motor, reducer, 12‑bit magnetic absolute encoder, and controller
- **Protocol**: UART/TTL half‑duplex protocol up to **1 Mbps**
- **Precision**: Resolution **4096 counts/360° (0.088°)**; min control step **0.1°**
- **Control range**: **±180°** (single‑turn) or **±368,640° / ±1024 turns** (multi‑turn)
- **Functions**: Power‑off position retention, Trapezoidal accel/decel trajectory, Three stop modes.
- **Safety**: Five protections: **temperature / voltage / stall / power / current**

---

## 2. Model definition

![产品命名-型号规则](img/产品命名-型号规则.png)

| Appearance | R：Dual-shaft | H：Single-shaft | |
| :--- | :--- | :--- | :--- |
| **Motor type** | X：Brushless | P：Coreless | A/L：Cored |
| **Dimension** | 6：31.5×21×27.6mm | 8：40×40×20mm | 18：63×34×47mm |
| **Protocols** | U：UART/TTL | R：RS-485 | C：CAN |
| **Voltage** | [-]：7.4V | H：12V | W：24V |

**Models available for order**: `RA8-U35(H)-M` | `HA8-U35(H)-M`

---

## 3. Specifications

### 3.1 Basic Specifications

| Item | Specification |
| :--- | :--- |
| **Input Voltage** | 6.0-8.4V \| 9.0–12.6 V |
| **Position Sensor** | 12‑bit magnetic absolute encoder |
| **Effective Range** | ±180° (single‑turn); ±368,640° (multi‑turn) |
| **Resolution** | 2048/360° (0.176°) |
| **Reduction Ratio** | 378:1 |
| **Gear Material** | All-metal copper-aluminum composite |

### 3.2 Characteristics

| Item | Specifications（7.4V \| 12V） |
| :--- | :--- |
| **Max Stall Torque** | 3.43 N·m (35 kg·cm) |
| **Max Continuous Torque** | 1.27 N·m (13 kg·cm) |
| **No‑load Speed** | 34 rpm (0.298 sec@60°) |
| **Axial / Radial Load** | 20 N / 40 N |

### 3.3 Performance & Overload Analysis

<div class="grid cards" markdown>

-   **Performance Graph**
    ![U35特性曲线](img/U35特性曲线.png)

-   **Overload Graph**
    ![U35过载曲线](img/U35过载曲线.png)

</div>

---

## 4. Drawings and Installation

<div class="grid cards" markdown>

-   **CAD Dimensional Drawing**
    ![U35_3D图](img/U35_3D图.png)

-   **Interface Definition**
    ![U35接口图](img/U35接口图.png)

</div>

### 4.3 Wiring & Installation

<div class="grid cards" markdown>

-   **Series Connection**
    ![U35串联](img/U35串联.png)

-   **Parallel Connection**
    ![U35并联](img/U35并联.png)

-   **Single-shaft Install**
    ![U35单轴安装](img/U35单轴安装.png)

-   **Dual-shaft Install**
    ![U35双轴安装](img/U35双轴安装.png)

</div>

---

## 5. Development & Compatibility

The bus servo series adopts a unified hardware platform. Different models are seamlessly compatible, supporting standard protocols.

![development environment](img/development environment.png){: width="70%" }

---

## 6. Protections

!!! warning "Modification Caution"
    Modification towards any protection parameters may cause damage to the production. Please proceed with caution.

![protection](img/protection.png){: width="60%" }

### 6.1 ~ 6.5 Protection Details
- **Temperature**: Default 70°C. Triggers low-power mode.
- **Voltage**: 7.4V (6.0-8.4V) | 12V (9.0-12.6V). Triggers free mode.
- **Stall/Power/Current**: Servo switches to free or low-power mode to protect the motor.

---

## 7. Control & Modes

### 7.1 Instruction List (Summary)
| ID | Instruction | Description |
| :--- | :--- | :--- |
| 01 | **Ping** | Check if servo is online |
| 08/11/12 | **Position Control** | Single-turn control (Time/Speed based) |
| 13/14/15 | **Multi-Turn Control** | Multi-turn control (Time/Speed based) |
| 24 | **Stop** | Free / Lock / Damping modes |

### 7.2 Communication Format 

<div class="grid cards" markdown>

-   **Transmit Packet Format**
    ![transmit_command](img/transmit_command.png)

-   **Response Packet Format**
    ![respond_command](img/respond_command.png)

</div>

### 7.6 & 7.7 Position Control Logic

<div class="
