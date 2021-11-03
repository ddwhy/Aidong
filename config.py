# coding=utf-8
import os,sys
HEADERS = {'X-Requested-With': 'XMLHttpRequest'}
IP = 'http://121.42.15.146:9090'
ABS_PATH = os.path.abspath(__file__) #当前文件的绝对路径
DIR_NAME = os.path.dirname(ABS_PATH) #当前文件的文件夹路径
JUMP_URL = None #支付成功接口调用支付订单接口提取参数后面使用，后面使用进行更改覆盖

# print(ABS_PATH)
# E:\AiDong\pythonProject\MDX\apiFrame\apiFrame\config.py
# print(DIR_NAME)
# E:\AiDong\pythonProject\MDX\apiFrame\apiFrame