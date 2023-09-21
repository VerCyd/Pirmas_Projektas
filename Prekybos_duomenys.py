# 2023.09.21
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import psycopg2
import time

# Apskaičiuokite kiekvieno produkto mėnesinį pardavimų sumažėjimą per metus.
# Sukurkite Matplotlib grafiką, kuriame būtų pateikti šie mėnesiniai sumažėjimai
# kiekvienam produktui (x ašis - mėnesiai, y ašis - sumažėjimas, produkto
# pavadinimas - linijos pavadinimas). Pridėkite pavadinimus ašims
# ir bendrą pavadinimą grafikui.


data = pd.read_csv('prekybos_duomenys.csv')
df = pd.DataFrame(data)
# print(df)

df["Data"] = pd.to_datetime(df["Data"])
df["Metai"] = df["Data"].dt.year
df["Menuo"] = df["Data"].dt.month
df["Diena"] = df["Data"].dt.day
print(f"\n", df)
#
# products = df["Produktas"]
# results = pd.DataFrame(columns = ["Produktas", "Metai", "Menuo", "Sumazejimas"])
# for product in products:
#     product_df = df[df["Produktas"] == product]
#     for year in product_df["Metai"].unique():
#         for month in range(1,13):
#             if product_df[(product_df["Metai"] == year) & (product_df["Menuo"] == month)].shape[0]> 0:
#                 sales = product_df[(product_df["Metai"] == year) & (product_df["Menuo"] == month)]["Pardavimai"].sum()
#                 if month > 1:
#                     praeje_metai = year
#                     praejes_menuo = month -1
#                 else:
#                     praeje_metai = year -1
#                     praejes_menuo = 12
#                 praeje_pardavimai = \
#                 product_df[(product_df["Metai"] == praeje_metai) & (product_df["Menuo"] == praejes_menuo)]["Pardavimai"].sum()
#                 decrease = praeje_pardavimai - sales
#                 results = pd.concat([results, pd.DataFrame([[product, year, month, decrease]], columns = results.columns)], ignore_index = True)
# print(results)
#
# pagal_produkta = df.groupby(["Menuo"])["Pardavimai"].sum()
# # print(Menesio_suma)
#
#
# plt.plot(results["Produktas"], results["Sumazejimas"], label = "linija", color = "blue", linestyle = "--", marker = "o")
# plt.xticks(rotation = 90)
# plt.legend()
# plt.xlabel("Menesiai")
# plt.ylabel("Sumazejimas")
# plt.title("Pardavimu mazejimas")
# plt.show()




