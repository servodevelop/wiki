# 串行总线舵机通用配置软件 (PC Configuration Tool)

---

### 软件下载与规格
<div class="table-container hide-scrollbar">
<table>
  <thead>
    <tr>
      <th style="text-align: center;">适配协议</th>
      <th style="text-align: center;">当前版本</th>
      <th style="text-align: center;">更新日期</th>
      <th style="text-align: center;">操作</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center;"><strong>UART / RS-485 全系列</strong><br></td>
      <td style="text-align: center;"><span class="no-wrap">v1.1.9.286</span></td>
      <td style="text-align: center;"><span class="no-wrap">2026-01-23</span></td>
      <td style="text-align: center;">
        <a href="./data/Develop-US_1.1.9.286.zip" download class="fs-download-btn">立即下载</a>
      </td>
    </tr>
  </tbody>
</table>
</div>

> [!TIP]
> - **运行环境**：支持 Windows 7/10/11 (x64) 系统，**免安装**解压即用。
> - **硬件依赖**：需配合 **USB 转 UART 转接板**使用，请确保驱动（CH340/CP2102）已正确安装。
> - **固件匹配**：建议舵机固件版本与软件版本保持一致，以获得最佳的控制精度与参数兼容性。
> - **快速启动**：解压压缩包后，直接运行目录下的 `Develop.exe` 即可进入控制界面。

---

## 1. 核心功能概览
本工具为总线舵机全生命周期开发提供支持：
* **拓扑扫描**：自动识别总线上的所有舵机节点，支持波特率自适应搜索。
* **实时监控**：图形化实时反馈舵机坐标、电流、电压及温度数据。
* **控制模式**：支持单圈/多圈位置模式、恒速模式及阻尼模式切换。
* **底层调试**：集成 UART 指令监视器，支持原始十六进制数据包的截获与下发。

![](img/上位机布局.png)

## 2. 快速入门
### 2.1 物理链路拓扑
1. **电源注入**：接入满足舵机规格的外部直流电源（注意正负极防止烧毁）。
2. **串联规范**：若进行多机通讯，请务必在通电前完成 ID 唯一性配置，避免总线冲突。
3. **接口识别**：点击 **Refresh**，选择对应的 COM 端口。若无端口显示，请下载 [CH340 驱动](https://www.wch.cn/downloads/CH341SER_EXE.html)。

### 2.2 参数配置流程
- 切换至 **Parameters** 选项卡。
- 修改参数后，数值颜色由橙变绿代表**成功写入 EEPROM**，断电可保存。

---

## 3. 技术参数与 FAQ
| 维度 | 说明 |
| :--- | :--- |
| **通讯协议** | 半双工异步串行通讯 (UART) |
| **波特率支持** | 9600 - 1000000 bps |
| **最大负载** | 理论支持 254 个节点 (受限于总线物理带宽) |
| **常见错误** | **超时错误**：请检查转接板 TX/RX 线序是否反接；**扫描失败**：请确认供电功率是否满足峰值电流需求。 |

---

<style>
/* 1. 表格容器样式 (保持与 CAD 预览页高度一致) */
.table-container { width: 100%; overflow-x: auto; margin: 20px 0; }
.table-container table { border-collapse: collapse !important; border: 0.8px solid var(--fs-divider) !important; }
.table-container th, .table-container td { border: 0.8px solid var(--fs-divider) !important; vertical-align: middle !important; padding: 12px 15px !important; }
.table-container th { background-color: var(--fs-table-header-bg) !important; font-weight: 600 !important; }
.hide-scrollbar::-webkit-scrollbar { display: none; }
.hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
.no-wrap { white-space: nowrap !important; }

/* 2. 核心修正：让 Tip 内部列表紧贴边框且垂直间距适中 */
.md-typeset .admonition ul {
    margin-left: 0 !important;
    padding-left: 1.8em !important;
}

.md-typeset .admonition ul li {
    margin-bottom: 4px !important; 
}

/* 3. 按钮样式 */
.md-typeset .fs-download-btn {
    background-color: var(--fs-accent) !important;
    color: #FFFFFF !important;
    border-radius: 6px !important;
    padding: 6px 20px !important;
    font-weight: 600 !important;
    text-decoration: none !important;
    display: inline-block !important;
    transition: all 0.2s ease;
}
.md-typeset .fs-download-btn:hover { transform: translateY(-1px); box-shadow: 0 4px 8px rgba(0,0,0,0.15); }

/* 4. 辅助样式 */
small { font-weight: normal; color: #666; font-size: 12px; }
</style>