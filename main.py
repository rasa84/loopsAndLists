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
#
# print("************************************")
# print("------------16 uzd.----------------")
# numbers = ['one', 'two', 'three', 'four', 'five']
# comma_separated_numbers = ""
# pipe_separated_numbers = ""
# space_separated_numbers = ""
# for num in numbers:
#     comma_separated_numbers += num + ", "
#     pipe_separated_numbers += num + "|"
#     space_separated_numbers += num + " "
# print(f"{comma_separated_numbers[:-2]}")
# print(f"{pipe_separated_numbers[:-1]}")
# print(f"{space_separated_numbers[:-1]}")

# print("************************************")
# print("------------17 uzd.----------------")
# numbers = ['python', 'web', 'file1.py', 'file2.py', 'file3.py']
# language, env, *files = numbers
# print(f"{language}, {env}, {files}")

# print("************************************")
# print("------------18 uzd.----------------")
# team_members = ['Jonas Jonaitis', 'Petras Petraitis', 'Agne Agnyte']
# print("prie projekto dirba šie komandos nariai:")
# for mem in team_members:
#     print(mem)

# print("************************************")
# print("------------19 uzd.----------------")
# topics = ["Conditional statements", "Arrays", "Loops"]
# print("We have already learned: ")
# for index in range(len(topics)):
#     print(f"{index + 1}-a tema: {topics[index]}")
# print("We have already learned: ")
# index = 0
# while index < len(topics):
#     print(f"{index + 1}-a tema: {topics[index]}")
#     index += 1

# print("************************************")
# print("------------20 uzd.----------------")
# programs = ["JavaScript mokymai", "Ilgieji Javascript \"Full-stack\" mokymai", "Nuo JAVA pagrindų iki mobilių aplikacijų kūrimo", "DevOps + Dirbtinis intelektas (AI)"]
# for p in programs:
#     print(p)

# print("************************************")
# print("------------21 uzd.----------------")
# countries = ["Lithuania", "Latvia", "Estonia"]
# for c in countries:
#     print(f"Country {c}")

# print("************************************")
# print("------------22 uzd.----------------")
# shopping_card = ["milk", "cheese", "carrots"]
# print(f"Total: {len(shopping_card)}")
# for i in range(len(shopping_card)):
#     print(f"nr {i + 1} product: {shopping_card[i]}")

# print("************************************")
# print("------------23 uzd.----------------")
# grades = [10, 9, 8, 2, 6, 4, 7]
# grades.sort()
# grades.reverse()
# for g in grades:
#     print(f"{g} - {"puikiai" if g == 10 else "labai gerai" if g == 9 else 'gerai' if g == 8 else 'vidutiniskai' if g == 7 else "patenkinamai arba nepatenkinamai"}")

# print("************************************")
# print("------------24 uzd.----------------")
# count = int(input("Kiek atsitiktiniu skaiciu turi buti sugeneruota: "))
# nums = []
# for i in range(count):
#     nums.append(random.randint(1, 10))
# print(nums)
# for n in nums:
#     print(f"{n} {n**2}")

# print("************************************")
# print("------------25 uzd.----------------")
# list = ["vienas", "du", "trys", "four", "five"]
# print(list)
# list[0] = "one"
# list[1] = "two"
# list[2] = "three"
# print(list)

# print("************************************")
# print("------------26 uzd.----------------")
# numbers = [8, 5, 7, 1, 6, 8, 10, 9]
# print("Lyginiai skaiciai: ")
# for n in numbers:
#     if n % 2 == 0:
#         print(n)
# print("Nelyginiai skaiciai: ")
# for n in numbers:
#     if n % 2 != 0:
#         print(n)
# print("Visi skaičiai, kurie dalinasi iš 3: ")
# for n in numbers:
#     if n % 3 == 0:
#         print(n)

