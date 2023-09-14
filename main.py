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
# sarasas = []
# while True:
#         skaicius = int(input("Iveskite skaiciu arba nutraukite irase 0"))
#         if skaicius = 0:
#                 break




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


# def pasisveikinimas(vardas):
#         sveikinimas = f"Sveiki, {vardas}"
#         # return sveikinimas grazina funkcija, kuria atlieka
#
# vardas = input("Iveskite savo varda: ")
# sveikinimas = pasisveikinimas(vardas)
# print(sveikinimas)

# def ar_lyginis(skaicius):
#         if skaicius % 2 == 0:
#                 return True
#         else:
#                 return False
#
# skaicius = 7
# if ar_lyginis(skaicius):
#         print(f"{skaicius} yra lyginis")
# else:
#         print(f"{skaicius} yra nelyginis")

# def ar_lyginis(skaicius):
#         if skaicius % 2 == 0:
#                 return True
#         else:
#                 return False
#
# skaicius = int(input("Iveskite skaiciu: "))
# if ar_lyginis(skaicius):
#         print(f"{skaicius} yra lyginis")
# else:
#         print(f"{skaicius} yra nelyginis")

# def suma(a, b):
#         rezultatas = a + b
#         return rezultatas
#
# x = 5
# y = 3
# sumos_rezultatas = suma (x, y)
# print(f"{x} + {y} = {sumos_rezultatas}")

# def suma():
#         rezultatas = 5 + 3
#         return rezultatas
#
# x = 5
# y = 3
# sumos_rezultatas = suma ()
# print(f"{x} + {y} = {sumos_rezultatas}")

# def pasisveikinimas():
#         print("Labas")
#
#
# if __name__ == "__main__":
#       pasisveikinimas()

# def vidurkis(skaiciai): #vidurkis yra funkcijos pavadinimas. skaiciai - argumentas arba parametras.
#         suma = sum(skaiciai)
#         avg = suma / len(skaiciai)
#         return avg
#
# sarasas = [10, 15, 20, 25, 30, 1]
# rezultatas = vidurkis(sarasas)
# print(f"saraso vidurkis yra: {rezultatas}")


# 1. Patikrinti ar skaicius yra teigiamas ar neigiamas.
# def ar_teigiamas(skaicius):
#         if skaicius > 0:
#                 return True
#         else:
#                 return False
#
# skaicius = -1
# if ar_teigiamas(skaicius):
#         print(f"{skaicius} yra teikiagas")
# else:
#         print(f"{skaicius} yra neigiamas")

# 2, funkcija, kuri surastu didziausia skaiciu
# def didziausias_skaicius(skaicius):
#         didziausias = skaicius[0]
#         for i in skaicius:
#                 if i > didziausias:
#                         didziausias = i
#         return didziausias
#
# sarasas = [10, 658, 12, -2]
# didziausias = didziausias_skaicius(sarasas)
# print(f"didziausias yra: {didziausias_skaicius}")

# 3. funkcija kuri sujungia 2 sarasus
# def sujungti_sarasai (sarasas1, sarasas2):
#         sujungtas_sarasas = sarasas1 + sarasas2
#         return sujungtas_sarasas
#
# sarasas1 = [1, 3, 5, 7, 9]
# sarasas2 = ["Kestas, Aurimas, ir kiti draugai"]
# rezultatas = sujungti_sarasai(sarasas1, sarasas2)
# print(rezultatas)

# Namu darbai:
# 1. Parašykite funkciją, kuri priimtų sąrašą studento pažymių ir grąžintų vidurkį;



# 2. Sukurkite funkciją pirminiai_skaiciai(n), kuri priima sveikąjį skaičių n ir grąžina
# visus pirminius skaičius nuo 2 iki n;



# 3. Sukurkite funkciją zodziu_kiekis(tekstas), kuri priima tekstą ir grąžina žodžių skaičių
# tekste. Žodžius galite laikyti atskirtais tarpais;



