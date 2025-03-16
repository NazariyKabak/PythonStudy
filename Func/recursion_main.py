# def countdown(n):
#     if n == 0:
#         print("Start!")
#         return
#     print(n)
#     countdown(n - 1)
#
# countdown(10)
#
#
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(6))
#
# def reverse_string(s):
#     if len(s) == 0:
#         return ""
#     return s[-1]+reverse_string(s[:-1])
# print(reverse_string("hello"))


#task1
def countdown(n):
    if n == 0:
        print("Start!")
        return
    print(n)
    countdown(n - 1)
countdown(10)

#task2
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(7))

#task3
def reverse_str(s):
    if len(s) == 0:
        return ""
    return  s[-1]+reverse_str(s[:-1])
print(reverse_str("apple"))

#task4
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(7))

#task5
def sum_digits(n):
    if n == 0:
        return 0
    return (n%10) + sum_digits(n//10)
print(sum_digits(1234))

#task6
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)
print(power(2, 3))

#task7
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("level"))
print(is_palindrome("hello"))

#task8
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(48, 18))

#task9