# # mano komentaras
# # '''
# # multi-line comment
# # '''
# # vardas = "Kestas"
# # # print(vardas)


# # skaicius = 25
# #
# # skaicius1 = "32"
# # print ("mano sugalvotas skaicius " + str(skaicius))
# #
# # print(type(skaicius1))
# # true_or_false = False
# # active_user = False
# fruits = ['apple', 'orange', 'kiwi', 'watermeleon']
# Lietuvos_pilietis = {
#     'id' :1,
#     'Vardas': 'Antanas',
#     'Amzius': 34,
#     'Miestas': 'Klaipeda'
# }
# # print(lietuvos_pilietis)
# print("Pries:")
# print("Vardas: ", Lietuvos_pilietis["Vardas"])
# print("Po:")
# Lietuvos_pilietis['Vardas'] = "Giedrius"
# print("Vardas: ", Lietuvos_pilietis["Vardas"])
# print (fruits[1])
# print(type(fruits))

# temperaturos = [20, 25, 22, 18, 12]
#
# suma = sum(temperaturos)
# print(suma)


# kiekis = len(temperaturos)
# print(kiekis)
#
# vidutine_temperatura = suma / kiekis
# print("vidutine temperatura yra: ",vidutine_temperatura)

# sudetis = 5 + 5
# atimtis = 6 - 2
# dalyba_be_liekanos = 15 // 3
# print(dalyba_be_liekanos)
# daugyba = 5*9
# print(daugyba)
# laipsnis = 2 ** 3
# print(laipsnis)
# liekana_po_dalybos = 10 % 3
# print(dalyba_su_liekana)
# dalyba = 1/3
# print(dalyba)

# skaicius = 42
# if skaicius == 42:
#     print("Lygus")
# else:
#     print("Nelygus")

# skaicius = 42
# if skaicius != 42:
#     print("Lygus")
# else:
#     print("Nelygus")

# skaicius = 42
# if skaicius < 42:
#     print("daugiau uz 42")
# elif skaicius == 42:
#     print("Lygus")
# else:
#     print("Nelygus")

# skaicius = 42
# if skaicius:
#     print("daugiau uz 42")
# elif skaicius == 42:
#     print("Lygus")
# else:
#     print("Nelygus")

# sarasas = [1, 2, 3, 4, 5]
# for elementas in sarasas:
#     print("Elementas:", elementas)
#
# for i in range(5):
#     print(i)

# for i in range(2, 7):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# skaiciai = [24, 11, 72, 34, 7, 84]
# didziausias_skaicius = skaiciai[0]
# for skaicius in skaiciai:
#     if skaicius > didziausias_skaicius:
#         didziausias_skaicius = skaicius
# print("Didziausias_skaicius yra:", didziausias_skaicius)

# skaicius = input("Koks mano vardas:")
# print (skaicius)

# skaicius = int(input("Parasykite skaiciu:"))
# print (skaicius)

# skaicius = float(input("Parasykite skaiciu:"))
# print (skaicius)

# skaicius = int(input("Iveskite skaiciu:"))
# suma = 0
# for i in range(1, skaicius + 1):
#     suma += i
# print ("skaiciu suma nuo 1 iki", skaicius, "yra", suma)

# 1.is saraso isfiltruoti lyginius skaicius
# sarasas = [2, 5, 11, 25, 9, 8]
# lyginiai_skaiciai = []
# for skaicius in sarasas:
#     if skaicius %2 == 0:
#         lyginiai_skaiciai.append(skaicius)
# print("lyginiai_skaiciai", lyginiai_skaiciai)

# 2.isspauzdinti piramide su zvaigzdutemis
# eiluciu_skaicius = int(input("Iveskite sveika skaiciu"))
# for eilute in range(1, eiluciu_skaicius +1):
#     tarpas = eiluciu_skaicius - eilute
#     zvaigdze = 2 * eilute -1
#     print(" " * tarpas + "*" * zvaigdze)

