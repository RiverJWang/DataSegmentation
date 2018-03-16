def read_file_by_chunks(file_name, chunk_size = 100):   
  file_object = open(file_name, 'rb') 
  while True: 
    chunk = file_object.read(chunk_size) 
    if not chunk: 
      break 
    yield chunk 
  file_object.close() 
for chunk in read_file_by_chunks('D:\\aData\\testdata\\test.txt', 1): 
  print(chunk)
