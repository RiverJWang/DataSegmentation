import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean, ptp, var, std
import numpy as np

file_name = 'D:\\aData\\jbs\\72Right_Vertical_Data\\20150727 _ SX3 _  060407.txt'
reader = pd.read_csv(file_name, iterator=True)

loop = True
ChunkSize = 1024 * 100
chunks = []
while loop:
    try:
        chunk = reader.get_chunk(ChunkSize)  # 读取一个chunk，怎么保证是接着读下去的呢？
        chunks.append(chunk)
    except StopIteration:
        loop = False
        print('Iteration is stopped...')
df = pd.concat(chunks, ignore_index=True).values  # ??
v = np.var(df)
m = np.mean(df)
print(v)
print(m)