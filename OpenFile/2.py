# 更规范的方法 
file = open('D:\\aData\\testdata\\test.txt')
try:
  text1 = file.read()
  print(text1)
finally:
  file.close()