# 3.surasti pirminius skaicius tarp 10 ir 50.
# pradzia = 10
# pabaiga = 50
# print (f"pirminiai skaiciai tarp {pradzia} ir {pabaiga} yra: " )
# for skaicius in range(pradzia, pabaiga +1):
#     if skaicius > 1:
#         for daliklis in range(2,skaicius):
#             if (skaicius % daliklis) == 0:
#                 break
#         else:
#             print(skaicius)

# 4. Patikrinti zodzius is saraso, rasti ir atspauzdinti zodzius kurie prasideda raide a.
# zodziai = ["Stalas", "Veidrodis", "A2", "Lova", "Sviestuvas", "NEO", "Aplankalas", "Kede"]
# raide = "A"
# for zodis in zodziai:
#     if zodis[0].upper()== raide.upper():
#         print (zodis)

# 5. Reikia sudaryti ir isvesti daugybos lentele.
# print("Daugybos lentele nuo 1 iki 10")
# for i in range(1,11):
#     for j in range(1,11):
#         rezultatas = i*j
#         print(f"{i} x {j} = {rezultatas}")
#     print()

# 6. Parasyti ir patikrinti ar ivestas skaicius yra teigiamas, neigiamas ar = 0.
# Skaicius = int(input("Iveskite skaiciu_>"))
# if Skaicius > 0:
#     print ("Ivestas skaicius yra teigiamas")
# elif Skaicius < 0:
#     print ("Ivestas skaicius yra neigiamas")
# else: Skaicius = 0
# print ("Ivestas skaicius yra = 0")

# 7. Maza programele kur isveda fizz (dalijasi is 3), buzz (kurie dalijasi is 5)
# fizzbuzz (kurie dalijasi is 3 ir 5) intervalas nuo 1 iki 100.
# for skaicius in range(1, 101):
#     if skaicius % 3 == 0 and skaicius % 5 == 0:
#         print ("FizzBuzz")
#     elif skaicius % 3 == 0:
#         print ("Fizz")
#     elif skaicius % 5 == 0:
#         print ("Buzz")
#     else:
#         print(skaicius)

# 8. Sukurkite skaiciu atspejimo zaidima.
# pasleptas_skaicius = random.randint(1,100)
# bandymai = 0
# maksimalus_bandymu_skaicius = 10
# while bandymai < maksimalus_bandymu_skaicius:
#     spejimas = int(input("Atspekite paslepta skaiciu nuo 1 iki 100: "))
#     bandymai += 1
#     if spejimas == pasleptas_skaicius:
#         print(f"Sveikiname! Atspejote skaiciu per {bandymai} bandymus")
#         break
#     elif spejimas < pasleptas_skaicius:
#         print ("Bandykite didesni skaiciu")
#     else:
#         print("Bandykite mazesni skaiciu")
# if bandymai >= maksimalus_bandymu_skaicius:
#     print(f"Jus pasiekete maksimalu bandymu skaiciu. Pasleptas skaicius buvo {pasleptas_skaicius}")

# 9. sukurti zodziu sarasas kur saugomi zodziai ir ju ilgiai ir isvesti kurie ilgesni nei 6 simboliai
# zodziai = ["Stalas", "Veidrodis", "As", "Lova", "Sviestuvas", "NEO", "Aplankalas", "Kede", "Laikrodis"]
# zodynas = {}
# for zodis in zodziai:
#     zodynas[zodis] = len(zodis)
# for zodis, ilgis in zodynas.items():
#     if ilgis > 6:
#         print(f"{zodis}: {ilgis} simboliai")


# +1.Sukurkite žodyną ir trumpą tekstą. Atspasudinkite žodžius, kurie pasikartojo daugiau nei 3 kartus.
# tekstas = "labas, labas. labas. labas, as esu Kestas"
# zodynas = {}
# zodziai = tekstas.split()
# for zodis in zodziai:
#     zodis = zodis.strip(",.")
#     zodynas[zodis] = zodynas.get(zodis, 0 ) +1
# for zodis, kartojasi in zodynas.items():
#     if kartojasi > 3:
#         print(f"zodis {zodis} kartojasi daugiau negu 3 kartus")