# 4. Sukurkite funkciją didziausias_elementas(sarasas), kuri priima sąrašą skaičių ir grąžina didžiausią elementą;



# 5. Sukurkite funkciją kvadrato_plotas(ilgis), kuri priima kvadrato kraštinės ilgį ir grąžina kvadrato plotą.



# 6. Sukurkite funkciją sarasas_suma(sarasas), kuri priima sąrašą skaičių ir suskaičiuoja jų sumą.
# Leiskite vartotojui įvesti sąrašą skaičių ir išvesti jų sumą;



# 7. Sukurkite funkciją, kuri priimtų skaičių sąrašą ir grąžintų visų sąrašo skaičių sandaugą.
# def mano_sarasas(sarasas):
#    sandauga = 1
#    for skaicius in sarasas:
#         sandauga = sandauga * skaicius
#    return sandauga
# sk_sarasas = [2, 4, 6, 8, 10]
# print('Saraso skaiciu sandauga lygi:',mano_sarasas (sk_sarasas))


# Klases darbas 2023-09-11
# class - apibreziamas visas objektas
# self - specialus kintamasis visada naudojamas su class.


#sukuriama klase:
# class Zmogus:
#     #Sukuriamas konstruktorius:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amziu = amzius
#
#         #Kuriami metodai:
#     def pasveikinimas (self):
#         return f"Sveiki, as esu {self.vardas} ir man yra {self.amziu} metu."
#
# # kuriamas objektas
# zmogus1 = Zmogus("Migle", 30)
# zmogus2 = Zmogus("Jonas", 20)
# print(zmogus1.pasveikinimas())
# print(zmogus2.pasveikinimas())


# class Automobilis:
#
#     def __init__(self, marke, modelis):
#         self.marke = marke
#         self.modelis = modelis
#         self.greitis = 0
#
#     def akseleratorius (self):
#         self. greitis += 10
#
#     def stabdis(self):
#         self.greitis -= 5
#
#     def info(self):
#         return f"{self.marke} {self.modelis}, greitis: {self.greitis} km/h"
#
# Auto1 = Automobilis("Kia", "Ceed")
# Auto1.akseleratorius()
# Auto1.stabdis()
# print(Auto1.info())



# sukurti knygos klase, kuri turi autoriu, pavadinima ir metus.
# class Knyga:
#
#     def __init__(self, pavadinimas, autorius, metai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.metai = metai
#
#     def info(self):
#         return f"Knygos pavadinimas: {self.pavadinimas}, Autorius: {self.autorius}, Leidimo metai: {self.metai}"
#
# knyga1 = Knyga("Visi norejo testo", "Nebus", "2022")
# print(knyga1.info())
#
# pirkiniu krepselis, kuris tures tam tikras prekes
# class Preke:
#
#     def __init__(self, pavadinimas, kaina):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#
#     def info(self):
#         return f"preke: {self.pavadinimas}, prekes kaina: {self.kaina}$"
#
# class Krepselis:
#     def __init__(self):
#         self.prekes = []
#
#     def ideti_preke(self, preke):
#         self.prekes.append(preke)
#
#     def krepselio_sudetis(self):
#         if not self.prekes:
#             print("Tokios prekes nera")
#         else:
#             print("Krepselio turinys: ")
#
#             for preke in self.prekes:
#                 print (preke.info())
#
#     def visa_suma(self):
#         suma = sum(preke.kaina for preke in self.prekes)
#         return suma
#
# krepsys = Krepselis()
# preke1 = Preke ("Duona", 1.25)
# preke2 = Preke ("Svogunai", 0.95)
# preke3 = Preke ("Cigaretes", 2.99)
# preke4 = Preke ("Pienas", 1.09)
# preke5 = Preke ("Kava", 5.99)
# preke6 = Preke ("Kefyras", 0.87)
#
# krepsys.ideti_preke(preke1)
# krepsys.ideti_preke(preke2)
# krepsys.ideti_preke(preke3)
# krepsys.ideti_preke(preke3)
# krepsys.ideti_preke(preke3)
# krepsys.ideti_preke(preke4)
# krepsys.ideti_preke(preke5)
#
# krepsys.krepselio_sudetis()
# print(f"Bendra suma: {krepsys.visa_suma()}$")



