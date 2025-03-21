# num = 99
# num = 5
# print(num)

#task2 Прогноз продаж
# sum_num = float(input())
# profit = sum_num * 0.23
# print(f"Очікуваний прибуток: {profit:.2f}")

#task3
# square_meters = float(input())
# meters = 4046.86
# acr = square_meters / meters
# print(f"Очікуваний акр: {acr:.2f}")

#task4
# p1 = int(input("Введіть ціну 1-го товара!"))
# p2 = int(input("Введіть ціну 2-го товара!"))
# p3 = int(input("Введіть ціну 3-го товара!"))
# p4 = int(input("Введіть ціну 4-го товара!"))
# p5 = int(input("Введіть ціну 5-го товара!"))
#
# sum_price = (p1 + p2 + p3 + p4 + p5)
# tax = sum_price * 0.07
# total_price = sum_price + tax
# print(f"Сума товарів - {sum_price}, загальна сума -  {total_price}")

#task5

# time = int(input("Enter the time"))
# speed = 70
# distance = time * speed
# print(distance)

#task6

# purchase_amount = float(input("Enter purchase amount: "))
# federal_tax = purchase_amount * 0.05
# regional_tax = purchase_amount * 0.025
# total_tax = federal_tax + regional_tax
# total = purchase_amount + federal_tax + regional_tax
#print(f"Федеральний податок: {federal_tax:.2f} грн")
# print(f"Регіональний податок: {regional_tax:.2f} грн")
# print(f"Загальний податок: {total_tax:.2f} грн")
# print(f"Сума до сплати: {total:.2f} грн")

#task7
# km_traveled = float(input("Enter km traveled: "))
# gasoline_consumption_in_liters = float(input("Enter gasoline consumption in liters: "))
# consumption = km_traveled/gasoline_consumption_in_liters
# print(f"Витрата: {consumption:.2f} км/л")

#task8
cost_food = float(input("Enter the cost of food: "))
tips = cost_food * 0.18
tax = cost_food * 0.07
print(f"Сума їжі: {cost_food:.2f} грн")
print(f"Чайові (18%): {tips:.2f} грн")
print(f"Податок (7%): {tax:.2f} грн")
print(f"Загальна сума: {cost_food + tax + tips:.2f} грн")

#task9
temp_Celsius = float(input("Enter the temperature in Celsius: "))
farenheit = 9/5 * temp_Celsius + 32
print(f"{temp_Celsius}°C = {farenheit:.2f}°F")

#task10
count_cake = int(input("Enter the number of cakes: "))
sugar = (1.5 * count_cake)/48
butter = (1 * count_cake)/48
flour = (2.75 * count_cake)/48
print(f"На {count_cake} булочок потрібно:")
print(f"Цукор: {sugar:.2f} склянки")
print(f"Масло: {butter:.2f} склянки")
print(f"Борошно: {flour:.2f} склянки")

#task11
man_student = int(input("Enter the number of students: "))
woman_student = int(input("Enter the number of students: "))
register_in_group = int(input("Enter the number of registers in group: "))
percentage_of_students_man = man_student/(man_student + woman_student)
percentage_of_students_woman = woman_student/(man_student + woman_student)
print(f"Чоловіки: {percentage_of_students_man * 100:.1f}%")
print(f"Жінки: {percentage_of_students_woman * 100:.1f}%")

#task12
action = 2000
price_one_action = 40.00
commission = 0.03
sum_by = action*price_one_action*commission
print(sum_by)

action_selling = 2000
price_one_action_selling = 42.75
sum_selling = action_selling * price_one_action_selling*commission
print(sum_selling)

div = sum_selling - sum_by
print(div)

profit = (action_selling * price_one_action_selling) - (action * price_one_action)
broker_fees = (action + action_selling) * price_one_action * commission
net_profit = profit - broker_fees
print(f"Прибуток: {profit:.2f} USD")
print(f"Комісія брокера: {broker_fees:.2f} USD")
print(f"Чистий прибуток: {net_profit:.2f} USD")
