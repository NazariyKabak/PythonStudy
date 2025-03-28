# #task1
# product = 0
# while product < 100:
#     num = float(input("Enter number: "))
#     result = num * 10
#     product += result
#     # print(product)
#
# print(product)
#
#
# #task2
# total = 0
# choose_op = "yes"
# while choose_op == "yes":
#     num1 = int(input("Enter number1: "))
#     num2 = int(input("Enter number2': "))
#     total = num2 + num1
#     print(total)
#     choose_op = input("Do you want to continue? (yes/no): ")

#task3
# for i in range(0, 1001, 10):
#     print(i)

#task4
# total = 0
# for i in range(10):
#     number = int(input("Enter a number: "))
#     total += number
# print(total)

#task5
# total = 0
# num = 30
# for i in range(1, 31):
#     total += i/num
#     num -= 1
# print(total)

#task7
# for row in range(10):
#     for col in range(15):
#         print("#", end=" ")
#     print()

#task8
# num = int(input("Enter a number: "))
# while num < 0:
#     print("Dont 0. Enter a number: ")
#     num = int(input())
# print("Nice!")

#task9

# num = int(input("Enter a number from 1 to 100: "))
# while num < 1 or num > 100:
#     num = int(input("Invalid! Enter a number from 1 to 100: "))
# print("Nice!")


#task1

# total_err = 0
# for i in range(1,6):
    # err = int(input("Enter count err: "))
#     total_err += err
# print(total_err)
#task2
# KAL_IN_MIN = 4.2
# kak = 1
# for i in range(10, 31, 10):
#     kal = i * KAL_IN_MIN
#     print(f"{i} - min = {kal}")

#task3

# budget = int(input("Enter a sum: "))
# total = 0
# n = int(input("Скільки у вас категорій витрат? "))
# for i in range(n):
#     amount = float(input(f"Введіть витрати {i+1}-ї категорії: "))
#     total += amount
#     print(f"Накопичувальна сума витрат: {total:.2f} грн")
#
# if total <= budget:
#     saved = budget - total
#     print(f"Ви зекономили {saved:.2f} грн")
# else:
#     overspent = total - budget
#     print(f"Ви перевитратили {overspent:.2f} грн")


#task4
# speed_in_hour = int(input('Enter speed: '))
# count_hour = int(input('Enter count: '))
# distance_traveled = 1
# for i in range(1, count_hour + 1):
#     distance_traveled = i * speed_in_hour
#     print(distance_traveled)

#task5
# count_year = int(input('Enter year: '))
# total_millimeters_of_rainfall = 0
# count_months = 0
# for year in range(1, count_year + 1):
#     for month in range(1, 13):
#         millimeters_of_rainfall = float(input('Enter millimeters of rainfall: '))
#         total_millimeters_of_rainfall += millimeters_of_rainfall
#         count_months += 1
#
# avg = total_millimeters_of_rainfall / count_months
#
# print(total_millimeters_of_rainfall, count_months, avg)

#task6
# for temperature in range(0, 21):
#     farenheit = (9/5) * temperature + 32
#     print(f"{temperature} = {farenheit}")
# print()

#task7
# count_day = int(input('Enter number of days: '))
# salary_per_day = 0.01
# total_salary = 0
# print("\nDay\tSalary (Грн)")
# print("-" * 20)
# for i in range(1, count_day + 1):
#     print(f"{i}\t{salary_per_day:.2f}")
#     # salary = i * salary_per_day
#     total_salary += salary_per_day
#     salary_per_day *= 2
#     # print(f"day {i} = {salary}")
# print("-" * 20)
# print(f"Total salary: {total_salary:.2f} ГРН.")

#task8
# total_num = 0
# num = int(input('Enter number: '))
# while num > 0:
#     total_num += num
#     num = int(input('Enter number: '))
# print(total_num)

#task9
# LEVEL_OCEAN = 1.6
# for year in range(1, 26):
#     print(year*LEVEL_OCEAN)

#task10
# TUITION_FEES = 145000
# year = TUITION_FEES+TUITION_FEES
# for i in range(1, 6):
#     print(f"{i} рік: {year:.2f} грн.")
#     year += year * 0.03

#task11
# initial_mass = float(input('Enter initial mass: '))
# for month in range(1, 7):
#     print(f'{month}: {initial_mass} kg')
#     initial_mass -= 1.5


#task12
# n = int(input('Enter number: '))
# result = 1
# for i in range(1, n+1):
#     result *= i
# print(result)

#task13
# starting_count_oranisms = int(input('Enter starting count: '))
# average_daily_increase = float(input('Enter average daily increase: '))
# count_day_for_reproduction = int(input('Enter count of day for reproduction: '))
# for i in range(1, count_day_for_reproduction + 1):
#     print(f"{i} = {starting_count_oranisms}")
#     starting_count_oranisms += starting_count_oranisms * average_daily_increase


#task14
for rows in range(7, 0, -1):
    for cols in range(rows):
        print('*', end='')
    print()