# print("************************************")
# print("------------27 uzd.----------------")
# nums = [random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)]
# print(nums)
# sum = 0
# for n in nums:
#     sum += n
# average = sum / len(nums)
# print(f"Vidurkis: {average}")
# print("Skaiciai didesni nei vidurkis")
# for n in nums:
#     if n > average:
#         print(n)
#
# print("************************************")
# print("------------28 uzd.----------------")
# count = int(input("Kiek atsitiktiniu skaiciu turi buti sugeneruota: "))
# nums = []
# for i in range(count):
#     nums.append(random.randint(1, 10))
# print(nums)
# for n in nums:
#     divisors = ""
#     for i in range(n):
#         if n % (i + 1) == 0:
#             divisors += str(i + 1) + ", "
#     print(f"skaicius {n} dalinasi is {divisors[:-2]}")

# print("************************************")
# print("------------29 uzd.----------------")
# count = int(input("Iveskite, kiek zodziu norite ivesti: "))
# words = []
# for i in range(count):
#     words.append(input("Iveskite zodi: "))
# print(words)

# print("************************************")
# print("------------30 uzd.----------------")
# words = ["apple", "carrot", "milk"]
# for w in words:
#     print(f"{w} - {len(w)}")

# print("************************************")
# print("------------31 uzd.----------------")
# count = int(input("Kiek pazymiu norite ivesti: "))
# negative_grades = []
# sum = 0
# negative_count = 0
# for i in range(count):
#     grade = int(input("Iveskite pazymi: "))
#     sum += grade
#     if (grade < 5):
#         negative_count += 1
#         negative_grades.append(grade)
# print(f"Vidurkis: {sum / count}")
# print(f"Neigiamu pazymiu kiekis: {negative_count}" if negative_count > 0 else "")
# print("Neigiami pažymiai: " + str(negative_grades) if negative_count > 0 else "")

# print("************************************")
# print("------------32 uzd.----------------")
# words = ["apple", "carrot", "milk", "soup"]
# words_and_lengths = []
# for w in words:
#     words_and_lengths.append([w, len(w)])
# sorted_words = sorted(words_and_lengths, key=lambda x: x[1])
# print(f"Visi zodziai su raidziu kiekiais: {words_and_lengths}")
# print(f"Trumpiausias zodis: {sorted_words[0][0]}. Raidziu kiekis: {sorted_words[0][1]}")
# print(f"Ilgiausias zodis: {sorted_words[-1][0]}. Raidziu kiekis: {sorted_words[-1][1]}")

# print("************************************")
# print("------------33 uzd.----------------")
# numbers = []
# sum = 0
# numbers_bellow_average = []
# numbers_bellow_average_count = 0
# numbers_bellow_average_sum = 0
# numbers_above_average = []
# numbers_above_average_count = 0
# numbers_above_average_sum = 0
# for num in range(1, 101):
#     numbers.append(num)
#     sum += num
# average = sum / 100
# numbers.sort()
# min = numbers[0]
# max = numbers[-1]
# print(f"Visi skaiciai: {numbers}")
# print(f"Vidurkis: {average}")
# print(f"Min: {min}")
# print(f"Max: {max}")
# round_average = int(average)
# numbers_bellow_average_count = round_average - 1;
# for num in range(1, round_average):
#     numbers_bellow_average.append(num)
#     numbers_bellow_average_sum += num
# print(f"Zemesni nei vidurkis: {numbers_bellow_average}")
# print(f"Ju vidurkis: {round(numbers_bellow_average_sum / numbers_bellow_average_count, 2)}")
# numbers_above_average_count = 100 - round_average - 1;
# for num in range(round_average + 1, 101):
#     numbers_above_average.append(num)
#     numbers_above_average_sum += num
# print(f"Didesni nei vidurkis: {numbers_above_average}")
# print(f"Ju vidurkis: {round(numbers_above_average_sum / numbers_above_average_count, 2)}")

# print("************************************")
# print("------------34 uzd.----------------")
# words = ["apple", "carrot", "milk"]
# word_lengths = []
# for w in words:
#     word_lengths.append(len(w))
# word_lengths.sort()
# print(word_lengths[-1] - word_lengths[0])

