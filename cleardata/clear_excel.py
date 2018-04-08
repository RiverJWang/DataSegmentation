# 思路

# ---建议
# 1. 文件读取；
# 2. 关键数据（字符串）的提取和判断；
# 3. list or set or tuple（形式你自己选取）的创建及保存；
# 4. 数据的保存（to_csv or to_excel）

# 1-读取excel和csv
# 2-
import xlrd
import csv
# 读取  文件->sheets->行，列，单元格，或者要处理的区块
file_name_set = 'D:/D盘桌面/z江宝山/联系data/72 _ cross std Clearing record -2.xlsx'
data_set = xlrd.open_workbook(file_name_set)
table_set = data_set.sheets()[0]
print(table_set)

file_name_subset = 'D:/D盘桌面/z江宝山/联系data/72Crossl Semi-quiescent Data Clearing Record.csv'
data_subset = csv.reader(ofile_name_subset)
table_subset = data_subset.sheets()[0]
print(table_subset)