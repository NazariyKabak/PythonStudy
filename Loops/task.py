#task1
from Loops.loops_prac import check_is_prime


def nums_armstrong(lower, upper):
    for num in range(lower, upper + 1):
        sum_armstrong = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum_armstrong += digit ** 3
            temp = temp // 10
        if sum_armstrong == num:
            print(num)


#task2
def check_prime_sum(n):
    for a in range(2, n // 2 + 1):
        b = n - a
        if check_is_prime(a) and check_is_prime(b):
            return True
    return False


#task3
def search_count_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if check_is_prime(num):
            count += 1
    return num


#task4
def arab_to_roman(n):
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
