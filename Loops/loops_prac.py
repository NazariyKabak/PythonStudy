import math
import random


#task1
def loops_num(n):
    for i in range(1, n + 1):
        if i % 3 != 0:
            print(i)


# loops_num(100)

#task2 Порахувати суму парних чисел від 1 до n

def sum_nums(n):
    sum_n = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum_n += i
    return sum_n


# print(sum_nums(10))

#task3 Перевернути число (наприклад, 1234 → 4321)
def revers_num(n):
    reversed_n = ""
    while n > 0:
        reversed_n += str(n % 10)
        n //= 10
    return reversed_n


# print(revers_num(1234))

#task4 Перебрати рядок і вивести кожен символ у новому рядку
def print_char(s):
    for c in s:
        print(c)


# print_char("hello")

#task5 Вивести всі числа Фібоначчі, що не перевищують n
def fibonacci(n):
    n1 = 0
    n2 = 1
    next = n1 + n2
    while next < n:
        n1 = n2
        n2 = next
        next = n1 + n2
    return next


# print(fibonacci(10))

#task6 Перевірити, чи число є простим
def check_is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
                break
    return True


# print(check_is_prime(6))
# print(check_is_prime(7))
# print(check_is_prime(8))


#task7 Знайти всі дільники числа n
def dividers(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return sorted(divisors)


# print(dividers(6))

#task8 Вивести таблицю множення (1-10) для числа n
def table_mult(n):
    for i in range(1, 10 + 1):
        print(i * n)


# table_mult(6)

#task9 Знайти факторіал числа без використання math.factorial()

def search_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# print(search_factorial(5))

#task10
def calc(a, b, operation):
    while True:
        match operation:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                if b == 0:
                    return "Помилка: Ділення на нуль!"
                return a / b
            case "exit":
                return "Калькулятор завершив роботу."
            case _:
                return "Невідома операція. Введіть +, -, *, / або 'exit'."


#task11 Вивести всі числа Амстронга у діапазоні
def nums_armstrong(lower, upper):
    for n in range(lower, upper + 1):
        sum_num = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            sum_num += digit ** 3
            temp //= 10
        if sum_num == n:
            print(n)


# nums_armstrong(1, 100)
# nums_armstrong(100, 1000)
# nums_armstrong(1000, 10000)

#task12 Перевірити, чи можна отримати число n як суму двох простих чисел


def check_prime_sum(n):
    for a in range(2, n // 2 + 1):
        b = n - a
        if check_is_prime(b) and check_is_prime(a):
            return True
    return False


# Перевірка
# print(check_prime_sum(10))
# print(check_prime_sum(11))
# print(check_prime_sum(16))
# print(check_prime_sum(20))

#task13 Знайти n-те просте число

def find_nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if check_is_prime(num):
            count += 1
    return num


# print(find_nth_prime(10))


#task14 Гра "Вгадай число" з підказками ("більше/менше")

def guess_the_number():
    random_number = random.randint(1, 100)

    while True:
        n = int(input("Enter a number between 1 and 100: "))
        if n > 100 or n < 1:
            print("Число має бути в діапазоні від 1 до 100!")
            continue
        if random_number == n:
            print("You guessed the number!")
            break
        elif n < random_number:
            print("Більше")
        elif n > random_number:
            print("Менше")


# guess_the_number()


#task15
def int_to_roman(n):
    roman_numerals = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV",
        1: "I"
    }

    roman_str = ""

    for value, symbol in roman_numerals.items():
        while n >= value:
            roman_str += symbol
            n -= value
    return roman_str


print(int_to_roman(5))
