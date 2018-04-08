import pandas as pd
import numpy as np
import csv
import xlrd

# 读取文件，并且获取总集和子集的dataframe
f1 = open("D:/D盘桌面/z江宝山/联系data/72 _ cross std Clearing record -2.csv", 'rb')
df1 = pd.read_csv(f1, header=0)
dfA = df1.values
size1 = df1.shape[0]
f2 = open('D:/D盘桌面/z江宝山/联系data/72Crossl Semi-quiescent Data Clearing Record.csv', 'rb')
df2 = pd.read_csv(f2, header=0)
dfB = df2.values
size2 = df2.shape[0]
save_data = []

# # originaldata_name = '72 _ cross std Clearing record -2.csv'
# # clearingdata_name = '72Crossl Semi-quiescent Data Clearing Record.csv'
# # orginal_file1 = file_path + '\\' + originaldata_name
# # orginal_file2 = file_path + '\\' + clearingdata_name
# # savefile = save_path + '\\' + 'Normaldata Record.csv'  #
# f1 = open('D:/D盘桌面/z江宝山/联系data/72 _ cross std Clearing record -2.csv', 'rb')
# f2 = open('D:/D盘桌面/z江宝山/联系data/72Crossl Semi-quiescent Data Clearing Record.csv', 'rb')
# dfA = pd.read_csv(f1, header=0).values
# dfB = pd.read_csv(f2, header=0).values
# size1 = dfA.shape[0]
# size2 = dfB.shape[0]
# save_data = []
# inx = 1

for i in range(0, size1):
    a0, a1, a2 = dfA[i, 0], dfA[i, 1], dfA[i, 2]
    if a1 != 0 and not a0.isdigit():
        for j in range(0, size2):
            b0, b1, b2 = dfB[j, 0], dfB[j, 1], dfB[j, 2]
            chunk_A = dfA[i + 1:i + 1 + a1, :]
            chunk_B = dfB[j + 1:j + 1 + b1, :]
            chunkA_size = chunk_A.shape[0]
            chunkB_size = chunk_B.shape[0]
            if b1 == 0:
                save_data.append(dfA[i, :])
                save_data.extend(chunk_A)
                break  # for j in range(0, size2):
            elif b1 != 0 and a0 == b0:
                num = a1 - b1
                dfA[i, 1] = num
                dfA[i, 2] = 'NAN'
                save_data.append(dfA[i, :])
                for an in range(0, chunkA_size):
                    k = 0
                    for bn in range(0, chunkB_size):
                        if chunk_A[an, 0] != chunk_B[bn, 0]:
                            k += 1
                    if k == chunkB_size:
                        save_data.append(chunk_A[an, :])
                break
df3 = pd.DataFrame(save_data, columns=['start time', 'end time', 'delta time'])
df3.to_csv('final_data2.csv', index=False, sep= ',')