# 1. Sukurkite klasę "Saskaita", kuri turėtų šias savybes ir metodus:
#
#     * saskaitos_nr: sąskaitos numeris.
#     * balansas: sąskaitos balansas (numatytasis pradžioje yra 0).
#     * inesti(suma): metodas, kuris prideda nurodytą sumą prie sąskaitos balanso.
#     * isimti(suma): metodas, kuris sumažina sąskaitos balansą nurodyta suma, jei yra pakankamai lėšų,
# arba išveda pranešimą apie nepakankamą balansą.
#     * +informacija(): metodas, kuris grąžina informaciją apie sąskaitą (sąskaitos numeris ir balansas).
#
# Sukurkite bent du objektus pagal šią klasę ir atlikite operacijas, tokiu kaip lėšų įnešimas ir išėmimas,
# bei gaukite sąskaitos informaciją.

# class Saskaita:
#     def __init__(self, saskaitos_nr, balansas = 0):
#         self.saskaitos_nr = saskaitos_nr
#         self.balansas = balansas
#         print("Sveiki. Ka panoresite atlikti?")
#
#     def inesta_suma(self, suma):
#         self.balansas += suma
#     def isimta_suma(self, suma):
#         if self.balansas >= suma:
#             self.balansas -= suma
#             print(f"Jus issigrininote {suma}")
#         else:
#             print("Jusu saskaitos likutis nepakankamas: ")
#
#     def informacija(self):
#         return f"Saskaitos numeris: {self.saskaitos_nr}, saskaitos balansas: {self.balansas}"
#
#
# saskaita1 = Saskaita("LT6767", 1500)
# saskaita1.isimta_suma(100)
# print(saskaita1.informacija())
#
#




# 2. Sukurkite klasę "Studentas", kuri turėtų šias savybes:
#     * vardas: studento vardas.
#     * pazymiai: sąrašas su studento pažymiais.
# Sukurkite klasę "Mokytojas", kuri turėtų šias savybes:
#     * vardas: mokytojo vardas.
#     * Mokytojo dėstoma tema: mokytojo dėstomas dalykas.
# Papildykite "Studentas" klasę metodu vidurkis(), kuris apskaičiuoja studento pažymių vidurkį.
# Papildykite "Mokytojas" klasę metodu ivertinimas(studentas, pazymys), kuris prideda studentui pažymį.
# Sukurkite objektus pagal "Studentas" ir "Mokytojas" klases, pridėkite pažymius ir vykdykite vidurkio apskaičiavimus
# bei pažymių pridėjimus.

# class Studentas:
#     def __init__(self, vardas):
#         self.vardas = vardas
#         self.pazymiai = []
#
#     def prideti_pazymi(self, pazymys):
#         self.pazymiai.append(pazymys)
#
#     def vidurkis(self):
#         if not self.pazymiai:
#             return 0
#         return sum(self.pazymiai) / len(self.pazymiai)
#
# class Mokytojas:
#     def __init__(self, vardas, destomas_dalykas):
#         self.vardas = vardas
#         self.destomas_dalykas = destomas_dalykas
#
#     def ivertinimas (self, studento_vardas, studento_pazymys):
#         studento_vardas.prideti_pazymi(studento_pazymys)
#
# studentas1 = Studentas("Petras")
# mokytojas1 = Mokytojas("Martynas", "Informatika")
#
# mokytojas1.ivertinimas(studentas1, 8)
#
# print(f"{studentas1.vardas},  vidurkis: {studentas1.vidurkis()}")




