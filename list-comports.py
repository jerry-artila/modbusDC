# list-comports.py
#
# 列出 Windows 系統上的所有 COM 端口
#
# 使用方法: python list-comports.py
#
# 作者: @uncle_jerry
#
# 許可證: MIT
#
# 日期: 2024-12-25
#
# 版本: 1.0.0
#
# 描述: 列出 Windows 系統上的所有 COM 端口
#
import serial.tools.list_ports  # 導入串口列表工具

# 獲取所有可用的串口
ports = serial.tools.list_ports.comports()

# 遍歷並打印每個串口的信息
for port in ports:
    print(f"{port.device}: {port.description}")  # 打印設備名稱和描述

