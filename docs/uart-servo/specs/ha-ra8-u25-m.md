# HA8/RA8-U25-M
---
{% include-markdown "snippets/shop-info/product-primary-simple.md"
   start="<!--start:HA8/RA8-U25-M-->"
   end="<!--end:HA8/RA8-U25-M-->" %}
## 1. 型号定义

![产品命名-型号规则](image/model-definition.png)


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



## 4. 外观尺寸

<img src="/uart-servo/specs/image/U25_3D图.png" style="width: 500px !important; height: auto !important;">


## 5. 连线说明

<div style="text-align: center; margin-bottom: 20px;">
  <img src="/uart-servo/specs/image/U25串联.png" 
       style="width: 500px !important; height: auto !important; display: inline-block;">
  <div style="margin-top: 10px; font-weight: bold; font-size: 14px;">
    串联
  </div>
</div>

<div style="text-align: center; margin-bottom: 20px;">
  <img src="/uart-servo/specs/image/U25并联.png" 
       style="width: 500px !important; height: auto !important; display: inline-block;">
  <div style="margin-top: 10px; font-weight: bold; font-size: 14px;">
    并联
  </div>
</div>



## 6. 安装说明

<div style="text-align: center; margin-bottom: 20px;">
  <img src="/uart-servo/specs/image/U25单轴安装.png" 
       style="width: 500px !important; height: auto !important; display: inline-block;">
  <div style="margin-top: 10px; font-weight: bold; font-size: 14px;">
    U25单轴安装尺寸图
  </div>
</div>


<div style="text-align: center; margin-bottom: 20px;">
  <img src="/uart-servo/specs/image/U25双轴安装.png" 
       style="width: 500px !important; height: auto !important; display: inline-block;">
  <div style="margin-top: 10px; font-weight: bold; font-size: 14px;">
    U25双轴安装尺寸图
  </div>
</div>

## 5. 开发支持矩阵

| 💻 硬件平台 | 🛠️ 开发语言 | 🤖 机器人框架 |
| :--- | :--- | :--- |
| **MCU:** STM32, ESP32, Arduino | **High-level:** Python, C# | **ROS:** ROS 1 / ROS 2 |
| **SBC:** Raspberry Pi 4B/5 | **Embedded:** C / C++ | **Industrial:** PLC (Modbus) |
| **PC:** Windows, Ubuntu | **Script:** MicroPython | **Driver:** SDK, API |



## 6. 保护功能说明

| 保护类型 | 触发条件 | 触发后动作 | 恢复机制 | 状态标志位 |
| :--- | :--- | :--- | :--- | :--- |
| **温度保护** | 温度 > 设定值（出厂默认 70℃） | 自动切换至 **低功率模式**，维持基础运动 | 温度降至（设定值 - 10℃）时自动恢复正常功率 | `[bit7]` |
| **电压保护** | 电压超出设定的高/低压保护范围 | **自动释放锁力**（无力矩输出） | 必须 **重新上电** 且工作电压在正常范围内 | `[bit3] / [bit4]` |
| **堵转保护** | 设定堵转失锁保护为“开”，且功率超出保护值 | **自动释放锁力**（无力矩输出） | 无需断电，发送 **停止指令** 即可恢复运行 | `[bit2]` |
| **功率保护** | 设定堵转失锁保护为“关”，且功率超出保护值 | **自动降低功率** 至“堵转功率上限”参数值运行 | 实时监测，功率回落后自动恢复 | `[bit6]` |
| **电流保护** | 工作电流 > 设定电流保护值 | **自动释放锁力**（无力矩输出） | 电流低于保护值后 **自动恢复** 工作 | `[bit5]` |

### 补充说明

* **电压保护出厂默认范围**：
    * **-7.4V 版本**：6.0V - 8.4V
    * **-12V 版本**：9.0V - 12.6V
    * **-24V 版本**：20.0V - 25.2V
* **电流保护应用**：该参数可以结合堵转或功率保护使用，作为前两者均未触发时的冗余安全保障。


### 保护功能规格说明

| 保护类型 | 触发条件 | 保护动作 | 恢复机制 | 状态标志位 |
| :--- | :--- | :--- | :--- | :--- |
| **温度保护** | 当前温度 > 设定阈值<br>(默认 70℃) | **强制低功率运行**<br>限制出力，维持基础运动 | 温度降至 (设定值 - 10℃) 时<br>**自动恢复** | `[bit7]` |
| **电压保护** | 电压超出高/低压<br>设定范围 | **自动释放锁力**<br>无力矩输出，进入自由状态 | **必须重新上电**<br>且电压恢复至正常区间 | `[bit3]/[bit4]` |
| **堵转保护** | 堵转失锁开启<br>且功率 > 保护阈值 | **自动释放锁力**<br>防止电机长时间过载烧毁 | 无需断电，发送 **停止指令**<br>即可恢复运行 | `[bit2]` |
| **功率保护** | 堵转失锁关闭<br>且功率 > 保护阈值 | **限制运行功率**<br>降至“堵转功率上限”运行 | 功率负载回落后<br>**自动恢复** | `[bit6]` |
| **电流保护** | 实时电流 > 设定阈值 | **自动释放锁力**<br>作为末端安全冗余保障 | 电流回落至阈值以下<br>**自动恢复** | `[bit5]` |

> **注1：电压版本默认保护区间**
> * **7.4V 版本**: 6.0V - 8.4V
> * **12V 版本**: 9.0V - 12.6V
> * **24V 版本**: 20.0V - 25.2V
>
> **注2：应用策略**
> 电流保护可与堵转/功率保护结合使用，当上位机未触发前两项逻辑时，电流保护作为硬件层级的最后保障。


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
