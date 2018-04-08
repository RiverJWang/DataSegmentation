# with open('filename') as file:
#     for line in file:
#         do_things(line)
# 内库要用with，pandas就不用。

# 1 一次性加载到字符串对象
# file = open('myfile.txt', 'r')
# print(file.read())

# 2 一次性加载后逐行读取
# file = open('myfile.txt', 'r')
# print(file.read())

# 3 直接逐行读取
# for line in open('myfile.txt','r'):
# print(line, end='')


