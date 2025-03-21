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

# start = int(input("Enter a num: "))
# end = int(input("Enter a num: "))
# while start < 1 and end > 100:
#     start = int(input("Enter a num: "))
#     end = int(input("Enter a num: "))
# print("Nice!")



#task1
# err = int(input("Enter count err: "))
# total_err = 0
# for i in range(1,6):
#     total_err += err
# print(total_err)
#task2
# KAL_IN_MIN = 4.2
# kak = 1
# for i in range(10, 31, 10):
#     kal = i * KAL_IN_MIN
#     print(f"{i} - min = {kal}")

#task3
sum_in_months = int(input("Enter a sum: "))
total = 0
while True:
    