# 3.






# 3. Kryziukai nuliukai zaidimas:
# stack over flow.
# gavot klaida. nusikopijuojat ta klaida, copy paste i google klaida. didelis procentas, kad bus sprendimas.







# Klases darbas 2023-09-12
# 1. Sukurkite klasę "Kava", kuri turėtų savybes "pavadinimas", "kaina", ir "talpa". Parašykite metodą, kuris
# patikrintų, ar ši kava yra tinkama tam tikram puodeliui, pagal jo talpą.

# class Kava:
#
#     def __init__(self, pavadinimas, kaina, talpa):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.talpa = talpa
#
#     def ar_tinkama_puodeliui(self, puodelio_talpa):
#         if self.talpa <= puodelio_talpa:
#             return f"{self.pavadinimas} kava tinka puodeliui su talpa {puodelio_talpa} ml"
#         else:
#             return f"{self.pavadinimas} kava netinka puodeliui su talpa {puodelio_talpa} ml"
#
# kava1 = Kava("Latte", 1.99, 250)
# puodelio_talpa = 300
# print(kava1.ar_tinkama_puodeliui(puodelio_talpa))



# 2. Knygynas kuris turi: knygos savybe, sarasa,. prideti - ieskoti ir atspausdinti visu knygu sarasa
# class Knygynas:
#     def __init__(self):
#         self.knygos = []
#     def prideti_knyga(self, knyga):
#         self.knygos.append(knyga)
#     def knygos_paieska (self, pavadinimas):
#         for knyga in self.knygos:
#             if knyga ["pavadinimas"] == pavadinimas:
#                 return knyga
#             return None
#     def knygu_sarasas(self):
#         if not self.knygos:
#             print ("Knygynas tuscias")
#         else:
#             print("Knygyno knygu sarasas: ")
#             for knyga in self.knygos:
#                 print(f"Pavadinimas: {knyga['pavadinimas']}, Autorius: {knyga['autorius']}, Metai: {knyga['metai']}")
# knygynas1 = Knygynas()
# knygynas1.prideti_knyga({"pavadinimas": "Ruduo", "autorius": "Zemaitis", "metai": 1981})
# knygynas1.prideti_knyga({"pavadinimas": "Sudie", "autorius": "Impotepas", "metai": 2029})
# ieskoma_knyga = knygynas1.knygos_paieska("Sudie") #kazkodel neranda.....................
# if ieskoma_knyga:
#     print(f"Rasta knyga: {ieskoma_knyga['pavadinimas']}")
# else:
#     print("Knyga buvo nerasta")
# knygynas1.knygu_sarasas()

# 3. Sukurkite klasę "Prekybininkas", kuri turi atributus "vardas" (name) ir "prekės" (items) ( prekių sąrašas).
# Parašykite metodus, kurie leidžia pridėti prekes prie prekių sąrašo, pašalinti prekes ir paskaičiuoti prekių
# bendrą sumą;
# class Prekybininkas:
#     def __init__(self, vardas, prekes, prekiu_sarasas = 0):
#         self.vardas = vardas
#         self.prekes = prekes
#         self.prekiu_sarasas = prekiu_sarasas
#     def prideti_preke(self, preke):
#         self.prekes.append(preke)
#     def prekes_paieska(self, pavadinimas):
#         for preke in self.prekes:
#             if preke ["pavadinimas"] == pavadinimas:
#                 return preke
#             return None
#     def prekiu_sarasas(self):
#         if not self.prekes:
#             print("Prekes nera")
#         else:
#             print ("Prekiu sarasas: ")
#             for preke in self.prekes:
#                 print(f"")

