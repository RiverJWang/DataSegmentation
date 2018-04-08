import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_name = 'D:\\DDesktop\\zJBS\\Velocity\\2015-08-11gps _ Velocity.csv'
reader = pd.read_csv(file_name)
data = reader.values
names = data[:,0]
y = data[:,1]
x = range(len(names))

plt.plot(x,y)
#plt.xticks(x, names, rotation=45)
plt.margins(0.08)
plt.subplots_adjust(bottom=0.15)
ann = plt.annotate(u"6546,lasting 2700s",xy=(6546,250), #注解
                    xytext=(4,4),size=10,
                    va="center",ha="center",
                    bbox=dict(boxstyle='sawtooth',fc="w"),
                    arrowprops=dict(arrowstyle="-|>",#"-|>"代表箭头头上是实心的
                                    connectionstyle="angle,rad=0.4",fc='r')#rad代表箭头是否是弯的，+-定义弯的方向
                    )

plt.show()