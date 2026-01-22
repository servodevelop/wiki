# 产品技术规格书 / Technical Specifications

---

## 中文版 (Chinese Version)

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

---

## English Version

### 1. Electrical & Control Specifications
<table>
  <tr>
    <th width="200" align="left">Items</th>
    <th width="400" align="left">Specifications</th>
  </tr>
  <tr>
    <td>Operating Voltage</td>
    <td>9.0 ～ 12.6 V</td>
  </tr>
  <tr>
    <td>Processor</td>
    <td>32-bit MCU</td>
  </tr>
  <tr>
    <td>Communication</td>
    <td>UART / TTL Half-duplex</td>
  </tr>
  <tr>
    <td>Baud Rate</td>
    <td>9,600 bps ～ 1 Mbps</td>
  </tr>
  <tr>
    <td>ID Range</td>
    <td>0 ～ 254</td>
  </tr>
  <tr>
    <td>Connector Type</td>
    <td>PH2.0 – 3Pin</td>
  </tr>
  <tr>
    <td>Current</td>
    <td>Standby ＜30 mA / No-load ＜300 mA / Peak 6 A</td>
  </tr>
</table>

### 2. Position & Motion Control
<table>
  <tr>
    <th width="200" align="left">Items</th>
    <th width="400" align="left">Specifications</th>
  </tr>
  <tr>
    <td>Motor Type</td>
    <td>Coreless Motor</td>
  </tr>
  <tr>
    <td>Position Sensor</td>
    <td>12-bit Contactless Absolute Magnetic Encoder</td>
  </tr>
  <tr>
    <td>Resolution</td>
    <td>4096 steps / 360° (0.088°)</td>
  </tr>
  <tr>
    <td>Effective Angle</td>
    <td>±180° (Single-turn) / ±368,640° (Multi-turn)</td>
  </tr>
  <tr>
    <td>Operating Mode</td>
    <td>Single-turn / Multi-turn / Damping Mode</td>
  </tr>
  <tr>
    <td>Reduction Ratio</td>
    <td>273 : 1</td>
  </tr>
</table>

### 3. Performance Parameters (@12V)
<table>
  <tr>
    <th width="200" align="left">Items</th>
    <th width="400" align="left">Specifications</th>
  </tr>
  <tr>
    <td>Stall Torque (Max)</td>
    <td>4.41 N·m (45 kg·cm)</td>
  </tr>
  <tr>
    <td>Max Dynamic Torque</td>
    <td>1.67 N·m (17 kg·cm)</td>
  </tr>
  <tr>
    <td>Rated Torque</td>
    <td>0.54 N·m (5.5 kg·cm)</td>
  </tr>
  <tr>
    <td>Rated Speed</td>
    <td>64 rpm (0.156 s / 60°)</td>
  </tr>
  <tr>
    <td>No-load Speed</td>
    <td>90 rpm (0.110 s / 60°)</td>
  </tr>
</table>

### 4. Mechanical & Environmental
<table>
  <tr>
    <th width="200" align="left">Items</th>
    <th width="400" align="left">Specifications</th>
  </tr>
  <tr>
    <td>Output Shaft</td>
    <td>Stainless Steel / Ø6 mm / 25T</td>
  </tr>
  <tr>
    <td>Gear Material</td>
    <td>Full Metal (Stainless Steel Combination)</td>
  </tr>
  <tr>
    <td>Max Load</td>
    <td>Axial 20 N / Radial 40 N</td>
  </tr>
  <tr>
    <td>Housing Material</td>
    <td>Aluminum Alloy (Mid) / Engineering Plastic (Covers)</td>
  </tr>
  <tr>
    <td>Size & Weight</td>
    <td>40 × 20 × 40 mm / 73 g</td>
  </tr>
  <tr>
    <td>Operating Temp</td>
    <td>-10 ～ 60 ℃</td>
  </tr>
</table>

### 5. Pinout Definition
<table>
  <tr>
    <th width="100" align="left">Pin No.</th>
    <th width="100" align="left">Symbol</th>
    <th width="200" align="left">Description</th>
    <th width="200" align="left">Note</th>
  </tr>
  <tr>
    <td>1</td>
    <td>GND</td>
    <td>System Ground</td>
    <td>Power negative & Signal ground</td>
  </tr>
  <tr>
    <td>2</td>
    <td>VCC</td>
    <td>Power Supply</td>
    <td>9.0V ～ 12.6V input</td>
  </tr>
  <tr>
    <td>3</td>
    <td>DATA</td>
    <td>UART Control</td>
    <td>Half-duplex Serial Bus</td>
  </tr>
</table>