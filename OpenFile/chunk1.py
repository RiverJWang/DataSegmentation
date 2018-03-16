import time
start_time = time.time()
begin_time = time.time()
def time_count():
    '''统计程序执行到此刻所耗时间'''
    global start_time
    print("Time elapse:%.3f s, total elapse:%.3f min" %(time.time() - start_time,
                                                        (time.time() - begin_time)/60.0))
    start_time = time.time()

def read_file_by_chunks(file_name, chunk_size = 1024 * 1024000):   
  file_object = open(file_name, 'rb') 
  while True: 
    chunk = file_object.read(chunk_size) 
    if not chunk: 
      break 
    yield chunk 
  file_object.close() 


  
data_name = 'D:\\aData\\jbs\\72Right_Vertical_Data\\20150711 _ SX3 _  002351.txt'

for chunk in read_file_by_chunks(data_name):
  chunk_size = len(chunk)
  print(chunk_size)
  time_count()
	