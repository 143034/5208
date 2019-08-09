from matplotlib import pyplot as plt


x = range(2,20,2)

y = [5,8,6,5,4,11,22,33,11]
#设置图片大小
plt.figure(figsize = (20,8), dpi = 80)
plt.plot(x,y)
#设置x轴的刻度
#plt.xticks(range(2,20))
#plt.savefig("./t1.svg")
plt.show()
#my_font = font_manager.FontProperties(fname = "C:/Windows/Fonts/simsun.ttc")
#plt.xticks(range(0,120,5),x_label[::5],rotation=90,fontproperties = my_font)
