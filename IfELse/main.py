import random
##task1
# x = int(input("Enter a number: "))
#
# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#
# ##task2
# x2 = int(input("Enter a number: "))
# if x2<0:
#     print("Negative")
# elif x2==0:
#     print("Zero")
# else:
#     print("Plus")


##task3
# password = input("Enter a password: ")
#
# if password == "secret123":
#     print("Correct Password")
# else: print("Incorrect Password")
#
# ##task4
# nums1 = int(input("Enter a number: "))
# nums2 = int(input("Enter a number: "))
# operation = input("Enter a operation: ")
#
# match operation:
#     case "+" :
#         print(nums1 + nums2)
#     case "*" :
#         print(nums1 * nums2)
#     case "/":
#         print(nums1 / nums2)
#     case "%":
#         print(nums1 % nums2)
#     case "**":
#         print(nums1**nums2)
#     case "-":
#         print(nums1 - nums2)
#
#
# ##task5
# z1 = int(input("Enter a number: "))
# z2 = int(input("Enter a number: "))
# z3 = int(input("Enter a number: "))
#
# if z1 > z2 and z1 > z3:
#     print(z1)
# elif z2 > z3 and z2 > z1:
#     print(z2)
# elif z3 > z1 and z3 > z2:
#     print(z3)

##task6
# login = input("Enter a login: ")
# password = input("Enter a password: ")
#
# if login != "admin" and password != "12345":
#     print("Wrong Login and Wrong Password")
# elif login =="admin" and password == "12345":
#     print("Login Successful")
#
#
# ##task7
# x3 = int(input("Enter a number: "))
# x4 = int(input("Enter a number: "))
#
# if x4%x3 == 0:
#     print(x3," є дільником ",x4)
# else:
#     print(x3, " не є дільником ", x4)


##task8
# age = int(input("Enter your age: "))
#
# if 0>age<12:
#     print("Дитина")
# elif 12<age<18:
#     print("Підліток")
# elif 18<age<59:
#     print("Дорослий")
# elif age>60:
#     print("Пенсіонер")
# elif age<=0:
#     print("Менше нуля або нуль не може бути")
#
# ##task9
# day_week = input("Enter your day week: ")
#
# match day_week:
#     case "Monday":
#         print("Work day")
#     case "Tuesday":
#         print("Work day")
#     case "Wednesday":
#         print("Work day")
#     case "Thursday":
#         print("Work day")
#     case "Friday":
#         print("Work day")
#     case "Saturday":
#         print("Weekend day")
#     case "Sunday":
#         print("Weekend day")

##task10
# year = int(input("Enter your year: "))
#
# if year%4==0 and year%100!=0 or year%400==0:
#     print("Yes")
# else:
#     print("No")

# task11
# name = input("Enter your name: ")
# year = int(input("Enter your year: "))
#
# login = name[0] + f".{year}"
# print(login)

#task12
grade = int(input("Enter your grade: "))
if 90 <= grade <= 100:
    print("Відмінно")
elif 75 <= grade <= 89:
    print("Добре")
elif 60 <= grade <= 74:
    print("Задовільно")
else:
    print("Незадовільно")

#task12
currency = input("Enter your currency: ")
money_sum = int(input("Enter your sum: "))
if currency == "USD":
    print(money_sum * 42)
elif currency == "EUR":
    print(money_sum * 45)

#task13

random_number = random.randint(1, 100)

attempt = int(input("Enter your attempt: "))
if attempt == random_number:
    print("You got it!")
else:
    print("Sorry, that's wrong.")



