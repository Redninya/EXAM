import imp
import matplotlib.pyplot as plt
import pandas as pd

figura = plt.figure()
plt.suptitle("Daris Mivrniks jadad")
chart1 = figura.add_subplot(121) #rindu skaits, colonnu skaits, grafika poz. lapā
chart2 = figura.add_subplot(122)
chart3 = figura.add_subplot(223)
chart4 = figura.add_subplot(224)


prices = pd.read_csv("gas_prices.csv")
chart1.plot(prices.Year, prices.Canada)

for x,y in zip(prices.Year, prices.Canada):
    chart1.annotate(y, (x,y), ha="left", va="top")
    #ha = left/right/center
    #va = top/bottom/center
    

chart2.bar_label(chart2.barh(prices.Year, prices.Germany))

chart3.scatter(prices.Year, prices.France)

chart4.bar(prices.Year, prices.Australia)

plt.show()