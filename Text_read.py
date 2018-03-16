#coding=utf-8
'''
完成数据清洗后，再从txt中提取数据，并写入csv文件
'''
import os
import numpy as np
import pandas as pd
import datetime

startDtime = datetime.datetime.now()                         #记录当店运行时间
print("Start time: "+str(startDtime))

def recordtime(startDtime):
    endDtime = datetime.datetime.now()
    print("End time: " + str(endDtime))
    timedelta = endDtime - startDtime
    print("Now, it only cost: " + str(timedelta) + ' seconds')  # 显示程序花费时间

def readAndWrite(file_path, save_path, f):
    txt_files = os.listdir(file_path)
    print(u'一共发现%s个Txt文件待处理' % len(txt_files))
    ids = []
    ids.append('id')
    itime = []
    itime.append('time')
    values = []
    values.append('value\n')
    j = 1
    for i in txt_files:
        print(u'正在拼命处理第%s个文件中，请稍后~~ ' % j)
        ittime = i.split('.')
        itt =ittime[0]
        txt_path = file_path + '\\' + i
        save_file = save_path + '\\' + 'LZX_vertical72_combine ' + str(f) + ' .csv'
        errordata_file = save_path + '\\' + 'abnormal_ LZX_vertical72_combine ' + str(f) + ' .csv'
        with open(txt_path) as reader, open(save_file, 'a') as writer, open(errordata_file, 'a') as writer1:
            for index, line in enumerate(reader):
                if index % f == 0:
                    writer.write(line)
                    if float(line) < -80:  # < 0 or float(line) > 6:
                        ids.append(str(index))
                        itime.append(itt)
                        values.append(line)
                        for i in zip(ids,itime, values):
                            writer1.write(i[0] + ',' + i[1]+ ',' + i[2])
        j = j+1
    print(u'数据提取完毕！')

if __name__ == "__main__":
    open_path = 'D:\\7车2轴右侧轴箱\\7车2轴右侧轴箱垂向'          # 目标数据文件路径
    save_path = 'D:\\Data_Analysis\\ExtractData'       # 目标存储文件路径
    f = 1000

    readAndWrite(open_path, save_path, f)
    endDtime = datetime.datetime.now()
    print("End time: " + str(endDtime))
    timedelta = endDtime - startDtime
    print("Total cost time: " + str(timedelta))  # 显示程序花费时间



