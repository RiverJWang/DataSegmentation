def read_file_by_chunks(file_name, chunk_size = 100):   
  file_object = open(file_name, 'rb') 
  while True: 
    chunk = file_object.read(chunk_size) 
    if not chunk: 
      break 
    yield chunk 
  file_object.close() 
for chunk in read_file_by_chunks('D:\\aData\\jbs\\72Right_Vertical_Data\\20150711 _ SX3 _  002351.txt', 1):
  print(chunk)