# zodyne turi buti zodziai kurie pasikartoja daugiau negu 3 kartus. 2 FOR ir 1 IF
# strip naudojamas skirybos zenklams skaiciavimo/ieskojimo metu, kad ju nepriskaiciuotu.

# 2.Sukurti sąrašą žodžių ir išvesti unikalius žodžius bei jų pasikartojimo dažnumą;


# 3.Sukurkite žodyną su studentų duomenimis ir atspausdinkite studentus, kurių vidurkis yra aukščiau 8.0;
# Studentu_duomenys = {
# 'id' = 1,
# 'Vardas' = 'Kestas',
# 'Amzius' = 28,
# 'Pazymiu vidurkis' = 7
# }
# print(Studentu_duomenys)

# 4.Sukurti žodyną su knygų informacija ir surikiuoti knygas pagal metus ir pavadinimus.







# ilgis = 7
# simboliai = string.ascii_letters + string.digits + string.punctuation
# random_string = ''.join(random.choice(simboliai) for _ in range(ilgis))
# print("random_string", random_string)
# _ naudojama tarp for ir in kai nera kintamojo ir nenorim jo nurodyti.




# 2023-09-06
# +1.Parašykite programą, kuri suskaičiuoja visų sveikujų skaičių nuo 1 iki n ėjimo sumą,
# kur n yra vartotojo įvestas skaičius. Panaudokite "for" ciklą ir "if" sąlygos sakinį,
# kad tikrintumėte, ar įvestas skaičius yra sveikasis;
# n = int(input("Iveskite skaiciu: "))
# if n <= 0:
#     print("Ivestas skaicius turi buti sveikasis, bandykite dar karta")
# else:
#     suma = 0
#     for skaicius in range(1, n +1):
#         suma += skaicius
#     print(f"suma nuo 1 iki {n} yra {suma}")

# +2. Sukurkite programą, kurioje vartotojas gali įvesti mokinio pažymį (nuo 1 iki 10).
# Programa turi grąžinti mokinio vertinimą
# (pvz., "Neužtektinai", "Silpnai", "Vidutiniškai", "Gerai", "Puikiai"). Naudokite "if" sąlygos sakinį.

# Pazymys = int(input("Iveskite pažymį:"))
# if Pazymys < 1:
#     print("Ivestas pazymys yra netinkamas, iveskite pazymi nuo 1 iki 10 (imtinai)")
# if Pazymys > 10:
#     print("Ivestas pazymys yra netinkamas, iveskite pazymi nuo 1 iki 10 (imtinai)")
# elif Pazymys <= 1 and Pazymys <= 3:
#     print("Neuztektinai")
# elif Pazymys <= 4:
#     print("Silpnai")
# elif Pazymys <= 5 and Pazymys <= 6:
#     print("Vidutiniskai")
# elif Pazymys <= 7 and Pazymys <= 8 and Pazymys <= 9:
#     print("Gerai")
# elif Pazymys <= 10:
#     print("Puikiai")

 # arba

# Pazymys = int(input("Iveskite pažymį:"))
# if Pazymys < 1 or Pazymys > 10:
#     vertinimas = "Netinkamas pazymys, iveskite pazymi nuo 1 iki 10"
# elif Pazymys >= 9:
#     vertinimas = "Puikiai"
# else:
#     vertinimas = "Nezutektinai"
# print(f"Mokinio vertinimas: {vertinimas}")


# +3. Sukurkite programą, kuri leidžia vartotojui įvesti metus. Programa turi patikrinti, ar įvesti
# metai yra keliamieji (dalijasi iš 4) ir atspausdinti atitinkamą pranešimą

# Metai = int(input("Iveskite metus:"))
# if Metai % 4 == 0:
#     print(f"{Metai} yra keliamieji")
# else:
#     print(f"{Metai} yra nekeliamieji")



