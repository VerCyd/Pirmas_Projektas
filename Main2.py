import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import psycopg2
import time
import numpy as np

# +Sukurkite Pandas duomenų lentelę su 5 eilutėmis ir 3 stulpeliais.
# +Pavadinkite stulpelius "Vardas", "Amžius" ir "Miestas".
# +Įtraukite naują eilutę į lentelę su duomenimis: "Jonas", 30, "Vilnius".
# Išspausdinkite pirmas 3 eilutes iš lentelės.
# +Išspausdinkite stulpelį "Amžius" visų eilučių atveju.
# Atrinkite visus žmones, kurių amžius yra mažesnis nei 25.
# Sukurkite naują stulpelį "Gimimo metai" pagal esamą stulpelį "Amžius". Paskaičiuokite gimimo metus pagal 2023 metus.
# Ištrinkite eilutę su "Jonas" iš lentelės.
# Išsaugokite lentelę į CSV failą pavadinimu "duomenys.csv".

# duomenys = {"Vardas": ["Jonis", "Ieva", "Petras", "Ona", "Simas"],
#             "Amzius": [20, 19, 7, 23, 22],
#             "Miestas": ["Vilnius", "Ignalina", "Siauliai", "Kaunas", "Visaginas"]
#             }
# df = pd.DataFrame(duomenys)
# # print(df)
# df.loc[len(df.index)] = ["Jonas", 30, "Vilnius"]
# print(df)



# metai = df["Amzius"]
# print("Amzius")
# print(metai)

# Pamoka 2023-09-18
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host = "localhost",
#         port = 5432,
#         database = "products",
#         user = "postgres",
#         password = "19950208m"
#     )
#     cursor = connection.cursor()
#
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS varle_products(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255),
#         price DECIMAL(10,2),
#         quantity INT)
#     """
#     # cursor.execute(create_table_query)
#     # print("Table created successfully!")
#     for i in range(1,5):
#         url = f"https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/{i}"
#         response = requests.get(url)
#         # print(response.status_code)
#
#         soup = BeautifulSoup(response.content, "html.parser")
#         product_elements = soup.find_all("div", class_ = "GRID_ITEM")
#         # print(product_elements)
#
#         product_data = []
#         for product_element in product_elements:
#             product_name = product_element.find("div", class_ = "product-title").text.strip()
#             product_price = float(product_element.find("span", class_ = "price-value").text.strip().replace("€",""))
#             product_quantity = product_element.find("b").text.strip()[:1]
#             # print(f"Adding products to the list: {product_name}")
#             # time.sleep(2)
#             # product_data.append((product_name, product_price, product_quantity))
#             # print("Products inserted into list successfully!")
#
#             insert_query = "INSERT INTO varle_products (name, price, quantity) VALUES (%s, %s, %s)"
#             cursor.execute(insert_query, (product_name, product_price, product_quantity))
#             connection.commit()
#
#         df = pd.DataFrame(product_data, columns=["name", "price", "quantity"])
#         print(df)
#         select_query = "SELECT * FROM varle_products"
#         cursor.execute(select_query)
#         rows = cursor.fetchall()
#         df = pd.DataFrame(rows, columns=["id", "name", "price", "quantity"])
#         print(df)
#
# if __name__ == "__main__":
#     create_and_insert_product()

# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="ZaislaiProducts",
#         user="postgres",
#         password="Dek***123*"
#     )
#     cursor = connection.cursor()
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS zaislai_products (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255),
#         price DECIMAL(10,2)
#         )
#     """
#     cursor.execute(create_table_query)
#     print('Table created successfully')
#     url = 'https://www.1a.lt/c/zaislu-pasaulis-20-zaislams-su-kodu/87w'
#     response = requests.get(url)
#     print(response.status_code)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     product_elements = soup.find_all('div', class_='catalog-taxons-products-container__grid-row')
#     # print(product_elements)
#     product_data = []
#     for product_element in product_elements:
#         product_name = product_element.find('div', class_='catalog-taxons-product__files').text.strip()
#         product_price = float(product_element.find('span', class_='catalog-taxons-product-price__item-price').text.strip().replace('€', '').replace('vnt.', '').replace('\n\n/', '').replace(' ','').replace(',', '.'))
#         print(f'Pridedame produktus i sarasa: {product_name}')
#         product_data.append((product_name, product_price))
#         insert_query = "INSERT INTO zaislai_products (name, price) VALUES(%s, %s)"
#         cursor.execute(insert_query, (product_name, product_price))
#         print(f'Products inserted into list succesfully!')
#         connection.commit()
#     # df=pd.DataFrame(product_data, columns=['name', 'price'])
#     # print(df)
#     select_query = "SELECT * FROM zaislai_products"
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     df=pd.DataFrame(rows, columns = ['id', 'name', 'price'])
#     print(df)
# if __name__ =='__main__':
#     create_and_insert_product()


