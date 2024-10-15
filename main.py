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
import random

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
# words1 = []
# words1.append(input("Iveskite pirma zodi: "))
# words1.append(input("Iveskite pirmo zodzio reiksme: "))
# words.append(words1)
# sorted_words = sorted(words, key=lambda x: x[0])
# print(sorted_words)
# words2 = []
# words2.append(input("Iveskite antra zodi: "))
# words2.append(input("Iveskite antro zodzio reiksme: "))
# words.append(words2)
# sorted_words = sorted(words, key=lambda x: x[0])
# print(sorted_words)
# words3 = []
# words3.append(input("Iveskite trecia zodi: "))
# words3.append(input("Iveskite trecio zodzio reiksme: "))
# words.append(words3)
# sorted_words = sorted(words, key=lambda x: x[0])
# print(sorted_words)

# print("************************************")
# print("------------15 uzd.----------------")
# balance = [["bulves", 3],
#            ["morkos", 4],
#            ["kriauses", 20],
#            ["saldainiai", 89],
#            ["kopustai", 100],
#            ["obuoliai", 2],
#            ["ropes", 55],
#            ["pienas", 45],
#            ["batonas", 1]]
# mod_balance = []
# for i in range(len(balance)):
#     if balance[i][1] < 5:
#         mod_balance.append(balance[i])
# print(f"Likuciai, kuriu like maziau nei 5 vnt.: {mod_balance[1, 2]}")
# if len(mod_balance) < 1:
#     sorted_balance = sorted(balance, key=lambda x: x[1])
#     print(f"Triju prekiu likuciai, kuriu like maziausiai: {sorted_balance[:3, 1]}")

# print("************************************")
# print("------------Papildoma 14.----------------")
# allowed_guesses = 5
# secret_number = 7
# for i in range(allowed_guesses):
#     input_number = int(input("Spek skaiciu: "))
#     if input_number == secret_number:
#         print("You guessed it!")
#         break
#     else:
#         print("Higher" if input_number < secret_number else "lower")

# print("**********************Ciklai***********************************")
# print("**********************FOR**************************************")
# print("************************************")
# print("-------------1 uzd.----------------")
# for i in range(5):
#     print("Rasa")
#
# print("************************************")
# print("-------------2 uzd.----------------")
# for i in range(11):
#     print(i)
#
# print("************************************")
# print("-------------3 uzd.----------------")
# for i in range(0,16,2):
#     print(i)
#
# print("************************************")
# print("-------------4 uzd.----------------")
# for i in range(1,21,3):
#     print(f"[{i}]")
#
# print("************************************")
# print("-------------5 uzd.----------------")
# for i in range(1,21):
#     if i % 4 == 0:
#         print(i)
#
# print("************************************")
# print("-------------6 uzd.----------------")
# for i in range(1,16):
#     if i % 2 == 0:
#         print(f"{i} - lyginis")
#     else:
#         print(f"{i} - nelyginis")
#
# print("************************************")
# print("-------------7 uzd.----------------")
# start = 1
# end = 10
# if start < end:
#     for i in range(start, end):
#         print(f"{i} {i**2}")
#
# print("************************************")
# print("-------------8 uzd.----------------")
# start = 1
# end = 10
# if start < end:
#     for i in range(start, end):
#         if i % 2 != 0 or i % 8 == 0:
#             print(i)
#
# print("************************************")
# print("-------------9 uzd.----------------")
# name = input("Iveskite savo varda: ")
# for letter in name:
#     print(f"Labas, {name}")
#
# print("************************************")
# print("------------10 uzd.----------------")
# for elementas in [88, 65, 21, 26, 47]:
#     if elementas % 2 == 0:
#         print(elementas)

# print("************************************")
# print("------------11 uzd.----------------")
# start = int(input("Iveskite reziu pradzia: "))
# end = int(input("Iveskite reziu pabaiga: "))
# step = int(input("Iveskite zingsni: "))
# even = input("Iveskite, kokius skaicius norite matyti (Lyginiai - L, Nelyginiai - N): ")
# if start < end:
#     for i in range(start, end, step):
#         if even == 'L' and i % 2 == 0:
#             print(i)
#         elif even == 'N' and i % 2 != 0:
#             print(i)

# print("************************************")
# print("------------12 uzd.----------------")
# size = int(input("Kokio dydzio eglute noretumet matyti: "))
# for i in range(size + 1):
#     line = ""
#     for j in range(i):
#         line += "*"
#     print(line)

# print("************************************")
# print("------------13 uzd.----------------")
# word = input("Iveskite zodi: ")
# count = int(input("Kiek kartu bus kartojama kiekviena raide: "))
# for letter in word:
#     repeated_letter = ""
#     for j in range(count):
#         repeated_letter += letter
#     print(repeated_letter)

# print("************************************")
# print("------------14 uzd.----------------")
# sk1 = 7
# sk2 = 9
# result = 0
# for i in range(sk1):
#     result += sk2
# print(result)

# print("************************************")
# print("------------15 uzd.----------------")
# sum = 0
# for i in range (1,101):
#     sum += i
# print(sum)

# print("************************************")
# print("------------16 uzd.----------------")
# sum = 0
# for i in range (20,51):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# print("************************************")
# print("------------17 uzd.----------------")
# sum = 0
# for i in range(30, 61):
#     if i % 2 != 0:
#         sum += i
# print(sum)

# print("************************************")
# print("------------18 uzd.----------------")
# sum = 0
# for i in range(1, 1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print(sum)

