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