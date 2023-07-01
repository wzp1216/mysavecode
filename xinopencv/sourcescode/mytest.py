import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
import time

#创建TCPMASTER对象
master = mt.TcpMaster('127.0.0.1', 502)
#设置超时时间
master.set_timeout(5)
# while True:
#     # time.sleep(1)
#     temp = []
#     data = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=0, quantity_of_x=3)
#     print('我是读取的data[0]:', data[0])
#     print('我是读取的data[0]:', data[1])
#     print('我是读取的data[0]:', data[2])
#     if int(data[0]) == 1:
#         while True:
#             data1 = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=0, quantity_of_x=1)
#             if int(data1[0]) == 1:
#                 temp.append(data1[0])
#             else:
#                 break
#         if temp[0] == 1:
#             print('我要传递信号1')
#     else:
#         print('我要传递信号0')

# 开始写入寄存器
#master.execute(slave=1, function_code=md.WRITE_SINGLE_REGISTER, starting_address=2, output_value=99)
master.execute(slave=1, function_code=md.WRITE_MULTIPLE_REGISTERS, starting_address=0, output_value=[1, 1, 1])
data = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=0, quantity_of_x=3)
print(data[0])




