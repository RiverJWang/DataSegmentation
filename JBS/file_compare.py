#coding=utf-8
# fileencoding=utf-8
"""
从csv文件中比较两个文件的不同，抽取不同值并保存到文件
"""
import os
import numpy as np
import dask.dataframe as dd
import pandas as pd
import datetime
import time
import matplotlib.pyplot as plt
import matplotlib as mpl

startDtime = datetime.datetime.now()                         #记录当店运行时间
print("Start time: "+str(startDtime))

start_time = time.time()
begin_time = time.time()
def time_count():
    '''统计程序执行到此刻所耗时间'''
    global start_time
    print("Time elapse:%.3f s, total elapse:%.3f min" %(time.time() - start_time,
                                                        (time.time() - begin_time)/60.0))
    start_time = time.time()

def filecompare(file_path, save_path):
    '''读取csv文本数据，并将其绘制出指定图形'''

    # configname = os.listdir(file_path)
    originaldata_name = 'origin data.csv'
    clearingdata_name = 'clearing data.csv'
    orginal_file1 = file_path + '\\' + originaldata_name
    orginal_file2 = file_path + '\\' + clearingdata_name
    savefile = save_path + '\\' + 'Normaldata Record' + '.csv'  #
    dfA = pd.read_csv(orginal_file1, header=0).values
    dfB = pd.read_csv(orginal_file2, header=0).values
    dfA_size = dfA.shape[0]
    dfB_size = dfB.shape[0]

    save_data = []#[] for i in range(3)]# 定义一个三维列表
    inx = 1
    for i in range(0, dfA_size):  # 遍历该文件
        x_a, x_b, x_c = dfA[i,0], dfA[i,1], dfA[i,2]     # 获取原始数据中第i行内容
        if x_b != 0 and not x_a.isdigit():                   # 判定该行为标志行还是数据行
            for j in range(0, dfB_size):  # 遍历该文件
                y_a, y_b, y_c = dfB[j, 0], dfB[j, 1], dfB[j, 2]  # 获取原始数据中第i行内容
                chunk_A = dfA[i + 1:i + 1 + x_b, :]  # 获取分块A数据内容
                chunk_B = dfB[j + 1:j + 1 + y_b, :]  # 获取分块B数据内容
                chunkA_size = chunk_A.shape[0]
                chunkB_size = chunk_B.shape[0]
                if y_b ==0:
                    save_data.append(dfA[i,:])
                    save_data.extend(chunk_A)
                    break
                elif y_b!=0 and x_a == y_a:
                    ###一下代码可以做优化
                    num = x_b - y_b
                    dfA[i, 1] = num
                    dfA[i, 2] = 'NaN'
                    save_data.append(dfA[i, :])
                    for xk in range(0, chunkA_size):
                        v = 0
                        for yk in range(0, chunkB_size):
                            if chunk_A[xk,0]!=chunk_B[yk,0]:
                                v +=1
                        if v==chunkB_size:
                            save_data.append(chunk_A[xk,:])
                    break

    normal_re = pd.DataFrame(save_data, columns=['startTime' , 'endTime' , 'deltatime'])
    normal_re.to_csv(savefile, index = False, sep = ',')

    print(u'数据处理完毕！')

if __name__ == "__main__":
    open_path = 'E:\\Data\\test3.16'          # 目标数据文件路径
    save_path = 'E:\\Data\\test3.16'       # 目标存储文件路径

    filecompare(open_path, save_path)




