# U25 串行总线舵机规格书

{% include-markdown "snippets/uart_servo/specs_example.md" start="<!--start:version_intro-->"  end="<!--end:version_intro-->" %}

<div class="fs-buy-grid" markdown="1">

<div class="fs-buy-card" markdown="1">
<img src="https://store.fashionstar.com.hk/wp-content/uploads/2025/09/RA8-U25-M-1536x1536.webp" alt="RA8-U25-M">
<div class="fs-product-name">RA8-U25-M</div>
</div>

<div class="fs-buy-card" markdown="1">
<img src="https://store.fashionstar.com.hk/wp-content/uploads/2025/09/HA8-U25-M-1536x1536.webp" alt="HA8-U25-M">
<div class="fs-product-name">HA8-U25-M</div>
</div>
</div>

---



## 1. 产品概述 { #overview }

U25(H) 是一款高性能串行总线舵机，支持大扭矩输出与精准的位置、速度及温控反馈。适用于机器人关节、自动化设备等高精度控制场景。

## 2. 规格参数 (Specifications) { #specs }

### 2.1 机械规格
| 参数项 | 规格值 |
| :--- | :--- |
| **外观尺寸** | 请参考 [3D模型 & 2D图纸](#drawings) |
| **重量** | 约 55g |
| **舵盘规格** | 25T / φ5.9mm |
| **外壳材质** | 工程塑料 + 铝合金中壳 |
| **齿轮组材质** | 高精度钢制齿轮 |

### 2.2 电气特性
| 参数项 | 工作电压 (7.4V) | 工作电压 (12V) |
| :--- | :--- | :--- |
| **堵转扭矩** | 18kg.cm | 25kg.cm |
| **空载速度** | 0.18sec/60° | 0.13sec/60° |
| **静态电流** | 5mA | 8mA |
| **工作电流** | 1.2A | 1.8A |

### 2.3 控制特性
* **通信接口**：TTL 异步串行通信（半双工总线）
* **指令角度**：0 - 4096 (0° - 360°)
* **波特率**：9600bps - 1Mbps (默认 115200bps)
* **反馈信息**：位置、速度、负载、电压、温度

---

## 3. 图纸与模型 (CAD Files) { #drawings }

::: info
如需进行机械结构设计，建议下载以下最新的工程资料。
:::

* **2D 尺寸图纸**: [点击下载 PDF](assets/U25H_2D_Dimensions.pdf)
* **3D 结构模型**: [点击下载 STEP](assets/U25H_3D_Model.step)

---

## 4. 软件与工具 (Software) { #software }
建议使用 **Fashion Star 调试助手** 进行 ID 设置与参数校准。
* [下载上位机工具](software/debug_assistant.md)

---

## 5. 开发套件 (SDK) { #sdk }
支持以下平台快速集成：
* [Arduino SDK](sdk/arduino_sdk.md)
* [Python SDK](sdk/python_sdk.md)
* [STM32F407 SDK](sdk/stm32f407_sdk.md)
