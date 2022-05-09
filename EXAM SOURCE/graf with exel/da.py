import imp


import matplotlib.pyplot as plt
import pandas as pd

figa = plt.figure()
chart1 = figa.add_subplot(221)
chart2 = figa.add_subplot(222)
chart3 = figa.add_subplot(223)
chart4 = figa.add_subplot(224)


ekos_bokes = pd.read_excel("ocenka.xlsx", sheet_name="Sheet1")
chart1.set_title("Anglish")
chart1.bar(ekos_bokes["Skolēns"], ekos_bokes["Angļu valoda"])
chart2.set_title("Matika")
chart2.bar(ekos_bokes["Skolēns"], ekos_bokes["Matemātika"])
chart3.set_title("Latgoliski")
chart3.bar(ekos_bokes["Skolēns"], ekos_bokes["Latviešu valoda"])
chart4.set_title("Fizika")
chart4.bar(ekos_bokes["Skolēns"], ekos_bokes["Fizika"])




plt.show()