# print("************************************")
# print("------------35 uzd.----------------")
# count = int(input("Kiek pazymiu norite ivesti: "))
# grades1 = []
# grades2 = []
# sum1 = 0
# sum2 = 0
# negative_count1 = 0
# negative_count2 = 0
#
# for i in range(count):
#     grade = int(input("Iveskite 1-o studento pazymi: "))
#     sum1 += grade
#     if (grade < 5):
#         negative_count1 += 1
#
# for i in range(count):
#     grade = int(input("Iveskite 2-o studento pazymi: "))
#     sum2 += grade
#     if (grade < 5):
#         negative_count2 += 1
# average1 = sum1 / count
# average2 = sum2 / count
# print(f"Pirmo studento vidurkis {average1} yra geresnis, nes antro studento tik {average2}"
#       if average1 > average2 else f"Antro studento vidurkis {average2} yra geresnis, nes pirmo studento tik {average1}"
# if average1 < average2 else "Vidurkiai lygus")
# print(f"Pirmas studentas turi neigiamu pazymiu " if negative_count1 > 0 else "",
#       end="\n" if negative_count1 > 0 else "")
# print(f"Antras studentas turi neigiamu pazymiu " if negative_count2 > 0 else "", end="")

# print("************************************")
# print("------------36 uzd.----------------")
# nums = []
# sum = 0
# for i in range(20):
#     number = random.randint(1, 20)
#     nums.append(number)
#     if number % 4 == 0:
#         sum += number
# print(nums)
# print(f"Skaiciu, kurie dalinasi is 4, suma: {sum}")

# print("************************************")
# print("------------37 uzd.----------------")
# numbers = [10, 5, 8, 9]
# for num in numbers:
#     if num % 2 == 0:
#         print(f"{num} {num ** 2}")
#     else:
#         print(num)

# print("************************************")
# print("------------38 uzd.----------------")
# grades = [10, 5, 3, 2, 8, 4, 9]
# for g in grades:
#     print(f"{g} - teigiamas" if g > 4 else f"{g} - neigiamas. Iki teigiamo trūko {5 - g}")

# print("************************************")
# print("------------39 uzd.----------------")
# words = ["one", "two", "three"]
# total = 0
# for w in words:
#     print(f"{w} {len(w)}")
#     total += len(w)
# print(f"Is viso raidziu: {total}")

# print("************************************")
# print("------------40 uzd.----------------")
# nums = [8, 5, 9, 3, 7]
# print(nums)
# sum = 0
# count = 0
# for n in nums:
#     if n % 3 == 0:
#         sum += n
#         count += 1
# print(f"Suma: {sum}. Vidurkis: {sum / count}")

# print("************************************")
# print("------------41 uzd.----------------")
# files = ["hi.py", "labas.txt", "data.json", "something.java"]
# appropriate_files = []
# for f in files:
#     if f.endswith("txt") or f.endswith("json"):
#         appropriate_files.append(f)
# print(f"Visi failai: {files}")
# print(f"Atrinkti failai: {appropriate_files}")

# print("************************************")
# print("------------42 uzd.----------------")
# errors = [["ui87", "Grafinės sąsajos klaida navigacijoje"],
#          ["sys12", "Trūksta operatyviosios atminties sistemoje"],
#          ["error999", "Iš esmės kažkas labai blogai"]]
# for e in errors:
#     print(e[1])

# print("************************************")
# print("------------43 uzd.----------------")
# balance = [
#     ["kopustai", 74],
#     ["morkos", 54],
#     ["agurkai", 32]]
# print(balance)
# list = []
# for b in balance:
#     days = int(round(b[1] / 5, 0))
#     print(f"Likutis {b[1]} vnt., užteks maždaug {days} dienų")
#     if days <= 7:
#         list.append(b[0])
# print(f"Siu prekiu uzteks savaitei ar maziau: {list}")

