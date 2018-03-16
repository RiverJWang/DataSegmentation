import pandas as pd
data = pd.read_table('D:\\aData\\jbs\\72Right_Vertical_Data\\20150711 _ SX3 _  002351.txt', iterator=True)
chunk = data.get_chunk(50) 