import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("bmh")
bins = [10,20,30,40,50,60,70,80,90,100]
statistika = pd.read_csv("publikcijas.csv")
plt.plot(statistika["Male Researchers"], label="Viriesi")
plt.plot(statistika["Female Researchers"], label="Sieviesu")

plt.title("Zinatniskas publikacijas pa polu")
plt.xlabel("Dzimumi")
plt.ylabel("Dzimumi")
plt.xticks(rotation=45)
plt.legend
plt.show()