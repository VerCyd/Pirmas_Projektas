import random

import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import psycopg2
import time
from datetime import datetime, timedelta

data = pd.read_csv('sales_data.csv', encoding = "iso-8859-1")
df = pd.DataFrame(data)
print(df.head(5))

vidutine_kaina = df["PRICEEACH"].mean().round(2)
vid_prad_kiekis = df["QUANTITYORDERED"].mean()
print("vidutine kaina", vidutine_kaina)
print(f"\n vidutinis parduotas kiekis", vid_prad_kiekis)

df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])
df['Metai'] = df['ORDERDATE'].dt.year
df['Mėnuo'] = df['ORDERDATE'].dt.month
df['Diena'] = df['ORDERDATE'].dt.day
print(f'\n', df)

Mėn_suma = df.groupby(['Metai', 'Mėnuo', 'Diena'])['QUANTITYORDERED'].sum()
Mėn_suma.plot(kind= 'line', color='skyblue')
plt.xticks(rotation = 90)
plt.xlabel('Data')
plt.ylabel('Pardavimai')
plt.title('pardavimų skaičius laiko atžvilgiu')
plt.show()

data = {"Stulpelis_id": [i+1 for i in range(10)],
        "data": [(datetime(2023, 1, 1) + timedelta(days = random.randint(0,364))).strftime("%Y-%m-%d") for _ in range(10)],
        "Pardavimai": [random.randint(5, 150) for _ in range (10)]
        }
df = pd.DataFrame(data)
print(df)


