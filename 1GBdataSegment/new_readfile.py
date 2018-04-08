import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import dask.dataframe as dd
import time
import numpy as np
start_time = time.time()
begin_time = time.time()
def time_count():
    '''统计程序执行到此刻所耗时间'''
    global start_time
    print("Time elapse:%.3f s, total elapse:%.3f min" %(time.time() - start_time,
                                                        (time.time() - begin_time)/60.0))
    start_time = time.time()

file_name = 'D:\\aData\\jbs\\X\\20150811 _ SX3 _  114605.csv'
# reader = pd.read_csv(file_name, iterator=True)

loop = True
ChunkSize = 5000 # 采样频率5,000点/秒
chunks = [] # 定义一个‘块’
variances = [] # 定义一个‘方差表’
index = [] # 定义一个‘方差下标表’
left_interval = [] # 定义一个‘方差左区间表’
right_interval = [] # 定义一个‘方差右区间表’
interval = [] # 定义一个‘区间’

reader = dd.read_csv(file_name,sep=',') # 用dask读取文件，存入内存
computer = reader.compute()# .compute是啥意思？ 定义一个computer的变量，并赋值
lines = len(computer) # 定义一个lines变量，大小是computer的个数
number = lines/5000 -1 # 因为下面的 5000*（i+1），所以要减一，且每次读取5,000个，也就是一秒
number = int(number) # 确保是整数
y = computer.values # 每个类型的取值函数都不一样。
time_count()
for i in range(number): # 对【a，b】区间算方差，存入‘方差表’
    a = 5000 * i
    b = 5000 * (i + 1)
    temp = computer.iloc[a:b,0] # 这里是numpy的dataframe读取方式，下面那个是list读取
    variance = np.var(temp)  # computing  every 5,000 right_interval's variance
    variances.append(variance) # appending variance to variances
time_count()

# index

for j in range(number): # ‘方差表’里面元素总数是number个。对‘方差表’进行查找，小于0.04的方差存入‘方差下标表’。
    if variances[j] < 0.04:
        index.append(j)
index_length = len(index) - 1
for i in range(index_length): # 对‘方差下标表’进行查找，相隔100个点距离的存入points‘方差右区间表’
    if index[i+1]-index[i] > 100:
        right_interval.append(index[i])
right_interval.append(index[index_length]) # 补充右区间完整
left_interval.append(index[0]) # 开始查找左区间
for i in range(index_length):
    if index[i+1]-index[i] > 100:
        left_interval.append(index[i + 1])
for i in range(6): # 合并左右区间
    a = left_interval[i]
    b = right_interval[i]
    print(a,b)
    locals()['block'+str(i)] = computer.iloc[left_interval[i]:right_interval[i],0]
    



# # figure -----------------------------------
y1 = variances
x1 = range(number)

plt.subplot(1, 1, 1)
plt.plot(x1, y1, 'o-',markerfacecolor='yellow',markersize=2)
plt.title('subplots')
plt.ylabel('Damped oscillation')

plt.show()
# #--------------------------------------------
# y1 = block1 # 怎么办，这种情况
# number = len(block1)
# x1 = range(number)
#
# plt.subplot(1, 1, 1)
# plt.plot(x1, y1, 'o-',markerfacecolor='yellow',markersize=2)
# plt.title('subplots')
# plt.ylabel('Damped oscillation')
#
# plt.show()

# ------------------
# while loop:
#      try:
#         chunk = reader.get_chunk(ChunkSize)  #
#         variance = np.var(chunk)
#         variances.append(variance)
# #       chunks.append(chunk)
#      except StopIteration:
#         loop = False
#         print('Iteration is stopped...')
#----------------------

# df = pd.concat(chunks, ignore_index=True)  # ??
# v = var(df)
# m = mean(df)
# print(v)
# print(m)
#---------------------------------------------
# ymax = np.max(y)
# ymin = np.min(y)
# if ymin <-80:
#     ymin = -5
# fig = plt.figure(figsize=(20, 9))          # 修改画板尺寸为：18 * 9；
# ax = fig.add_subplot(1, 1, 1)
# plt.axis('tight')                    # 数据紧凑型绘制
# ax.set_ylim(ymin-1,ymax+1)              # 数据y 显示范围, 剔除数据小于-100的值
# ax.set_xlim(0,lines)
# ax.grid(True)
# plt.xticks(fontsize=16)  # 设置x坐标轴刻度字体大小
# plt.yticks(fontsize=16)  # 设置y坐标轴刻度字体大小
# # plt.legend()                          # 绘制图例
# ax.plot(y, 'r', lw=0.2)
# # plt.plot(y, 'r', lw=0.2)            # 表示绘图线宽为0.2，用红色线条；
# plt.xlabel('time', fontsize=20)  # 表示X轴标签
# plt.ylabel('velocity (kM/h)', fontsize=20)  # 表示Y轴标签；
# plt.title('All velocity of GPS', fontsize=20)  # 表示添加标题；如图所示
# mpl.rcParams['agg.path.chunksize'] = 2000
# plt.savefig('testt2.png', format='png', dpi=600)
#----------------------------------
# plt.show()
# plt.clf()
# plt.close()

#-----------------------------------
# plt.plot(reader)