# class Prekybininkas:
#     def __init__(self, vardas):
#         self.vardas = vardas
#         self.prekes = []
#     def prideti_preke(self, preke, kiekis = 1):
#         for _ in range(kiekis):
#             self.prekes.append(preke)
#     def pasalinti_preke(self, preke, kiekis = 1):
#         if preke in self.prekes:
#             for _ in range(kiekis):
#                 self.prekes.remove(preke)
#         else:
#             print ("Nera tokios prekes")
#     def prekiu_suma(self):
#         suma = sum(preke[1] for preke in self.prekes)
#         return suma
#
# pardavejas = Prekybininkas("Martynas")
# preke1 = ("kava", 1.0)
# preke2 = ("cukrus", 2.5)
# preke3 = ("cigaretes", 1.5)
# pardavejas.prideti_preke(preke1, 3)
# pardavejas.prideti_preke(preke2)
# pardavejas.prideti_preke(preke3, 3)
# suma = pardavejas.prekiu_suma()
# print(suma)
#
# pardavejas.pasalinti_preke(preke1, 1)
# pardavejas.pasalinti_preke("preke4")
# suma = pardavejas.prekiu_suma()
# print("Prekiu sarasas: ")
#
# for preke in pardavejas.prekes:
#     print(f"{preke[0]}: {preke[1]}")
# print(f"Bendra visu prekiu suma: {suma}")

# 4. Sukurkite klasę "Darbuotojas" (Employee), kuri turi atributus "vardas" (name), "pareigos" (position), ir "
# atlyginimas" (salary). Parašykite metodus, kurie leidžia keisti darbuotojo pareigas ir atlyginimą;
# class Darbuotojas:
#     def __init__(self, vardas, pareigos, atlyginimas):
#         self.vardas = vardas
#         self.pareigos = pareigos
#         self.atlyginimas = atlyginimas
#     def darbuotojo_pareigos(self, uzimamos_pareigos):
#         if self.pareigos <= uzimamos_pareigos:
#             return f"darbuotojas {self.vardas}, uzima {self.pareigos} pareigas ir gauna {self.atlyginimas}$ atlginima"
#
# darbuotojas1 = Darbuotojas("Kestas", "Testavimo Inzinierius", 2100)
# print(darbuotojas1.darbuotojo_pareigos("Testavimo inzinierius"))

# class Darbuotojas:
#     def __init__(self, vardas, pareigos, atlyginimas):
#         self.vardas = vardas
#         self.pareigos = pareigos
#         self.atlyginimas = atlyginimas
#     def pakeisti_atlyginima(self, naujas_atlyginimas):
#         self.atlyginimas = naujas_atlyginimas
#     def pakeisti_pareigas(self, naujos_pareigos):
#         self.pareigos = naujos_pareigos
#
# darbuotojas1 = Darbuotojas("Kestas", "Inzinierius", 2100)
# darbuotojas1.pakeisti_atlyginima(2200)
# darbuotojas1.pakeisti_pareigas("Inzineriu Vadovas")
#
# print (f"{darbuotojas1.vardas}, pareigos: {darbuotojas1.pareigos}, gaunamas uzmokestis: {darbuotojas1.atlyginimas}")



# 5. Sukurkite klasę "Skaičiuotuvas", kuri turi metodus "sudėti" (add), "atimti" (subtract), "dauginti" (multiply) ir
# "dalinti" (divide). Šie metodai priima du skaičius ir atlieka atitinkamą matematinę operaciją.


# class Skaiciuotuvas:
#     def add(self, a, b):
#         return a+b
#     def subtract(self, a, b):
#         return a-b
#     def multiply(self, a, b):
#         return a*b
#     def divide(self, a, b):
#         if b == 0:
#             return "Dalyba is 0 negalima"
#         else:
#             return a/b
# a = 3
# b = 7
# a1 = Skaiciuotuvas()
# suma = a1.add(a, b)
# atimtis = a1.subtract(a, b)
# daugyba = a1.multiply(a, b)
# dalyba = a1.divide(a, b)
# print(f"{suma}, {atimtis}, {daugyba}, {dalyba}")


