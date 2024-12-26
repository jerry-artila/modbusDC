# SerialClient01.py

import serial
import time
from pymodbus.client import ModbusSerialClient

client = ModbusSerialClient(port='COM11', baudrate=9600, stopbits=1, bytesize=8, parity='N')

connection = client.connect()

if connection:
    print("連接成功")
    try:
        while True:
            res = client.read_holding_registers(address=0, count=5, slave=1)
            print(res.registers)
            time.sleep(1)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\n程序已停止")
    finally:
        client.close()
else:
    print("連接失敗")




