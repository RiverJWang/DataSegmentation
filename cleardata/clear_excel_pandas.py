import pandas as pd
import numpy as np

# set
file_name_set = 'D:/D盘桌面/z江宝山/联系data/72 _ cross std Clearing record -2.xlsx'
df_set = pd.read_excel(file_name_set)
col_set = df_set.shape[0]
df_x, df_y, df_z = df_set.values[:,0],df_set.values[:,1],df_set.values[:,2]
config_size = df_x.size
lists3D = [[] for i in range(3)]
subset3D = [[] for i in range(3)]
inx = 1
for i in range(0, config_size):
    a, b, c = df_x[i], df_y[i], df_z[i]
    if b != 0 and len(a) > 8:
        plusa = df_x[i+1:i+1+b]
        plusb = df_y[i+1:i+1+b]
        plusc = df_z[i+1:i+1+b]
        lists3D[:, 0, i] = plusa   # 假设每一组都放进了一个二维空间
        lists3D[:, 1, i] = plusb
        lists3D[:, 2, i] = plusc
# 同样的，def 对子集进行操作，得到subset3D,每一组都放进了一个二维空间
page = lists3D.shape[2]
for i in range(0,page): # 只检测第一列
    aa, bb = lists3D(0, 0, i),lists3D(0, 1, i)  # page的名称
    aaa, bbb= subset3D(0, 0, i),subset3D(0, 1, i)
    if aa == bb and bb!=0 and bbb!=0:
    for  : # page里的循环
        if cell[k] == subset_cell[]:
            del cell[k]




# subset
file_name_subset = open('D:/D盘桌面/z江宝山/联系data/72Crossl Semi-quiescent Data Clearing Record.csv')
df_subset = pd.read_csv(file_name_subset, encoding='utf-8')
col_subset = df_subset.shape[0]


# Q1:open和不open有什么不一样？
print
# for row in range()
