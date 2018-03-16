import pandas as pd
file_name = 'D:\\aData\\jbs\\72Right_Vertical_Data\\20150711 _ SX3 _  002351.txt'
reader = pd.read_csv(file_name, iterator = True)

loop = True
ChunkSize = 1024 * 10000
chunks = []
while loop:
  try:
    chunk = reader.get_chunk(ChunkSize) # 读取一个chunk，怎么保证是接着读下去的呢？
    chunks.append(chunk)
  except StopIteration:
    loop = False
    print('Iteration is stopped...')
df = pd.concat(chunks, ignore_index = True) # ??


print(df)