# print("************************************")
# print("------------44 uzd.----------------")
# words = ["one", "sixteen", "two", "seventeen", "three", "four", "eighteen"]
# short_words = []
# for w in words:
#     if len(w) <5:
#         short_words.append(w)
# print(f"Visi zodziai: {words}")
# print(f"Trumpi zodziai: {short_words}")

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
# start = -1
# end = -2
# step = int(input("Iveskite zingsni: "))
# even = input("Iveskite, kokius skaicius norite matyti (Lyginiai - L, Nelyginiai - N): ")
# while start > end:
#     start = int(input("Iveskite reziu pradzia: "))
#     end = int(input("Iveskite reziu pabaiga: "))
#     for i in range(start, end, step):
#         if even == 'L' and i % 2 == 0:
#             print(i)
#         if even == 'N' and i % 2 != 0:
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
# start = -1
# end = -2
# while start >= end:
#     start = int(input("Iveskite reziu pradzia: "))
#     end = int(input("Iveskite reziu pabaiga: "))
#     if start >= end:
#         print("Rezius ivedete neteisingai, prasau pakartokite is naujo...")
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
# num = -1
# while num != 0:
#     num = int(input("Iveskite nauja skaiciu (jei nobenoresite testi, iveskite nuli): "))
#     sum += num
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
# num = -1
# while num != 0:
#     num = int(input("Iveskite skaiciu (kai nebenoresite testi, iveskite 0): "))
#     sum += num
#     count += 1
# print(f"Ivestu skaicius suma: {sum}, vidurkis: {sum / (count - 1)}")

# print("************************************")
# print("------------12 uzd.----------------")
# repeat = 't'
# while repeat == 't':
#     pazymiu_suma = 0
#     pazymiu_kiekis = 0
#     pazymys = -1
#     print('Iveskite tiek pazymiu kiek norite (atskiriant enter)')
#     print('Norint baigti irasykite 0')
#     while pazymys != 0:
#         pazymys = int(input('Iveskite pazymi: '))
#         pazymiu_suma += pazymys
#         pazymiu_kiekis += 1
#     vidurkis = round(pazymiu_suma / (pazymiu_kiekis - 1), 1)
#     print('Suvestu pazymiu vidurkis:', vidurkis)
#     repeat = input('Ar norite testi (t/n)? ')

# print("************************************")
# print("------------13 uzd.----------------")
# finished = False
# while finished == False:
#     min = int(input("Iveskite maziausia galima skaiciu: "))
#     max = int(input("Iveskite didziausia galima skaiciu: "))
#     secret = random.randint(min, max)
#     print(f"Secret number: {secret}")
#     need_help = input("Ar norite pagalbos (t/n)? ")
#     if (need_help != 't' and need_help != 'n'):
#         continue
#     repeat_endless = input("Ar norite speti neribota sk. (t/n)? ")
#     if (repeat_endless != 't' and repeat_endless != 'n'):
#         continue
#     guess_count = 0
#     guess_count_max = 0
#     if repeat_endless == 'n':
#         guess_count_max = int(input("Iveskite, kiek spejimu leidziama: "))
#     guessed = False
#     while guessed == False and (repeat_endless == 't' or guess_count < guess_count_max):
#         guessed_number = int(input("Spekite skaiciu: "))
#         if guessed_number != secret:
#             if need_help == 't':
#                 if (guessed_number < secret):
#                     print("Iveskite didesni skaiciu")
#                 else:
#                     print("Iveskite mazesni skaiciu")
#             if repeat_endless == 'n':
#                 guess_count += 1
#         else:
#             guessed = True
#             print("Atspejote!!!")
#     finished = True
# #****************************************************************************************************
# Additional tasks:
# print("************************************")
# print("-------------3 uzd.----------------")
# limit = 25
# for i in range(limit):
#     for j in range(limit):
#         print("*", end="")
#     print()

# print("************************************")
# print("-------------4 uzd.----------------")
# count = 0
# limit = 25
# for i in range(limit):
#     for j in range(limit):
#         if count == j or (limit - 1 - count) == j:
#             print("0", end="")
#         else:
#             print("*", end="")
#     print()
#     count += 1

