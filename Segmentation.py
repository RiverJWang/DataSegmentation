# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

print('loading data1.txt ... ...')
data1 = np.loadtxt(r'D:\aData\jbs\72Right_Vertical_Data\20150711 _ SX3 _  002351.txt',delimiter=' ')
print(data1)
print(data1.shape)
print("type of data1:",type(data1))
print("type of element of data1:",data1.dtype)
print("\n")

print("------usecols test:------")
#use 2th column
test=np.loadtxt("data1.txt",delimiter=' ',usecols=(1,))
print(test)
print(test.shape)
print("type of test:",type(test))
print("type of element of test:",test.dtype)