# Klases darbas 2023-09-13:
#
# 1. Sukurkite klasę "Klase", kuri turės savybę "pavadinimas" ir sąrašą "pamokos" (pamokų pavadinimai ir laikas).
# Sukurkite klasę "Mokykla", kuri turės sąrašą klasių. Parašykite metodą, kuris išveda mokyklos tvarkaraštį
# su visomis pamokomis.

#teisingas:
# class Klase:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.pamokos = []
#     def pamoka(self, pavadinimas, laikas):
#         self.pamokos.append((pavadinimas, laikas))
#     def tvarkarastis(self):
#         tvarkarastis = f"klase: {self.pavadinimas} \n" # \n = is naujos eilutes
#         for pamoka in self.pamokos:
#             pavadinimas, laikas = pamoka
#             tvarkarastis += f"- {pavadinimas}, laikas: {laikas} \n"
#         return tvarkarastis
# class Mokykla:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.klases = []
#     def sukurti_klase(self, klase):
#         self.klases.append(klase)
#     def bednras_tvarkarastis(self):
#         galutinis_tvarkarastis = f"Mokykla: {self.pavadinimas} \n"
#         for klase in self.klases:
#             galutinis_tvarkarastis += klase.tvarkarastis()
#         return galutinis_tvarkarastis
#
# mokykla = Mokykla("Svyturio Alus")
#
# klase1 = Klase("5b")
# pamoka1 = klase1.pamoka("Geografija", "8:00 - 8:45")
# pamoka2 = klase1.pamoka("Fizika", "8:55 - 9:40")
#
# klase2 = Klase("5c")
# pamoka1 = klase2.pamoka("Ekonomika", "8:00 - 8:45")
# pamoka2 = klase2.pamoka("Istorija", "8:00 - 8:45")
#
# mokykla.sukurti_klase(klase1)
# mokykla.sukurti_klase(klase2)
#
# tvarkarastis = mokykla.bednras_tvarkarastis()
#
# print(mokykla.bednras_tvarkarastis())



# Mano:
# class Mokykla:
#     def __init__(self, klases):
#         self.klases = klases
#     def klasiu_sarasas(self):
#         class Klase:
#             def __init__(self, pavadinimas):
#                 self.pavadinimas = pavadinimas
#                 self.pamokos = []
#
#             def pamokos_pavadinimas(self, sekanti_pamoka=1):
#                 self.pamokos = sekanti_pamoka
#                 return sekanti_pamoka
#
#             def pamokos_laikas(self):
#                 self.
#
#         class Mokykla:
#             def __init__(self, klases):
#                 self.klases = klases
#
#             def klasiu_sarasas(self):

# 2.Sukurkite klasę "Žaislas", kuri turėtų savybes, tokias kaip "pavadinimas" ir "amžiaus rekomendacija".
# Tada sukurkite klasę "Vaikas", kuri turėtų vardą ir amžių. Tada sukurkite klasę "VaikasSuZaislu",
# kuri turėtų šio vaiko objektą ir žaislo objektą. Patikrinkite, ar vaiko amžius atitinka žaislo amžiaus rekomendaciją.

