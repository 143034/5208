from matplotlib import pyplot as plt
import random
from matplotlib import font_manager
#设置中文字体
my_font = font_manager.FontProperties(fname = "C:/Windows/Fonts/simsun.ttc")
y = [random.randint(20,35)  for i in range(120)]
x = range(120)
plt.figure(figsize=(20,8),dpi = 80)
x_label = ["十点{}分".format(i) for i in range(60)]
x_label += ["十一点{}分".format(i) for i in range(60)]
#参数(数组(x轴的刻度)，数组(x下标文字)，角度，字体)
plt.xticks(range(0,120,5),x_label[::5],rotation=45,fontproperties = my_font)
plt.plot(x,y)
plt.show()