# print("************************************")
# print("------------19 uzd.----------------")
# sum = 0
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
# print(sum)
#
# print("************************************")
# print("------------20 uzd.----------------")
# sk1 = 1
# sk2 = 1
# sk3 = sk1 + sk2
# print(sk1)
# print(sk2)
# print(sk3)
# for i in range(40):
#     sk1 = sk2
#     sk2 = sk3
#     sk3 = sk1 + sk2
#     print(sk3)

# print("**********************WHILE************************************")
# print("************************************")
# print("-------------1 uzd.----------------")
# num = 1
# while num < 21:
#     print(num)
#     num += 1
#
# print("************************************")
# print("-------------2 uzd.----------------")
# num = 1
# while num < 51:
#     if num % 2 == 0:
#         print(f"{num} - lyginis")
#     else:
#         print(f"{num} - nelyginis")
#     num += 1
#
# print("************************************")
# print("-------------3 uzd.----------------")
# num = 25
# while num < 51:
#     if num % 3 == 0:
#         print("Dalinasi is 3")
#     else:
#         print(num)
#     num += 1
#
# print("************************************")
# print("-------------4 uzd.----------------")
# num = 1
# while num < 101 and num % 7 != 0:
#     print(num)
#     num += 1

# print("************************************")
# print("-------------5 uzd.----------------")
# num = 1
# while num % 3 != 0 or num % 5 != 0:
#     print(num)
#     num += 1

# print("************************************")
# print("-------------6 uzd.----------------")
# while True:
#     start = int(input("Iveskite reziu pradzia: "))
#     end = int(input("Iveskite reziu pabaiga: "))
#     if start >= end:
#         print("Rezius ivedete neteisingai, prasau pakartokite is naujo...")
#     else:
#         break
#
# for i in range(start, end):
#     if i % 2 == 0:
#         print(f"{i} {i**2} - lyginis")
#     else:
#         print(f"{i} {i**2} - nelyginis")

# print("************************************")
# print("-------------7 uzd.----------------")
# num = 1
# while True:
#     is_prime = True
#     i = 2
#     while i < num:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1
#     if num > 20 and is_prime == True:
#         break
#     print(num)
#     num += 1
#
# print("************************************")
# print("-------------8 uzd.----------------")
# sum = 0
# while True:
#     num = int(input("Iveskite nauja skaiciu (jei nobenoresite testi, iveskite nuli): "))
#     sum += num
#     if num == 0:
#         break
# print(f"Suma: {sum}")

# print("************************************")
# print("-------------9 uzd.----------------")
# repeat = 't'
# while repeat == 't':
#     num1 = int(input("Iveskite pirma skaiciu: "))
#     num2 = int(input("Iveskite antra skaiciu: "))
#     print(f"Skaiciai: {num1} ir {num2}")
#     print(f"Suma: {num1} + {num2} = {num1 + num2}")
#     print(f"Atimtis: {num1} - {num2} = {num1 - num2}")
#     print(f"Daugyba: {num1} * {num2} = {num1 * num2}")
#     print(f"Dalyba: {num1} / {num2} = {num1 / num2}")
#     repeat = input("Ar norite kartoti? t/n")

# print("************************************")
# print("------------10 uzd.----------------")
# repeat = 't'
# while repeat == 't':
#     num2 = int(input("Iveskite skaiciu, kurio daugybos lentele norite matyti: "))
#     num1 = 1
#     while num1 < 10:
#         print(f"{num2} * {num1} = {num2*num1}")
#         num1 += 1
#     repeat = input("Ar norite testi (t/n)?")

# print("************************************")
# print("------------11 uzd.----------------")
# sum = 0
# count = 0
# while True:
#     num = int(input("Iveskite skaiciu (kai nebenoresite testi, iveskite 0): "))
#     if num == 0:
#         break
#     sum += num
#     count += 1
# print(f"Ivestu skaicius suma: {sum}, vidurkis: {sum / count}")

# print("************************************")
# print("------------12 uzd.----------------")
# repeat = 't'
# while repeat == 't':
#     pazymiu_suma = 0
#     pazymiu_kiekis = 0
#     print('Iveskite tiek pazymiu kiek norite (atskiriant enter)')
#     print('Norint baigti irasykite 0')
#     while True:
#         pazymys = int(input('Iveskite pazymi: '))
#         if pazymys == 0:
#             break
#         pazymiu_suma += pazymys
#         pazymiu_kiekis += 1
#     vidurkis = round(pazymiu_suma / pazymiu_kiekis, 1)
#     print('Suvestu pazymiu vidurkis:', vidurkis)
#     repeat = input('Ar norite testi (t/n)? ')

# print("************************************")
# print("------------13 uzd.----------------")
finished = False
while finished == False:
    min = int(input("Iveskite maziausia galima skaiciu: "))
    max = int(input("Iveskite didziausia galima skaiciu: "))
    secret = random.randint(min, max)
    print(f"Secret number: {secret}")
    need_help = input("Ar norite pagalbos (t/n)? ")
    if (need_help != 't' and need_help != 'n'):
        continue
    repeat_endless = input("Ar norite speti neribota sk. (t/n)? ")
    if (repeat_endless != 't' and repeat_endless != 'n'):
        continue
    guess_count = 0
    guess_count_max = 0
    if repeat_endless == 'n':
        guess_count_max = int(input("Iveskite, kiek spejimu leidziama: "))
    guessed = False
    while guessed == False and (repeat_endless == 't' or guess_count < guess_count_max):
        guessed_number = int(input("Spekite skaiciu: "))
        if guessed_number != secret:
            if need_help == 't':
                if (guessed_number < secret):
                    print("Iveskite didesni skaiciu")
                else:
                    print("Iveskite mazesni skaiciu")
            if repeat_endless == 'n':
                guess_count += 1
        else:
            guessed = True
            print("Atspejote!!!")
    finished = True





