# HA8/RA8-U25-M
---
{% include-markdown "snippets/shop-info/product-primary-simple.md"
   start="<!--start:HA8/RA8-U25-M-->"
   end="<!--end:HA8/RA8-U25-M-->" %}
## 1. 型号定义

![产品命名-型号规则](image/产品命名-型号规则a.jpeg)


## 2. Specifications
### 1. 基础电气与控制参数
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

### 2. 运动控制与反馈精度
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

### 3. 动力性能参数 (@12V)
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

<img src="/uart-servo/specs/image/U25特性曲线.png" style="width: 400px !important; height: auto !important;">

### 4. 机械与环境特性
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

<img src="/uart-servo/specs/image/U25过载曲线.png" style="width: 400px !important; height: auto !important;">

### 5. 接口引脚定义 (Pinout)
<table>
  <tr>
    <th width="100" align="left">引脚编号</th>
    <th width="100" align="left">标识</th>
    <th width="200" align="left">功能说明</th>
    <th width="200" align="left">备注</th>
  </tr>
  <tr>
    <td>1</td>
    <td>GND</td>
    <td>系统地线</td>
    <td>电源负极与信号地</td>
  </tr>
  <tr>
    <td>2</td>
    <td>VCC</td>
    <td>动力电源正极</td>
    <td>9.0V ～ 12.6V 输入</td>
  </tr>
  <tr>
    <td>3</td>
    <td>DATA</td>
    <td>UART 控制信号</td>
    <td>半双工异步串行通信</td>
  </tr>
</table>


| Appearance | Motor Type | Dimension | Protocols | Voltage | Position Sensor |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **R**: Dual-shaft | **X**: Brushless | **6**: 31.5×21×27.6mm | **U**: UART/TTL | **[-]**: 7.4V | **[-]**: Potentiometer |
| **H**: Single-shaft | **P**: Coreless | **8**: 40×40×20mm | **R**: RS-485 | **H**: 12V | **M**: 12-bit Encoder |
| | **A/L**: Cored | **18**: 63×34×47mm | **C**: CAN | **W**: 24V | |

**Models available for order**
- **RA8-U25(H)-M|HA8-U25(H)-M**
<div class="table-container hide-scrollbar">
<table>
  <thead>
    <tr>
      <th style="width: 20%; text-align: center;">类别</th>
      <th style="width: 30%; text-align: center;">具体平台</th>
      <th style="width: 50%; text-align: center;">支持型号 / 说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7" style="text-align: center; font-weight: 600; background-color: var(--fs-table-header-bg);">开发环境</td>
      <td style="text-align: center; font-weight: 600;">STM32</td>
      <td>
        <ul>
          <li>STM32F103</li>
          <li>STM32F407</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: 600;">Raspberry Pi</td>
      <td>
        <ul>
          <li>Pi 4B</li>
          <li>Pi 5</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: 600;">ESP32</td>
      <td>
        <ul>
          <li>NodeMCU32s</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: 600;">PLC</td>
      <td>
        <ul>
          <li>Siemens</li>
          <li>Inovance</li>
          <li>Mitsubishi</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: 600;">Arduino</td>
      <td>
        <ul>
          <li>UNO</li>
          <li>Mega2560</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: 600;">Windows</td>
      <td>
        <ul>
          <li>Multi-version support</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: 600;">Linux</td>
      <td>
        <ul>
          <li>Ubuntu</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: 600; background-color: var(--fs-table-header-bg);">编程语言</td>
      <td colspan="2">
        <ul>
          <li>Python / MicroPython</li>
          <li>C / C++</li>
          <li>C#</li>
          <li>ROS</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
</div>

### 开发支持矩阵

| 💻 硬件平台 | 🛠️ 开发语言 | 🤖 机器人框架 |
| :--- | :--- | :--- |
| **MCU:** STM32, ESP32, Arduino | **High-level:** Python, C# | **ROS:** ROS 1 / ROS 2 |
| **SBC:** Raspberry Pi 4B/5 | **Embedded:** C / C++ | **Industrial:** PLC (Modbus) |
| **PC:** Windows, Ubuntu | **Script:** MicroPython | **Driver:** SDK, API |

<div class="table-container hide-scrollbar">
<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: left; padding-left: 20px;">系统兼容性与二次开发支持</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="width: 30%; background-color: var(--fs-table-header-bg); font-weight: 600;">嵌入式控制器</td>
      <td>STM32 (F1/F4/H7), ESP32, Arduino (UNO/Mega)</td>
    </tr>
    <tr>
      <td style="background-color: var(--fs-table-header-bg); font-weight: 600;">单板计算机</td>
      <td>Raspberry Pi 4B / 5 (Debian/Ubuntu)</td>
    </tr>
    <tr>
      <td style="background-color: var(--fs-table-header-bg); font-weight: 600;">工业控制 (PLC)</td>
      <td>Siemens, Inovance (汇川), Mitsubishi (三菱)</td>
    </tr>
    <tr>
      <td style="background-color: var(--fs-table-header-bg); font-weight: 600;">PC 操作系统</td>
      <td>Windows 10/11, Linux (Ubuntu 20.04+)</td>
    </tr>
    <tr>
      <td style="background-color: var(--fs-table-header-bg); font-weight: 600;">编程语言支持</td>
      <td>
        <span class="no-wrap">C / C++</span> | 
        <span class="no-wrap">Python</span> | 
        <span class="no-wrap">C#</span> | 
        <span class="no-wrap">ROS 1/2</span>
      </td>
    </tr>
  </tbody>
</table>
</div>

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
