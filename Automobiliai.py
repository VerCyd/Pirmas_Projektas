import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import psycopg2
import time

# +Išspausdinkite pirmas 5 eilutes;
data = pd.read_csv('automobiliai.csv')
df = pd.DataFrame(data)
# print(df.head(5))

# Filtruokite automobilius pagal jų kainą (pvz., kaina mažesnė nei 10 000). Išspausdinkite šiuos automobilius;
pigiausi = df[df["Kaina"] < 20000 ]
# print(pigiausi)

# Suskirstykite automobilius pagal gamintoją ir susumuokite kiekvieno gamintojo automobilių kiekius.
# df["Markė"] = df[df["Markė"]].sum()
# print(df)
par_auto_suma = df.groupby(["Markė"])["Modelis"].count()
# print(par_auto_suma)

# Atvaizduokite stulpelinėje diagramoje automobilių kiekius;
x = df["Markė"]
y = df["Modelis"]
plt.hist(x, bins = 5, color = "red", alpha = 1, edgecolor = "black")
plt.legend()
plt.align("Mid")
plt.xlabel("Marke")
plt.ylabel("Parduodamu automobiliu suma")
plt.title("Automobiliai")
plt.show()

