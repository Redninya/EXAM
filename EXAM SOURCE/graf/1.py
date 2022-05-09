from turtle import width
import matplotlib.pyplot as plt
import numpy

plt.style.use("bmh")
figura = plt.figure(1)
figura.suptitle("ZONA")
chart1 = figura.add_subplot(221) #rindu skaits, colonnu skaits, grafika poz. lapā
chart2 = figura.add_subplot(222)
chart3 = figura.add_subplot(223) 
chart4 = figura.add_subplot(224)

vecums = [120,80,30]
labels1 = ["ONE","TWO","FOUR"]
colors1 = ["purple", "yellow", "green"]
explode1 = (0, 0.1, 0.2)
chart1.set_title("ANATOLIJ")

chart1.pie(vecums, labels=labels1, colors=colors1, autopct="%1.1f%%", 
explode=explode1, pctdistance=0.1, rotatelabels=True, shadow=True,
wedgeprops={"edgecolor":"orange", "linewidth":2})


edge = [90, 12, 43, 54, 15]
chart2.hist(edge)
chart2.set_title("KOLJA")




xAss1 = [2011, 2012, 2013, 2014, 2015]
yAss1 = [12, 23, 34, 12, 3]
yAss2 = [34, 54, 23, 45, 56]
width = 0.3
x = numpy.arange(len(xAss1)) #сгрупировать по оси x
chart3.bar(x - width/2, yAss1, width)
chart3.bar(x + width/2, yAss2, width)
chart3.set_title("LOSARA")


xAss = [1232, 2013, 2312, 3423]
yAss = [54,23,56,87]
chart4.plot(xAss, yAss)
chart4.set_title("Lines")
chart4.set_xlabel("Gadi")
chart4.set_ylabel("Cena, EUR")

plt.show()