# class Zaislas:
#     def __init__(self, pavadinimas, amziaus_rekomendacija):
#         self.pavadinimas = pavadinimas
#         self.amziaus_rekomendacija = amziaus_rekomendacija
#
# class Vaikas:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#
# class VaikasSuZaislu:
#     def __init__(self, vaikas, zaislas):
#         self.vaikas = vaikas
#         self.zaislas = zaislas
#     def amziaus_tikrinimas(self):
#         if self.vaikas.amzius >= self.zaislas.amziaus_rekomendacija:
#             return f"{self.vaikas.vardas} gali zaisti su zaislu '{self.zaislas.pavadinimas}'"
#         else:
#             return f"{self.vaikas.vardas} negali zaisti su zaislu '{self.zaislas.pavadinimas}' del amziaus apribojimo"
#
# zaislas1 = Zaislas("Lego 'StarWars'", 12)
# zaislas2 = Zaislas("'Monopolis'", 9)
# zaislas3 = Zaislas ("Pripuciama moteris", 18)
#
# vaikas1 = Vaikas("Algis", 7)
# vaikas2 = Vaikas("Austeja", 11)
# vaikas3 = Vaikas("Tomas", 16)
#
# vaikas_su_zaislu1 = VaikasSuZaislu(vaikas1, zaislas1)
# vaikas_su_zaislu2 = VaikasSuZaislu(vaikas2, zaislas2)
# vaikas_su_zaislu3 = VaikasSuZaislu(vaikas3, zaislas3)
# rezultatas = vaikas_su_zaislu1.amziaus_tikrinimas()
# rezultatas1 = vaikas_su_zaislu2.amziaus_tikrinimas()
# rezultatas2 = vaikas_su_zaislu3.amziaus_tikrinimas()
# print(rezultatas, rezultatas1, rezultatas2)


# 3. Sukurkite programą, kuri leidžia vartotojui valdyti krepšinio komandą. Galite kurti klases,
# pvz., "Komanda", "Žaidėjas", "Treneris". Kiekvienas žaidėjas turėtų turėti savo statistiką(taiklumas,pozicija),
# o treneris - instrukcijas ir strategiją(komandos sudeti). Programa turi leisti vartotojui pridėti naujus žaidėjus,
# juos treniruoti ir valdyti komandos sudeti.

# class Komanda:
#     def __init__(self, pavadinimas):
#         self.pavadinimas = pavadinimas
#         self.treneris = Treneris()
#         self.komanda = []
#     def prideti_zaideja(self, zaidejas):
#         self.komanda.append(zaidejas)
#     def isimti_zaideja(self, zaidejas):
#         if zaidejas in self.komanda:
#             self.komanda.remove(zaidejas)
#     def pasirinkti_treneri(self, treneris):
#         self.komanda.append(treneris)
#     def pakeisti_treneri(self, treneris):
#         if treneris in self.komanda:
#             self.komanda.remove(treneris)
#     def komandos_informacija(self):
#         print (f"{self.pavadinimas}, komandos zaidejai: ")
#         for zaidejas in self.komanda:
#             print(zaidejas.zaidejo_informacija())
#     def strategijos_informacija(self):
#         print (self.treneris.strategijos_informacija())
# class Zaidejas:
#     def __init__(self, vardas, pavarde, pozicija):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.taiklumas = 30
#         self.pozicija = pozicija
#     def upgrade(self):
#         self.taiklumas += 5
#         if self.taiklumas > 100:
#             self.taiklumas = 100
#     def zaidejo_informacija(self):
#         return f"{self.vardas} {self.pavarde}, zaidzia pozicijoje: {self.pozicija}, kurio taiklumas {self.taiklumas}%"
# class Treneris:
#     def __init__(self):
#         self.strategija = "ataka"
#     def keisti_strategija(self, nauja_strategija):
#         self.strategija = nauja_strategija
#     def strategijos_informacija(self):
#         return f"naudojama strategija: {self.strategija}"
#
# komanda1 = Komanda("Lietuva")
# zaidejas1 = Zaidejas("Jonas", "Maciulis", "Gynejas")
# zaidejas2 = Zaidejas("Jonas", "Valanciunas", "Centras")
# zaidejas3 = Zaidejas("Simas", "Jasaitis", "Puolejas")
# zaidejas4 = Zaidejas("Deividas", "Jurkus", "I-Zaudejas")
#
# komanda1.prideti_zaideja(zaidejas1)
# komanda1.prideti_zaideja(zaidejas2)
# komanda1.prideti_zaideja(zaidejas3)
# komanda1.prideti_zaideja(zaidejas4)
#
# zaidejas1.upgrade()
# zaidejas2.upgrade()
# zaidejas3.upgrade()
# zaidejas4.upgrade()
#
# komanda1.komandos_informacija()
# komanda1.strategijos_informacija()

