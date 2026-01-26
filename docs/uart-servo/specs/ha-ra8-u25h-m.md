# HA8/RA8-U25-M
---
{% include-markdown "snippets/shop-info/product-primary-simple.md"
   start="<!--start:HA8/RA8-U25H-M-->"
   end="<!--end:HA8/RA8-U25H-M-->" %}
## 1. 型号定义

![产品命名-型号规则](image/产品命名-型号规则a.jpeg)


## 2. 规格参数
### 2.1. 基础电气与控制参数
<table>
  <tr>
    <th width="200" align="left">参数项目</th>
    <th width="400" align="left">技术规格</th>
  </tr>
  <tr>
    <td>工作电压</td>
    <td>9.0 ～ 12.6 V</td>
  </tr>
  <tr>
    <td>处理器</td>
    <td>32-bit MCU</td>
  </tr>
  <tr>
    <td>通信类型</td>
    <td>UART / TTL 半双工</td>
  </tr>
  <tr>
    <td>波特率</td>
    <td>9,600 bps ～ 1 Mbps</td>
  </tr>
  <tr>
    <td>ID 范围</td>
    <td>0 ～ 254</td>
  </tr>
  <tr>
    <td>接口类型</td>
    <td>PH2.0 – 3Pin</td>
  </tr>
  <tr>
    <td>电流参数</td>
    <td>待机 ＜30 mA / 空载 ＜300 mA / 峰值 6 A</td>
  </tr>
</table>

### 2.2. 运动控制与反馈精度
<table>
  <tr>
    <th width="200" align="left">参数项目</th>
    <th width="400" align="left">技术规格</th>
  </tr>
  <tr>
    <td>马达类型</td>
    <td>高性能空心杯马达</td>
  </tr>
  <tr>
    <td>位置传感器</td>
    <td>12-bit 非接触式绝对值磁编码器</td>
  </tr>
  <tr>
    <td>分辨率</td>
    <td>4096 阶 / 360°（0.088°）</td>
  </tr>
  <tr>
    <td>有效角度</td>
    <td>±180°（单圈） / ±368,640°（多圈）</td>
  </tr>
  <tr>
    <td>工作模式</td>
    <td>单圈角度 / 多圈角度 / 阻尼模式</td>
  </tr>
  <tr>
    <td>减速比</td>
    <td>273 : 1</td>
  </tr>
</table>

### 2.3. 动力性能参数 (@12V)
<table>
  <tr>
    <th width="200" align="left">参数项目</th>
    <th width="400" align="left">规格内容</th>
  </tr>
  <tr>
    <td>最大静态扭矩（堵转）</td>
    <td>4.41 N·m（45 kg·cm）</td>
  </tr>
  <tr>
    <td>最大动态扭矩</td>
    <td>1.67 N·m（17 kg·cm）</td>
  </tr>
  <tr>
    <td>额定扭矩</td>
    <td>0.54 N·m（5.5 kg·cm）</td>
  </tr>
  <tr>
    <td>额定转速</td>
    <td>64 rpm（0.156 s / 60°）</td>
  </tr>
  <tr>
    <td>空载转速</td>
    <td>90 rpm（0.110 s / 60°）</td>
  </tr>
</table>

<img src="/uart-servo/specs/image/U25特性曲线.png" style="width: 500px !important; height: auto !important;">

### 2.4. 机械与环境特性
<table>
  <tr>
    <th width="200" align="left">参数项目</th>
    <th width="400" align="left">技术规格</th>
  </tr>
  <tr>
    <td>输出轴规格</td>
    <td>不锈钢 / Ø6 mm / 25T</td>
  </tr>
  <tr>
    <td>齿轮材料</td>
    <td>全金属不锈钢组合</td>
  </tr>
  <tr>
    <td>机械负载</td>
    <td>轴向 20 N / 径向 40 N</td>
  </tr>
  <tr>
    <td>外壳材料</td>
    <td>铝合金中段 / 上下壳工程塑胶</td>
  </tr>
  <tr>
    <td>尺寸与重量</td>
    <td>40 × 20 × 40 mm / 73 g</td>
  </tr>
  <tr>
    <td>工作温度</td>
    <td>-10 ～ 60 ℃</td>
  </tr>
</table>

<img src="/uart-servo/specs/image/U25过载曲线.png" style="width: 500px !important; height: auto !important;">

## 3. 接口引脚定义

<img src="/uart-servo/specs/image/U25接口图.png" style="width: 500px !important; height: auto !important;">



## 4. Drawings and Installation Instructions

### 4.1 CAD Dimensional Drawing

<img src="/uart-servo/specs/image/U25_3D图.png" style="width: 500px !important; height: auto !important;">

### 4.2 Interface Definition

<img src="/uart-servo/specs/image/U25接口图.png" style="width: 500px !important; height: auto !important;">

### 4.3 Wiring Diagram 
- **Series Connection**

<img src="/uart-servo/specs/image/U25串联.png" style="width: 500px !important; height: auto !important;">


- **Parallel Connection**

<img src="/uart-servo/specs/image/U25并联.png" style="width: 500px !important; height: auto !important;">

### 4.4 Installation Instruction
- **Single-shaft**

<img src="/uart-servo/specs/image/U25单轴安装.png" style="width: 500px !important; height: auto !important;">

- **Dual-shaft**

<img src="/uart-servo/specs/image/U25双轴安装.png" style="width: 500px !important; height: auto !important;">

### 4. 开发支持矩阵

| 💻 硬件平台 | 🛠️ 开发语言 | 🤖 机器人框架 |
| :--- | :--- | :--- |
| **MCU:** STM32, ESP32, Arduino | **High-level:** Python, C# | **ROS:** ROS 1 / ROS 2 |
| **SBC:** Raspberry Pi 4B/5 | **Embedded:** C / C++ | **Industrial:** PLC (Modbus) |
| **PC:** Windows, Ubuntu | **Script:** MicroPython | **Driver:** SDK, API |

## 5. Development & Compatibility
The bus servo series adopts a unified hardware platform.


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
