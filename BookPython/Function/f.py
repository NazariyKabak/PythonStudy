import math
import random


#     # x = 1
#     # y = 3.4
#     # print(x, y)
#     # change_us(x, y)
#     # print(x, y)
#     print(convert_to_km(10))
#
#
# #task1
# def times_ten(n):
#     return n * 10
#
#
# #task2
# def show_value(quantity):
#     print(quantity)
#
#
# # show_value(12)
#
#
# #task3
#
# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
#
#
# #task1
# def convert_to_km(n):
#     return n * 0.6
#
#
# #task2
# def purchase_amount():
#     n = float(input("Enter the purchase amount: "))
#     return n
#
#
# def federal_tax():
#     return purchase_amount() * 0.05
#
#
# def regional_tax():
#     return purchase_amount() * 0.025
#
#
# def total_tax():
#     f_tax = federal_tax()
#     r_tax = regional_tax()
#     return f_tax + r_tax
#
#
# def total():
#     amount = purchase_amount()
#     f_tax = federal_tax()
#     r_tax = regional_tax()
#     return amount + f_tax + r_tax
#
#
# def print_t():
#     print(f"Федеральний податок: {federal_tax:.2f} грн")
#     print(f"Регіональний податок: {regional_tax:.2f} грн")
#     print(f"Загальний податок: {total_tax:.2f} грн")
#     print(f"Сума до сплати: {total:.2f} грн")
#
#
# main()
#
#
# #task3
# def cost_of_insurance():
#     cost_building = float(input("Enter the cost of building: "))
#     return cost_building * 0.8
#
#
# #task4
# def car_expenses():
#     credit_payment = float(input("Enter the credit payment: "))
#     insurance = float(input("Enter the insurance: "))
#     gasoline = float(input("Enter the gas line: "))
#     tyre = float(input("Enter the tyre: "))
#     car_butter = float(input("Enter the car butter: "))
#     maintenance = float(input("Enter the maintenance: "))
#     monthly_expenses = car_butter + insurance + gasoline + tyre + maintenance + credit_payment
#     yearly_expenses = monthly_expenses * 12
#     return monthly_expenses, yearly_expenses
#
#
# #task5
# def property_tax():
#     price = float(input("Enter the price of property: "))
#     estimated_variety = price * 0.60
#     tax = estimated_variety / 100 * 0.72
#     return estimated_variety, tax
#
#
# #task6
# def task6():
#     count_grams_fat = float(input("Enter a grams fat"))
#     count_grams_carbohydrates = float(input("Enter a grams calories"))
#     calories_fat = count_grams_fat * 9
#     calories_carbohydrates = count_grams_carbohydrates * 4
#     return calories_fat, calories_carbohydrates
#
#
# #task7
# def stadium_seats():
#     count_A_tickets = int(input("Enter the number of tickets"))
#     count_B_tickets = int(input("Enter the number of tickets"))
#     count_C_tickets = int(input("Enter the number of tickets"))
#
#     sum_A = count_A_tickets * 20
#     sum_B = count_B_tickets * 15
#     sum_C = count_C_tickets * 10
#     total = sum_A + sum_B + sum_C
#     return total
#
#
# #task8
# def task8():
#     total = task8_6() + task8_5()
#     return total
#
#
# def task8_1():
#     area = float(input("Enter the area: "))
#
#     return area
#
#
# def task8_2():
#     price_5_l = float(input("Enter the price: "))
#     return price_5_l
#
#
# def task8_3():
#     count_of_cans = task8_1() / 10
#     return count_of_cans
#
#
# def task8_4():
#     hour = (task8_1() / 10) * 8
#     return hour
#
#
# def task8_5():
#     price_paint = task8_3() * task8_2()
#     return price_paint
#
#
# def task8_6():
#     price_work = task8_4() * 2000
#     return price_work
#
#
# #task9
# def input_monthly_sales():
#     monthly_sales = float(input("Enter the monthly sales: "))
#     return monthly_sales
#
#
# def sum_tax_municipal():
#     monthly_sales = input_monthly_sales()
#     return monthly_sales * 0.025
#
#
# def sum_tax_federal():
#     monthly_sales = input_monthly_sales()
#     return monthly_sales * 0.5
#
#
# def total_tax():
#     tax = sum_tax_municipal() + sum_tax_federal()
#     return tax
#
#
# #task10
# def feet_to_inches(feet):
#     return feet * 12