# print("************************************")
# print("-------------5 uzd.----------------")
# print(f"Coat of Arms = 0 (H), Number = 1 (N)")
# coat_of_arms = 0
# for i in range(20):
#     flip_coin = random.randint(0, 1)
#     print(f"{i+1}-as metimas: ", end="")
#     print("S" if flip_coin == 1 else "H")
#     if flip_coin == 0:
#         coat_of_arms += 1
#     if coat_of_arms == 3:
#         break

# coat_of_arms = 0
# previous_flip = 0
# i = 0
# while True:
#     i += 1
#     flip_coin = random.randint(0, 1)
#     print(f"{i}-as metimas: ", end="")
#     print("S" if flip_coin == 1 else "H")
#     if flip_coin == 0 and (coat_of_arms == 0 or previous_flip == 0):
#         coat_of_arms += 1
#     else:
#         coat_of_arms = 0
#     previous_flip = flip_coin
#     if coat_of_arms == 3:
#         break

# print("************************************")
# print("-------------6 uzd.----------------")
# sum_petras = 0
# sum_kazys = 0
# win_score = 222
# while True:
#     petras_score = random.randint(10, 20)
#     sum_petras += petras_score
#     kazys_score = random.randint(5, 25)
#     sum_kazys += kazys_score
#     if sum_kazys >= win_score or sum_petras >= win_score:
#         break
# print(f"Petras: {sum_petras}. Kazys: {sum_kazys}")
# print(f"Partiją laimėjo: ", end="")
# print("Kazys" if sum_kazys > sum_petras else "Petras" if sum_petras > sum_kazys else "abu")

# print("************************************")
# print("-------------7 uzd.----------------")
# limit = 21
# center = int(limit / 2) + 1
# line = ""
# for i in range(center):
#     for j in range(1, limit + 1):
#         if j == center or (j <= center + i and j >= center - i):
#             line += "*"
#         else:
#             line += " "
#     line += "\n"
# for i in range(center - 2, -1, -1):
#     for j in range(limit, 0, -1):
#         if j == center or (j <= center + i and j >= center - i):
#             line += "*"
#         else:
#             line += " "
#     line += "\n"
# print(line)

# Tomo kodas:
# print("\n--- 7 ---")
# increment = 0
# for y in range(21):
#     line=""
#     for x in range(21):
#         if 10-increment<=x and x<=10+increment:
#             line += "*"
#         else:
#             line += " "
#     increment += 1 if y<10 else -1
#     print(line)

# print("************************************")
# print("-------------8 uzd.----------------")
# nail_length = 85
# for i in range(5):
#     sum = 0
#     count = 0
#     while True:
#         sum += random.randint(5, 20)
#         count += 1
#         if sum >= nail_length:
#             break
#     print(f"{i + 1}-a vinis. Reikia smugiu: {count}. Is viso mm: {sum}")
# for i in range(5):
#     sum = 0
#     count = 0
#     while True:
#         success = random.randint(0,1) == 1
#         if success:
#             sum += random.randint(20, 30)
#         count += 1
#         if sum >= nail_length:
#             break
#     print(f"{i + 1}-a vinis. Reikia smugiu: {count}. Is viso mm: {sum}")

# print("************************************")
# print("-------------9 uzd.----------------")
# line_numbers = ""
# numbers = random.sample(range(1, 200), 50)
# print(numbers)
# for i in numbers:
#     line_numbers += str(i) + " "
# line_numbers = line_numbers[:-1]
# print(line_numbers)
#
# numbers2 = map(int, line_numbers.split())
# print(numbers2)
# prime_numbers = []
# for num in numbers2:
#     is_prime = True
#     i = 2
#     while i < num:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1
#     if is_prime:
#         prime_numbers.append(num)
#
# prime_numbers.sort()
# s = ' '.join(str(n) for n in prime_numbers)
# print(s)
