# #task1
# day_week = int(input('Enter day of week: '))
# if day_week == 1:
#     print('Monday')
# elif day_week == 2:
#     print('Tuesday')
# elif day_week == 3:
#     print('Wednesday')
# elif day_week == 4:
#     print('Thursday')
# elif day_week == 5:
#     print('Friday')
# elif day_week == 6:
#     print('Saturday')
# elif day_week == 7:
#     print('Sunday')
# else:
#     print('Invalid input')
#
# #task2
# length1 = float(input('Enter length of item: '))
# length2 = float(input('Enter length of item: '))
# width1 = float(input('Enter width of item: '))
# width2 = float(input('Enter width of item: '))
# area1 = length1 * width1
# area2 = length2 * width2
# if area1 > area2:
#     print("Triangle1 > Triangle2")
# elif area2 > area1:
#     print("Triangle2 > Triangle1")
# else:
#     print("Triangle1 == Triangle2")
#
# #task3
# person_age = int(input('Enter person age: '))
# if person_age < 0:
#     print("Invalid age")
# elif person_age == 1 or person_age == 0:
#     print("Baby")
# elif 1 < person_age < 13:
#     print("Child")
# elif 13 <= person_age < 20:
#     print("teenager")
# elif person_age >= 20:
#     print("adult")
#
# #task4
# num = int(input('Enter a number 1 - 10: '))
# if num == 1:
#     print('I')
# elif num == 2:
#     print('II')
# elif num == 3:
#     print('III')
# elif num == 4:
#     print('IV')
# elif num == 5:
#     print('V')
# elif num == 6:
#     print('VI')
# elif num == 7:
#     print('VII')
# elif num == 8:
#     print('VIII')
# elif num == 9:
#     print('IX')
# elif num == 10:
#     print('X')
# else:
#     print('Invalid input')
#
# #task5
# body_weight = float(input("Enter body weight: "))
# heft = body_weight * 9.8
# if heft > 500:
#     print("Тіло занадто тяжке")
# elif heft < 100:
#     print("Тіло занадто легке")
#
# #task6
# month = int(input('Enter month: '))
# day = int(input('Enter day: '))
# year = int(input('Enter year: '))
# product = month * day
# if product == year:
#     print("Magic data!")
# else:
#     print("Dont magic data!")
#
# #task7
# color1 = input("Enter color1: ")
# color2 = input("Enter color2: ")
# if color1 == "синій" and color2 == "червоний":
#     print("Фіолетовий")
# elif color1 == "червоний" and color2 == "синій":
#     print("Фіолетовий")
# elif (color1 == "червоний" or color1 == "жовтий") and (color2 == "червоний" or color2 == "жовтий"):
#     print("Оранжовий")
# elif (color1 == "синій" or color1 ==  "жовтий") and (color2 == "синій" or color2 ==  "жовтий")
#     print("Зелений")
# else:
#     print("Incorrect input")
#
# #task8
# picnic_participants = int(input("Enter number of picnic: "))
# count_hot_dogs = int(input("Enter count of hot dogs: "))
# Serious_quantity_of_hot_dogs = picnic_participants * count_hot_dogs
# Minimum_quantity_of_sausage_packages = (picnic_participants * count_hot_dogs)/10
# Minimum_quantity_of_bun_packages = (picnic_participants * count_hot_dogs)/8
# Surplus_bun = (Minimum_quantity_of_bun_packages * 8) - (picnic_participants * count_hot_dogs)
# Surplus_sausage = (Minimum_quantity_of_sausage_packages * 10) - (picnic_participants * count_hot_dogs)
#
# #task9
# pocket_number = int(input("Enter pocket 0 - 36 number : "))
# if pocket_number == 0:
#     print("Green")
# elif 1 <= pocket_number <= 10:
#     if pocket_number % 2 == 0:
#         print("Black")
#     else:
#         print("Red")
# elif 11 <= pocket_number <= 18:
#     if pocket_number % 2 == 0:
#         print("Red")
#     else:
#         print("Black")
# elif 19 <= pocket_number <= 28:
#     if pocket_number % 2 == 0:
#         print("Black")
#     else:
#         print("Red")
# elif 29 <= pocket_number <= 36:
#     if pocket_number % 2 == 0:
#         print("Red")
#     else:
#         print("Black")
# else:
#     print("Incorrect input")
#
# #task10
# count_coins = int(input("Enter count of coins: "))
# count_dollar = count_coins / 100
# if count_dollar == 1:
#     print("You win")
# else:
#     print("You lose")
#
# #task11
# count_book_by = int(input("Enter count of book by: "))
# two_books_point = 5
# one_books_point = two_books_point /2
# point = one_books_point * count_book_by
# if count_book_by == 0:
#     print("0 point")
# elif count_book_by == 1:
#     print(point)
# elif count_book_by == 2:
#     print(point)
# elif count_book_by == 4:
#     print("15 point")
# elif count_book_by == 5:
#     print(point)
# elif count_book_by == 6:
#     print("30 point")
# elif count_book_by == 7:
#     print(point)
# elif count_book_by >= 8 :
#     print("60 point")
#
# #task12
# RETAIL = 99
# count_pack = int(input("Enter count of pack: "))
# sum_serious = 0
# if 10 <= count_pack <= 19:
#     sum_serious += RETAIL*0.10
# elif 20 <= count_pack <= 49:
#     sum_serious += RETAIL*0.20
# elif 50 <= count_pack <= 99:
#     sum_serious += RETAIL*0.30
# elif 100 <= count_pack:
#     sum_serious += RETAIL*0.40
#
# print(sum_serious)
#
#task13
# weight = int(input("Enter weight of pack: "))
# bid = 1
# if weight <= 200:
#     bid = (weight * 150)/100
#     print(bid)
# elif 200 < weight < 600:
#     bid = (weight * 300)/100
#     print(bid)
# elif 600 <= weight < 1000:
#     bid = (weight * 400)/100
#     print(bid)
# elif 1000 <= weight:
#     bid = (weight * 475)/100
#     print(bid)

#task14
weight = float(input('Enter weight: '))
height = float(input('Enter height: '))
bmi = weight / (height ** 2)
if 18.5 <= bmi <= 25:
    print('BMI =', bmi, "Оптимально")
elif bmi < 18.5:
    print('BMI below 18.5', "вес ниже норми")
elif bmi >= 25:
    print(bmi, "вес више норми")

#task15