#importuojame bibliotekas
import pandas as pd
import matplotlib.pyplot as plt
#sarasas su duomenimis
# duomenys = {"Vardas":["Jonas", "Ieva", "Petras", "Ona"],
#             "Amzius": [25, 28, 22, 30]
#             }
# #sukuriame DataFrame = df is saraso
# df = pd.DataFrame(duomenys)
#
# print(df)
#
# #filtruojame duomenis pagal amziu
# jaunesni = df[df["Amzius"] < 25 ]
# print(jaunesni)
#
# #jei norima paskaiciuoti vidutini amziu
# #mean skirtas skaiciuoti vidurki.
# vidutinis_amzius = df["Amzius"].mean()
# print(f"Vidutinis amzius: {vidutinis_amzius}")


# temperaturos = [24.5, 25.2, 23.8, 26.0, 22.5] #sarasas
# sr = pd.Series(temperaturos)
# # serija_rikiavimas = sr.sort_values()
# # serija_rikiavimas = sr.sort_values(ascending=False)
# # print(serija_rikiavimas)
# print(f"pirmas elementas: {sr[0]}")

# duomenys = {"Vardas":["Jonas", "Ieva", "Petras", "Ona"],
#             "Amzius": [25, 28, 22, 30]
#             }
# df = pd.DataFrame(duomenys)
# vardai = df["Vardas"]
# print("Vardai")
# print(vardai)

# duomenys = {"Vardas":["Jonas", "Ieva", "Petras", "Ona"],
#             "Amzius": [25, 28, 22, 30]
#             }
# df = pd.DataFrame(duomenys)
# vardai = df["Vardas"]. to_list()
# print("Vardai")
# print(vardai)

#Nauju stulpeliu pridejimas
# duomenys = {"Vardas":["Jonas", "Ieva", "Petras", "Ona"],
#             "Amzius": [25, 28, 22, 30]
#             }
# df = pd.DataFrame(duomenys)
# df["Lytis"] = ["Vyras", "Moteris", "BBZ kas", "Moteris"]
# print("Atnaujintas dataframe su nauju stulpeliu")
# # print(df)
# df.head(1)
# df.to_excel("duomenys.xlsx", index=False)

# plt.figure(figsize=(8,5))
# plt.bar(df["Vardas"], df["Amzius"], color="red")
# plt.xlabel("Vardas")
# plt.ylabel("Amzius")
# plt.title("Amzius pagal vardus")
# plt.show()

# data = {"Miestas": ["Vilnius","Kaunas", "Kaunas", "Vilnius"],
#         "Lytis": ["Vyras", "Vyras", "Moteris", "Vyras"],
#         "Amzius": [25, 25, 22, 30]
#         }
# data1 =pd.DataFrame(data)
#
# vidutinis_amzius_pagal_miesta = data1.groupby("Miestas")["Amzius"].mean()
# print(vidutinis_amzius_pagal_miesta)

# Sukurkite Pandas DataFrame(4 miestai ir ju populiacija).
# Filtravimas ir paieška:
# a. Filtruokite miestus, kurių populiacija yra didesnė nei 200 000 žmonių.
# b. Raskite miestą, turintį mažiausią populiaciją.
# Duomenų grupavimas ir agregavimas:
# a. Pridėkite stulpelį "Šalis" prie ankstesnio DataFrame, kuriame nurodoma, kuri šalis priklauso kiekvienam miestui
# (pvz., "Lietuva").
# b. Grupuokite duomenis pagal "Šalis" stulpelį ir apskaičiuokite bendrą populiaciją kiekvienai šaliai.
# Duomenų rikiavimas:
# Rikiuokite miestus pagal populiaciją mažėjimo tvarka.