# +4. Turite žodyną, kuriame yra vardai ir amžius. Parašykite programą,kuri peržiūri žodyną ir išrenka tik
# tas poras, kuriose amžius yra didesnis arba lygus 18. Rezultatus patalpinkite naujame žodyne;
# Asmenys ={
#      'Jovita': 21,
#      'Aurelijus': 71,
#      'Aurimas': 8,
#      'Dovile': 18,
#      'Ausra': 41,
#     }
# zodynas = {}
# for vardas, metai in Asmenys.items():
#     if metai >= 18:
#         zodynas[vardas] = metai
# print(zodynas)



# +5. Leiskite vartotojui įvesti kelias prekes ir jų kainas. Sukurkite sąrašą, kuriame prekės yra žodynai,
# kuriuose yra prekės pavadinimas ir kaina. Taip pat paskaičiuokite bendrą visų prekių kainą;
# turi buti 1 while 1 if ir 2 for.
# prekiu_krepselis = []
# while True:
#     preke = input("Nurodykite preke arba irasykite zodi baigti: ")
#     if not preke:
#         break
#     kaina = float(input("Iveskite prekes kaina: "))
#     prekes_informacija = {"pavadinimas": preke, "kaina": kaina}
#     prekiu_krepselis.append(prekes_informacija)
# Krepselio_suma = sum(prekes_informacija ["kaina"] for prekes_informacija in prekiu_krepselis)
# print("prekiu sarasas: ")
# for prekes_informacija in prekiu_krepselis:
#     print(f"Pavadinimas: {prekes_informacija['pavadinimas']}, Kaina: {prekes_informacija['kaina']}")
# print (f"Benra kaina: {Krepselio_suma}")

# 6. Turite sąrašą žmonių vardų. Sukurkite programą, kuri leidžia vartotojui įvesti vardą ir patikrina,
# ar jis yra sąraše. Jei vardas yra sąraše, programa turi išvesti pranešimą "Vardas yra sąraše,"
# kitu atveju - "Vardo nėra sąraše."
# sarasas = ["Jovita", "Aurelijus", "Aurimas", "Dovile", "Ausra"]
# vardas = int(input("Irasykite varda: "))
# if vardas in sarasas:
#     print ("Vardas yra sarase")
# else:
#     print("Vardo sarase nera")




# x(kintamasis) = 5 - Pradine reiksme
# x = 8 - galutine reiksme
# lieka x = 8


# a = 5
# if a > 5:
#     print()
# elif a == 5:
#     print()
# else:
#     print()

# 1. Sukurkite sąrašą temperatūros su temperatūromis. Patikrinkite kiekvieną temperatūrą sąraše ir išveskite "šilta"
# (jei temperatūra virš 20) arba "šalta" (jei temperatūra 20 ar mažiau).
# Temperaturos = ["20, 21, 22, 30, 18, 19, 5, 0, -1"]
# if Temperatura in Temperaturos > 20:
#         print(f" Temperatura {Temperaturos} yra silta")
# else:
#         print(f"Temperatura{Temperaturos} yra salta")






# 2. Turite žodyną su studentų vardais ir jų pažymiais. Parašykite "for" ciklą,
# kuris išveda kiekvieno studento vardą ir jo pažymį.
# Studentai = {
#      'Jovita': 7,
#      'Aurelijus': 3,
#      'Aurimas': 8,
#      'Dovile': 8,
#      'Ausra': 10
#     }
# for i in Studentai:
#         break
# print(Studentai)

# 3. Sukurkite tuščią sąrašą sarasas ir leiskite vartotojui įvesti skaičius. Naudojant "while" ciklą, pridėkite
# kiekvieną įvestą skaičių prie sąrašo. Ciklą nutraukite, kai vartotojas įveda 0.
sarasas = []
while True:
        skaicius = int(input("Iveskite skaiciu arba nutraukite irase 0"))
        if skaicius = 0:
                break




