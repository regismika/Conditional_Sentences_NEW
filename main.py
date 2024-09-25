# 1 Liepkite vartotojui suvesti savo amžių. Patikrinkite ar amžius yra
# didesnis arba lygus 18-ai, jei taip - išveskite "jūs galite balsuoti"
#
# print("Iveskite savo amziu")
# skaicius = int(input())
# if skaicius >= 18:
#     print("Esate pilnametis ir galite balsuoti")
# else: print("esate nepilnametis ir balsyoti negalite")
#
# 2 Leiskite vartotojui suvesti norimą kiekį pažymių (pavyzdžiui, jūs
# nusimatote 3-is kintamuosius, tai leidžiate padaryti 3 įvedimus). Raskite
# šių pažymių vidurkį. Patikrinkite ar vidurkis teigiamas (daugiau arba lygu
# 5-iems), jei taip - išveskite "vidurkis teigiamas"
import random

# print("iveskite 1-a skaiciu")
# skaicius1 = int(input())
# print("iveskite 2-a skaiciu")
# skaicius2 = int(input())
# print("iveskite 3-a skaiciu")
# skaicius3 = int(input())
# print(f'jus ivedete {skaicius1}, {skaicius2}, {skaicius3}')
# Pazymiu_Vidurkis = (skaicius1 + skaicius2 + skaicius3) / 3
# print(f'jusu Pazymiu_vudirkis yra {Pazymiu_Vidurkis}')
# if Pazymiu_Vidurkis >= 5:
#     print("Pazimys teigiamas")
# else:
#     print("Pazimys neigiamas")

# 3 Susikurkite skaičiaus kintamąjį arba leiskite šį skaičių įvesti vartotojui.
# Atlikite šiuos patikrinimus ir veiksmus:
# 1. Jei skaičius dalinasi iš 5, tuomet išveskite šio skaičiaus daugybos lentelę nuo 1 iki 5.
# 2. Jei skaičius lyginis, tuomet išveskite šį skaičių, jo kvadratą ir jį padalintą iš 2.
# 3. Jei skaičius nesidalina iš 7, tuomet susikurkite antrąjį kintamąjį, išveskite šių dviejų skaičių
# sumą, skirtumą, sandaugą, dalmenį

# print("Iveskite skaiciu")
# skaicius = int(input())
# if skaicius % 5 == 0:
#     print(f"1 * {skaicius} {1*skaicius} \n 2 * {skaicius} {2*skaicius} \n 3 * {skaicius} {3*skaicius} \n 4 * {skaicius} {4*skaicius} \n 5 * {skaicius} {5*skaicius}")
# if skaicius % 2 == 0:
#     result = (skaicius) * (skaicius) / 2
#     print(result)
# if skaicius % 7 != 0:
#    print("Iveskite dar viena skaiciu")
#    skaiciusX = int(input())
#    suma = skaicius + skaiciusX
#    skirtumas = skaicius - skaiciusX
#    sandauga = skaicius * skaiciusX
#    dalmuo = skaicius / skaiciusX
#    print("suma:", (suma), "skirtumas:", (skirtumas), "sandauga:", (sandauga), "dalmuo:", (dalmuo))

# 4 Sukurkite 4 kintamuosius, kurie saugotų jūsų vardą, pavardę, gimimo metus ir šiuos metus (nebūtinai tikrus). Parašykite kodą, kuris pagal gimimo metus
# paskaičiuotų jūsų amžių ir naudodamas vardo ir pavardės kintamuosius atspausdintų tokį sakinį: "Aš esu Vardenis Pavardenis. Man yra XX metai(ų)".

# Vardas = "Regimantas"
# Pavarde = "Mikaliunas"
# Gimes = 1979
# Sie_metai = 2024
# Amzius = Sie_metai - Gimes
# print(f'As esu {Vardas} {Pavarde}. Man yra {Amzius}')

# 5 Sukurkite du kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite atsitiktines reikšmes nuo 0 iki 4.
# Didesnę reikšmę padalinkite iš mažesnės. Atspausdinkite rezultatą jį suapvalinę iki 2 skaičių po kablelio.

# random_number1 = random.randint(0, 4)
# random_number2 = random.randint(0, 4)
# print(random_number1)
# print(random_number2)
# if random_number1 != 0 and random_number2 != 0:
#     if random_number1 > random_number2:
#         print(round(random_number1 / random_number2, 2))
#     else:
#         print(round(random_number2 / random_number1, 2))
# else:
#         print("dalyba negalima")

# 6 Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius ir naudodamiesi funkcija random.randint(x,x) jiems priskirkite
# atsitiktines reikšmes nuo 0 iki 25. Raskite ir atspausdinkite kintąmąjį turintį vidurinę reikšmę.

