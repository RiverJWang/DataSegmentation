import pandas as pd
file_name = 'D:\\aData\\jbs\\72Right_Vertical_Data\\20150711 _ SX3 _  002351.txt'
reader = pd.read_csv(file_name)
try:
  df = reader.get_chunk(1024 * 1024 * 10) # 读取文件，块的大小，只读取一次
except StopIteration:
  print('Iteration is stopped...')

loop = True
ChunkSize = 1024 * 1000
chunks = []
while loop:
  try:
    chunk = reader.get_chunk(ChunkSize) # 读取一个chunk，怎么保证是接着读下去的呢？
    chunks.append(chunk)
  except StopIteration:
    loop = False
    print('Iteration is stopped...')
df = pd.concat(chunks, ignore_index = True) # ??