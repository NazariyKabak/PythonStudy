#task1
import math

from OOP.Exception.NegativeNumError import NegativeNumError


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ділення на 0 неможливе!"


print(divide(1, 0))

#task2
def int_to_str(n):
    try:
        return int(n)
    except ValueError:
        return "You need to enter a number."

print(int_to_str(232))

#task4
def index_er(arr, index):
    try:
        return arr[index]
    except IndexError:
        return "Невірний індекс"


print(index_er([1, 2, 3], 4))

#task5
def check_key(dict_1, key):
    try:
        return dict_1[key]
    except KeyError:
        return "Ключа немає!"


#task6
def sqrt_number(n):
    if n < 0:
        raise ValueError
    return  math.sqrt(n)

#task7
def calc(a,b,operation):
    while True:
        try:
            if operation == "exit":
                break
            match operation:
                case "+":
                    print(a + b)
                case "-":
                    print(a - b)
                case "*":
                    print(a * b)
                case "/":
                    if b == 0:
                        raise ZeroDivisionError("Ділення на 0 неможливе!")
                    print(a / b)
                case _:
                    print("❌ Невідома операція!")
        except ValueError:
            print("❌ Введіть коректні числа!")



#task8
def read_number():
    while True:
        try:
            n = int(input())
            return n
        except ValueError:
            print("Помилка! Введіть число, а не текст.")


#task10

def sqrt(n):
    if n <= 0:
        raise NegativeNumError(n)
    return n ** 0.5

try:
    print(sqrt(-9))
except NegativeNumError as e:
    print(e)


#task11
year = int(input())
if 120 < year < 0:
    raise ValueError
else:
    print(year)


