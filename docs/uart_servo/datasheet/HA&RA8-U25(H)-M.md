# UART Bus Servo 25KG Series 

![U25产品图片](img/U25产品图片.png){ width="50%" }

## 1. Features

- **Integrated design**: brushed motor, reducer, 12‑bit magnetic absolute encoder, and controller
- **Protocol**: UART/TTL half‑duplex protocol up to **1 Mbps**
- **Precision**: Resolution **4096 counts/360° (0.088°)**; min control step **0.1°**
- **Control range**: **±180°** (single‑turn) or **±368,640° / ±1024 turns** (multi‑turn)
- **Safety**: Five protections: **temperature / voltage / stall / power / current**

---

## 2. Model definition

![产品命名-型号规则](img/产品命名-型号规则.png)

| Appearance     | R：Dual-shaft     | H：Single-shaft |
| :------------- | :---------------- | :-------------- |
| **Motor type** | X：Brushless      | P：Coreless     |
| **Dimension**  | 6：31.5×21×27.6mm | 8：40×40×20mm   |

**Models available for order**: `RA8-U25(H)-M` | `HA8-U25(H)-M`

---

## 3. Specifications

### 3.1 Basic Specifications

| Item                | Specification                       |
| :------------------ | :---------------------------------- |
| **Input Voltage**   | 6.0-8.4V \| 9.0–12.6 V              |
| **Position Sensor** | 12‑bit magnetic absolute encoder    |
| **Resolution**      | 2048/360° (0.176°)                  |
| **Baud Rate**       | 9,600 bps–1 Mbps                    |
| **Gear Material**   | All-metal copper-aluminum composite |

### 3.2 Characteristics

| Item                      | Specifications（7.4V \| 12V） |
| :------------------------ | :---------------------------- |
| **Max Stall Torque**      | 2.54 N·m (25 kg·cm)           |
| **Max Continuous Torque** | 0.88 N·m (9 kg·cm)            |
| **No‑load Speed**         | 51 rpm (0.198 sec@60°)        |
| **Peak Current**          | 3 A                           |

### 3.3 Performance & Overload Analysis

<div class="grid cards" markdown>

-   **Performance Graph**
    
    ![特性曲线](img/U25特性曲线.png){: width="100%" }

-   **Overload Graph**
    
    ![过载曲线](img/U25过载曲线.png){: width="100%" }

</div>

---

### 4. Drawings and Installation Instructions

#### 4.1 CAD Dimensional Drawing
![U25_3D图](img/U25_3D图.png){: width="75%" }

#### 4.2 Interface Definition & Wiring
<div class="grid cards" markdown>

-   **Interface Definition**
    ![U25接口图](img/U25接口图.png)

-   **Wiring (Series)**
    ![U25串联](img/U25串联.png)

</div>

## 5. Protections

!!! warning "Modification Caution"
    Modification towards any protection parameters may cause damage to the production. Please proceed with caution and ensure potential risks are fully assessed before making changes.

| ![protection](img/protection.png) |
| :-------------------------------: |

### 5.1 Temperature Protection
- **Default value**: 70°C.
- When triggered, the servo switches to **low-power mode**.
- Resumes normal operation when temperature drops 10°C below threshold.

---

## 6. Control & Modes

### 6.1 Communication Format 

**Transmit Packet Format**
![transmit_command](img/transmit_command.png)

**Response Packet Format**
![respond_command](img/respond_command.png)

### 6.2 Position Control

- **Trapezoidal Profile**: ![Velocity Profile](img/Velocity Profile.png){ width="50%" }
- **Multi-turn Reset**: ![多圈重置](img/多圈重置.png){ width="50%" }
- **Position Retention**: ![掉电记忆](img/掉电记忆.png){ width="50%" }

---

## 7. Configuration Parameters

!!! danger "Safety Warning"
    Any modification in parameters may affect normal operation. It is recommended to use our **PC configuration tool** for setting.

| Number | Parameter Name  | Write | Unit | Default |
| :----: | :-------------- | :---: | :--: | :------ |
|   34   | Servo ID        |   ●   |  -   | 1       |
|   36   | Baud Rate       |   ●   | bps  | 1Mbps   |
|   41   | Protection Temp |   ●   | ADC  | 70°C    |
|   51   | Upper Limit     |   ●   | 0.1° | +180.0° |