# random_number1 = random.randint(0,25)
# random_number2 = random.randint(0,25)
# random_number3 = random.randint(0,25)
# print(random_number1)
# print(random_number2)
# print(random_number3)
# if random_number1 > random_number2 and random_number1 < random_number3 or random_number1 > random_number3 and random_number1 < random_number2:
#     print(f'Vidurinis skaičius: {random_number1}')
# elif random_number2 > random_number1 and random_number2 < random_number3 or random_number2 > random_number3 and random_number2 < random_number1:
#     print(f'Vidurinis skaičius: {random_number2}')
# elif random_number3 > random_number1 and random_number3 < random_number2 or random_number3 > random_number2 and random_number3 < random_number1:
#     print(f'Vidurinis skaičius: {random_number3}')
# else:
#     print("UPS")

# 7 Įvedami skaičiai - a, b, c –kraštinių ilgiai, trys kintamieji (naudokite random.randint(x,x) funkciją nuo 1 iki 10). Parašykite Python programą,
# kuri nustatytų, ar galima sudaryti trikampį ir atsakymą atspausdintų.

# krastineA = random.randint(0,10)
# krastineB = random.randint(0,10)
# krastineC = random.randint(0,10)
# print(f' Kraštinė A: {krastineA}, Kraštinė B: {krastineB}, Kraštinė C: {krastineC}')
# if krastineA + krastineB > krastineC and krastineA + krastineC > krastineB and krastineB + krastineC > krastineA:
#     print("Trikampis sudaromas")
# else:
#     print("Trikampio nesudarysi")

# 8 Sukurkite keturis kintamuosius ir random.randint(x,x) funkcija sugeneruokite jiems reikšmes nuo 0 iki 2.
# Suskaičiuokite kiek yra nulių, vienetų ir dvejetų. (sprendimui masyvo nenaudoti).

knt1 = random.randint(0,2)
knt2 = random.randint(0,2)
knt3 = random.randint(0,2)
knt4 = random.randint(0,2)
print(knt1)
print(knt2)
print(knt3)
print(knt4)
if knt1 == knt2 == knt3 == knt4:
    print(knt1 + knt2 + knt3 + knt4)
# elif knt1 == 1 and knt2 == 1 and knt3 == 1 and knt4 == 1:
#     print(knt1 + knt2 + knt3 + knt4)
# elif knt1 == 2 and knt2 == 2 and knt3 == 2 and knt4 == 2:
#     print(knt1 + knt2 + knt3 + knt4)
else:
    print("Finito")




# 9 Naudokite funkcija random.randint(x,x). Sukurkite ir atspausdinkite 3 skaičius nuo -10 iki 10. Skaičiai mažesni už 0 turi būti  laužtiniuose skliaustuose
# [], 0 -  (), didesni už 0 {}.   [-4],  (0)


# 10 Įmonė parduoda žvakes po 1 EUR. Perkant daugiau kaip 1000 vienetų taikoma 3 % nuolaida, daugiau kaip 2000 vienetų- 4 % nuolaida.
# Parašykite programą, kuri skaičiuos žvakių kainą ir atspausdintų atsakymą kiek žvakių ir kokia kaina perkama. Žvakių kiekį
# generuokite random.randint(x,x) funkcija nuo 5 iki 3000.



# 11 Naudokite funkcija random.randint(x,x). Sukurkite tris kintamuosius su atsitiktinėm reikšmėm nuo 0 iki 100.
# Paskaičiuokite jų aritmetinį vidurkį. Ir aritmetinį vidurkį atmetus tas reikšmes, kurios yra mažesnės nei 10 arba didesnės nei 90.
# Abu vidurkius atspausdinkite. Rezultatus apvalinkite iki sveiko skaičiaus.




# 12 Padarykite skaitmeninį laikrodį, rodantį valandas, minutes ir sekundes. Valandom, minutėm ir sekundėm sugeneruoti panaudokite funkciją random.randint(x,x).
# Sugeneruokite skaičių nuo 0 iki 300. Tai papildomos sekundės. Skaičių pridėkite prie jau sugeneruoto laiko. Atspausdinkite laikrodį prieš ir po
# sekundžių pridėjimo ir pridedamų sekundžių skaičių.


# 13 Naudokite funkcija random.randint(x,x). Sugeneruokite 6 kintamuosius su atsitiktinem reikšmėm nuo 1000 iki 9999. Atspausdinkite reikšmes viename strige,
# išrūšiuotas nuo didžiausios iki mažiausios, atskirtas tarpais. Naudoti ciklų ir masyvų NEGALIMA.