# url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"
# # response = requests.get(url)
# # print(response.status_code)
# # soup = BeautifulSoup(response.content, 'html.parser')
# # forecast = soup.find_all("div", class_ = "forecast-day")
# # week_days = soup.find_all("span", class_ = "date")
# # day_temperature = soup.find_all("span", class_ = "big up-from-zero")[1::2]
# # # print(week_day, day_temperature)
# #
# filtered_week_day =[week_day.get_text().split(",")[0] for week_day in week_days]
# day_temperatures = []
# for temperature in day_temperature:
#     temp_text = temperature.get_text().replace("°C", "")
#     temp_value = int(temp_text[:-1])
#     day_temperatures.append(temp_value)
# print(day_temperatures)
#
# data = {"weekday": filtered_week_day, "temperature": day_temperatures}
# df = pd.DataFrame(data)
# print(df)
#
# max_temperature = df["temperature"].max()
# min_temperature = df["temperature"].min()
# import matplotlib.pyplot as plt # yra virsuja
# plt.figure(figsize=(12, 5))
# plt.bar("auksciausia temperatura", max_temperature, color = "green")
# plt.bar("maziausia temperatura", min_temperature, color = "red")
# plt.ylabel("temperatura °C")
# plt.title("auksciausi ir zemiausia temperatura Vilniuje")
# plt.show()

# proc = [90, 10, 45, 60, 70]
# pavadinimas = ["matematika", "istorija", "fizika", "anglu", "biologija"]
# spalvos = ["gold", "lightcoral", "lightskyblue", "lightgreen", "pink"]
# ex = (0.1, 0, 0, 0, 0)
#
# plt.pie(proc, explode=ex, labels=pavadinimas, colors=spalvos, autopct="%1.1f%%", startangle=140)
# plt.title("pavadinimu diegrama")
# plt.axis("equal")
# plt.show()

# 2023.09.20

# x = [5, 8, 6, 4, 5]
# y = [4, 3, 2, 9, 7]
# plt.plot(x, y, label = "linija", color= "blue", linestyle = "--", marker = "o")
# plt.legend()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Grafine vizualizacija")
# plt.show()

# x = [5, 8, 6, 4, 5]
# y = [4, 3, 2, 9, 7]
# z = [5, 4, 3, 10, 8]
# plt.plot(x, y, label = "linija", color= "blue", linestyle = "--", marker = "o")
# plt.plot(y, z, label = "linija2", color= "red", linestyle = "--", marker = "o")
# plt.legend()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Grafine vizualizacija")
# plt.show()

# x = [5, 8, 6, 4, 5]
# y = [4, 3, 2, 9, 7]
# z = [5, 4, 3, 10, 8]
# plt.scatter(x, y, label = "taskai", color = "red", marker = "s")
# plt.legend()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Grafine vizualizacija")
# plt.show()

# x = [5, 8, 6, 4, 5]
# y = [4, 3, 2, 9, 7]
# z = [5, 4, 3, 10, 8]
# plt.scatter(x, y, label = "taskai", color = "red", marker = "s")
# plt.scatter(z, y, label = "taskai", color = "green", marker = "s")
# plt.legend()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Grafine vizualizacija")
# plt.show()

# x = [1, 2, 2, 1, 5, 3, 3, 5]
#
#
# plt.hist(x, bins = 5, color = "purple", alpha = 0.7, edgecolor = "black")
# plt.legend()
# plt.xlabel("x")
# plt.title("Grafine vizualizacija")
# plt.show()