#task11
# def random_num1():
#     random_num = random.randint(1, 100)
#     return random_num
#
#
# def random_num2():
#     random_num = random.randint(1, 100)
#     return random_num
#
#
# def sum_random_nums():
#     random_n1 = random_num1()
#     random_n2 = random_num2()
#     return random_n1 + random_n2
#
#
# def check_sum():
#     answer = int(input("Enter the sum of two numbers: "))
#     if answer == sum_random_nums():
#         print("Correct")
#     else:
#         print("Incorrect")


#task12
# def input_num1():
#     num1 = int(input("Enter the first number: "))
#     return num1
#
#
# def input_num2():
#     num2 = int(input("Enter the second number: "))
#     return num2
#
#
# num1 = input_num1()
# num2 = input_num2()
#
#
# def max_num(num1, num2):
#     if num1 > num2:
#         return num1
#     elif num1 < num2:
#         return num2
#     else:
#         return num1
#
#
# print(max_num(num1, num2))


#task13
# def falling_distance(t):
#     d = (1 / 2) * 9.8 * t ** 2
#     return d
#
#
# for t in range(1, 11):
#     print(falling_distance(t))


#task14
# value_mass = float(input("Enter the mass: "))
# value_speed = float(input("Enter the speed: "))
#
#
# def kinetic_energy(value_mass, value_speed):
#     return (1 / 2) * value_mass * value_speed ** 2


#task15
# mark_1 = int(input("Enter the mark of first: "))
# mark_2 = int(input("Enter the mark of second: "))
# mark_3 = int(input("Enter the mark of third: "))
# mark_4 = int(input("Enter the mark of fourth: "))
# mark_5 = int(input("Enter the mark of fifth: "))
#
#
# def calc_avg(mark_1, mark_2, mark_3, mark_4, mark_5):
#     avg = (mark_1 + mark_2 + mark_3 + mark_4 + mark_5) / 5
#     return avg
#
#
# avg = calc_avg(mark_1, mark_2, mark_3, mark_4, mark_5)
#
#
# def determinate_grade(avg):
#     if avg >= 90:
#         print("A")
#     elif avg >= 80:
#         print("B")
#     elif avg >= 70:
#         print("C")
#     elif avg >= 60:
#         print("D")
#     else:
#         print("F")


#task16
# def count_even_odd_num():
#     count_even = 0
#     count_odd = 0
#     for _ in range(100):
#         random = random_num1()
#         if random % 2 == 0:
#             count_even += 1
#         else:
#             count_odd += 1
#     return count_even, count_odd


#task17
# def is_prime(n):
#     is_Prime = True
#     if n < 2:
#         return False
#     else:
#         for i in range(2, int(math.sqrt(n)) + 1):
#             if n % i == 0:
#                 is_Prime = False
#                 break
#     return is_Prime


#task18
# for i in range(100):
#     print(is_prime(i))

#task20
# random_num = random.randint(1, 100)
# attempt = int(input("Enter a number between 1 and 10: "))
# count_attempt = 0
# while attempt != random_num:
#     if attempt > random_num:
#         print("Більше заданого числа, спробуйте ще раз!")
#     elif attempt < random_num:
#         print("Менше заданого числа, спробуйте ще раз!")
#     attempt = int(input("Enter a number between 1 and 10: "))
#     count_attempt += 1
# print("You got it!")

#task21
def random_num():
    random_n = random.randint(1, 3)
    return random_n


def check_pc_choice():
    random_n = random_num()
    if random_n == 1:
        return "stone"
    elif random_n == 2:
        return "scissors"
    elif random_n == 3:
        return "paper"


def choice_player():
    choice = input("Enter your choice: ")
    return choice


def main():
    choice_pc = check_pc_choice()
    choice_play = choice_player()
    print(choice_play, choice_pc)
    while choice_pc == choice_play:
        choice_pc = check_pc_choice()
        choice_play = choice_player()
    if choice_pc == "stone" and choice_play == "scissors":
        print("PC win!")
    elif choice_pc == "paper" and choice_play == "stone":
        print("PC win!")
    elif choice_pc == "scissors" and choice_play == "paper":
        print("PC win!")
    elif choice_pc == "paper" and choice_play == "scissors":
        print("You win!")
    elif choice_pc == "scissors" and choice_play == "stone":
        print("YOU win!")
    elif choice_pc == "stone" and choice_play == "paper":
        print("You win!")