# prekiu_krepselis = []
# while True:
#     preke = input("Nurodykite preke arba irasykite zodi baigti: ")
#     if not preke:
#         break
#     kaina = float(input("Iveskite prekes kaina: "))
#     prekes_informacija = {"pavadinimas": preke, "kaina": kaina}
#     prekiu_krepselis.append(prekes_informacija)
# Krepselio_suma = sum(prekes_informacija ["kaina"] for prekes_informacija in prekiu_krepselis)
# print("prekiu sarasas: ")
# for prekes_informacija in prekiu_krepselis:
#     print(f"Pavadinimas: {prekes_informacija['pavadinimas']}, Kaina: {prekes_informacija['kaina']}")
# print (f"Benra kaina: {Krepselio_suma}")





# 4. Turite žodyną, kuriame saugomi gėrimų pavadinimai ir jų kainos. Vartotojas įveda gėrimo pavadinimą,
# o jūs patikrinkite, ar tokio pavadinimo gėrimas yra žodyne. Jei taip, išveskite jo kainą; jei ne,
# išveskite pranešimą "Gėrimas nerastas".



# 5. Patikrinkite, ar skaičiai sąraše yra lyginiai arba nelyginiai. Sukurkite du tuščius sąrašus:
# vienas lyginiams ir kitą nelyginiams skaičiams, išrūšiuokite lyginius ir nelyginius skaičius iš skaičiai sąrašo.


# vardai = ["Jonas", "Petras", "Marius", "Laura"]
#
# pirmas_vardas = vardai.pop(2) (spauzdina varda po tam tikru skaiciumi. tuscias grazina paskutini varda)
# print(pirmas_vardas)

# vardai.insert(1, "Giedrius") (nurodai i pozicija kur ideti ir pridedi i ta vieta komanda index)
# print(vardai)

# vardai.append("Giedrius") (pridedi i gala)
# print(vardai)

# vardai.sort(reverse=True(apsuka nuo z iki a)) rusiuoja pagal abecele A-Z
# print(vardai)

# vardai.remove("Jonas")
# print(vardai)

# vaisiai = ("Obuolys", "Kriause", "Bananas", "Braske")
# vaisiai1 = ["Obuolys", "Kriause", "Bananas", "Braske"]
# vaisiai = {
#     "Obuolys"
#     "Kriause"
#     "Bananas"
#     "Braske "
# }
# vaisiai2 = vaisiai[0]
# print(vaisiai2)

# skaiciai =(3.14, 2.71)
# x, y = skaiciai
# print(x)
# print(y)

# vaisiai1 = ["Obuolys", "Kriause", "Bananas", "Braske"]
# for indeiksas, vaisius in enumerate(vaisiai1, start=1):
#     print(f"{indeiksas}. {vaisius}")
    # enumerate = (naudojamas sarasuose.eilutese) suteikti galimybe, kad gauti tiek elementu
# kiek turime tame objekte. suskaiciuoja ir sunumeruoja viska.

# # funkcija open
# with open("failo_pavadinimas.txt", 'w', encoding='utf-8') as file:
#     content = file.write("Kuriame nauja faila")
#     print(content)

# with open("failo_pavadinimas.txt", 'w', encoding='utf-8') as file:
#     content = file.write("Kuriame nauja faila")

# with open("failo_pavadinimas.txt", 'a', encoding='utf-8') as file:
#     content = file.write("\nPapildomas tekstas")

    # r = read
    # w =
    # a = apend (papildo)
    # b = forbaner

# with open("failo_pavadinimas.txt", 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# with open("failo_pavadinimas.txt", 'r', encoding='utf-8') as file:
#     for eilute in file:
#         print(eilute.strip())
#
# with open("vaisiai.txt", 'w', encoding='utf-8') as file:
#         file.write('\nObuolys, \nKriause, \nBananas, \nBraske.')
#
# vaisiai = []
# with open("vaisiai.txt", 'r', encoding='utf-8') as file:
#         vaisiai = file.readline()
#         print(vaisiai)