# y = [4, 3, 2, 9, 7]
# z = [4, 6, 2, 5, 7]
# plt.step(y, z, label = "pakopos", color = "red", where = "mid")
# plt.fill_between(y, z, color = "grey", alpha = 0.5)
# plt.text(4,6, "svarbus taskas", fontsize = 12, color = "blue")
# plt.legend()
# plt.xlabel("z")
# plt.ylabel("y")
# plt.title("Grafine vizualizacija")
# plt.show()

# y = [4, 3, 2, 9, 7]
# z = [4, 6, 2, 5, 7]
# plt.step(y, z, label = "pakopos", color = "red", where = "mid")
# plt.fill_between(y, z, color = "grey", alpha = 0.5)
# plt.text(4,6, "svarbus taskas", fontsize = 12, color = "blue")
# plt.axhline(y = 3, color = "green", linestyle = "--", label = "horizontali")
# plt.axvline(x = 5, color = "purple", linestyle = "--", label = "vertikali")
# plt.legend()
# plt.xlabel("z")
# plt.ylabel("y")
# plt.title("Grafine vizualizacija")
# plt.show()

# x = [1, 2, 3, 4, 5]
# y = [10, 15, 7, 12, 9]
# z = [4, 6, 2, 5, 7]
# plt.subplot(2, 1, 1)
# plt.plot(x, y, label = "linija1")
# plt.title("Grafine vizualizacija")
# plt.legend()
# plt.subplot(2, 1, 2)
# plt.plot(x, [i**2 for i in y], label = "linija2", color = "black")
#
# plt.legend()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()
#
# x = [1, 2, 3, 4, 5]
# y = [10, 15, 7, 12, 9]
# z = [4, 6, 2, 5, 7]
# plt.subplot(2, 1, 1)
# plt.plot(x, y, label = "linija1")
# plt.title("Grafine vizualizacija")
# plt.legend()
# plt.subplot(2, 1, 2)
# plt.plot(x, [i**2 for i in y], label = "linija2", color = "black")
#
# plt.legend()
# plt.xlabel("x")
# plt.ylabel("y")
# plt.savefig("grafikas.png")
# plt.show()

# 2023.09.22 - numpy (negalima ivedineti vardu, tiks skaiciai)
# masyvas = np.array([1, 2, 3, 4, 5])
# suma = np.sum(masyvas)  ## suma
# vidurkis = np.mean(masyvas)  ## mean yra vidurkis
# # print(f"Suma: {suma}\nVidurkis: {vidurkis}")
#
# mediana = np.median(masyvas)
# nuokrypis = np.std(masyvas)
# # print(f"Mediana: {mediana}\nNuokrypis: {nuokrypis}")
#
# masyvas2 = np.array([6, 2, 7, 4, 8])
# moda = np.mod(masyvas, masyvas2)
# # print(moda)
#
# suma1 = masyvas + masyvas2
# min = np.min(masyvas)
# max = np.max(masyvas2)
# # print(suma1, min, max)
#
# matrica = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # print(matrica)
#
# suma2 = np.sum(matrica)
# # print(suma2)
#
# matrica2 = np.random.randint(1, 11, (4, 4))
# print(matrica2)
#
# vidurkis2 = np.mean(matrica2)
# # print(vidurkis2)
#
# vidurkis3 = np.mean(matrica2, axis = 0)                 # stulpelis
# vidurkis4 = np.mean(matrica2, axis= 1)                  #eilute
# print(vidurkis3, vidurkis4)

# Darbas:
# studentu_pazymiai = np.array([[7, 8, 9], [6, 4, 10], [10, 9, 10], [8, 8, 7]])
# vidurkis = np.mean(studentu_pazymiai, axis = 1)
# print(vidurkis)
# mediana = np.median(studentu_pazymiai, axis = 1)
# # print(mediana)
#
# for i in range(len(vidurkis)):
#     print(f"Studentas {i + 1}: vidurkis {vidurkis[i]}, mediana {mediana[i]}")

# masyvas33 = np.random.randint(1, 51,(1, 1))
# maksis = np.argmax(masyvas33)
# minas = np.argmin(masyvas33)
# print(masyvas33, "\n", maksis, "\n", minas)

masyvas = np.array([1, 2, 3, 4, 5])
daugiau_uz_tris = masyvas[masyvas > 3]
print(daugiau_uz_tris)