# print("************************************")
# print("-------------1 uzd.----------------")
# names = ["Aras", "Petras", "Lina", "Danielius", "Zita"]
# print(names)
# print(names[0])
# print(names[-1])
# print(len(names))
#
# print("************************************")
# print("-------------2 uzd.----------------")
# heights = [169, 178, 203, 145, 160]
# print(heights)
# print(len(heights))
#
# print("************************************")
# print("-------------3 uzd.----------------")
# grades = []
# grades.append(input("Iveskite 1-a pazymi: "))
# grades.append(input("Iveskite 2-a pazymi: "))
# grades.append(input("Iveskite 3-a pazymi: "))
# grades.append(input("Iveskite 4-a pazymi: "))
# print(f"Visi pazymiai: {grades}")
# print(f"Is viso pazymiu: {len(grades)}")
from itertools import count

# print("************************************")
# print("-------------4 uzd.----------------")
# towns = ["Kaunas", "Vilnius", "Klaipeda"]
# print(f"Pradinis masyvas: {towns}")
# towns.append(input("Iveskite miesta: "))
# towns.append(input("Iveskite dar viena miesta: "))
# print(f"Papildytas masyvas: {towns}")
# index = int(input("Iveskite i kuria vieta norite papildyti miesta: "))
# newTown = input("Iveskite miesta: ")
# towns.insert(index, newTown)
# print(f"Papildytas masyvas: {towns}")

# print("************************************")
# print("-------------5 uzd.----------------")
# names = ["Aras", "Petras", "Lina", "Danielius", "Zita", "Zoja", "Liuda", "Juozas"]
# print(names)
# names.pop()
# names.pop()
# names.pop()
# print(names)
# count = int(input("Kiek dar norite pasalint duomenu? "))
# for name in range(count):
#     names.pop()
# print(names)

# print("************************************")
# print("-------------6 uzd.----------------")
# names = ["Aras", "Petras", "Lina", "Danielius", "Zita", "Zoja", "Liuda", "Juozas"]
# print(names)
# if len(names) > 5:
#     names.clear()
# print(names)

# print("************************************")
# print("-------------7 uzd.----------------")
# names = ["Aras", "Petras", "Lina", "Danielius", "Zita", "Zoja", "Liuda", "Juozas"]
# print(names)
# name = input("Iveskite varda: ")
# if name in names:
#     print(f"Vardas masyve egzistuoja sioje pozicijoje: {names.index(name)}")
# else:
#     print("Vardas masyve neegzistuoja")

# print("************************************")
# print("-------------8 uzd.----------------")
# grades = [10, 9, 5, 7, 6, 10, 8]
# print(f"Desimtuku skaicius: {grades.count(10)}")

# print("************************************")
# print("-------------9 uzd.----------------")
# car_brands = ["Tesla", "Toyota", "Ferrari", "Kia", "Ford"]
# print(car_brands)
# car_brands.sort()
# print(car_brands)
# car_brands.reverse()
# print(car_brands)

# print("************************************")
# print("------------10 uzd.----------------")
# grades = [10, 9, 5, 7, 6, 10, 8]
# print(grades)
# grades.sort()
# print(grades)
# print(grades[-3:])

# print("************************************")
# print("------------11 uzd.----------------")
# grades = [1, 10, 9, 3, 5, 7, 6, 2, 10, 8, 4, 3]
# print(grades)
# count = 0
# for grade in grades:
#     if grade <= 4:
#         count += 1
# print(f"Is viso neigiamu pazymiu: {count}")

# print("************************************")
# print("------------12 uzd.----------------")
# grades = [1, 10, 9, 3, 5, 7, 6, 2, 10, 8, 4, 3]
# print(f"Visi: {grades}")
# print(f"Pirmi trys nariai: {grades[:3]}")
# print(f"Du nariai pradedant treciuoju: {grades[2:4]}")
# print(f"Paskutiniai keturi nariai: {grades[-4:]}")
# print(f"Kas antras narys, pradedant trečiuoju: {grades[2::2]}")
# grades.reverse()
# print(f"Visi atbuline tvarka: {grades}")

# print("************************************")
# print("------------13 uzd.----------------")
# grade_averages = [8.5, 6.4, 9.2, 5.1, 9.5, 9.75]
# print(grade_averages)
# grade_averages.sort()
# max_averages = grade_averages[-3:]
# print(max_averages)

# print("************************************")
# print("------------14 uzd.----------------")
# words = []
# words.append(input("Iveskite pirma zodi: "))
# words.sort()
# print(words)
# words.append(input("Iveskite antra zodi: "))
# words.sort()
# print(words)
# words.append(input("Iveskite trecia zodi: "))
# words.sort()
# print(words)
# words.append(input("Iveskite ketvirta zodi: "))
# words.sort()
# print(words)

print("************************************")
print("------------15 uzd.----------------")
balance = [3, 4, 20, 89, 100, 2, 55, 45, 1, 0]
mod_balance = []
mod_balance2 = []
for residual in balance:
    if residual < 5:
        mod_balance.append(residual)
print(f"Likuciai, kuriu like maziau nei 5 vnt.: {mod_balance}")
balance.sort()
print(f"Triju prekiu likuciai, kuriu like maziausiai: {balance[:3]}")