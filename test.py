# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

print('loading data1.txt ... ...')
data1 = np.loadtxt(r'C:\Users\40664\Desktop\DataSegmentation\test.txt',delimiter=' ')
print(data1)
print(data1.shape)
print("type of data1:",type(data1))
print("type of element of data1:",data1.dtype)
print("\n")
