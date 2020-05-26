# -*- coding: utf-8 -*-
# @Author : Angious
# @Github : https://github.com/Angious
# @FileName: main.py
# @Software: PyCharm
# @Time : 2020/5/26 13:03

from demo import GetInfo
if __name__ == '__main__':
    for i in range(0, 10):
        data = GetInfo(i*25)
        print(data)