import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import psycopg2
import time

## +Įkelkite kitą CSV failą su duomenimis apie studentų egzaminų rezultatus.
## b. Pateikite histogramą, kuri atvaizduotų studentų matematikos egzaminų rezultatus.
## c. Nustatykite tinkamą stulpelių (bins) skaičių, kad histograma būtų aiški ir informatyvi.
## d. Pridėkite ašių pavadinimus ir pavadinimą grafiko viršuje.
## Duomenų grupavimas ir pie grafikas:
## a. Grupuokite studentų egzaminų duomenis pagal lytį (vyrus ir moteris).
## b. Apskaičiuokite vidutinius rezultatus kiekvienoje grupėje.
## c. Pateikite pie grafiką, kuriame būtų rodoma, kiek procentų vyrų ir moterų pasiekė aukštesnius
## nei vidutinius rezultatus.
## a. Sukurkite tris linijinius grafikus viename paveiksle (subplots). Kiekvienas grafikas turėtų
## atvaizduoti skirtingus duomenų rinkinius (pavyzdžiui, kainas skirtinguose miestuose).
## b. Kiekvienam grafikui priskirkite ašių pavadinimus, pavadinimus ir legendas.
## c. Pateikite visus tris grafikus viename paveiksle.

data = pd.read_csv('egzaminai.csv')
df = pd.DataFrame(data)
# print(df)

# x = ["Student ID"]
# y = ["Math Score"]
# plt.hist(x, bins = 100, color = "green", alpha = 0.7, edgecolor = "black")
# plt.hist(y, bins = 100, color = "green", alpha = 0.7, edgecolor = "black")
# plt.xlabel("Student_ID")
# plt.ylabel("Math_Score")
# # plt.title("Matematikos egzaminu rezultatai")
# plt.show()

x = ["Student ID"]
plt.hist(x, grid=True, bins=20, rwidth=0.9, color='#607c8e')
plt.title('Commute Times for 1,000 Commuters')
plt.xlabel('Student ID')
plt.ylabel('Math Score')
plt.show()