import math
import random
from math import factorial
from string import digits

##task1
# for i in range(1,10+1):
#     print(i)
##2
# for i in range(2,20+1):
#     if i%2==0:
#         print(i)

# x=2
# while x<=10:
#     if x%2==0:
#         print(x)
#     x=x+1

#task3
# for x in range(1,6):
#     print(x**2)
#
# #task4
# num1 = int(input("Enter a number: "))
#
# for x in range(1,11):
#     result = num1 * x
#     print(f"{x}","* " f'{num1}', "=",result)

##task5
# x = int(input("Enter a number: "))
# sum_x = 0
# for i in range(x+1):
#     sum_x = sum_x + i
#
# print("The sum of {} is {}".format(i, sum_x))

#task6
n = int(input("Enter a number: "))
isPrime = True
if n<2:
    isPrime = False
else:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            isPrime = False
            break
print("Prime" if isPrime else "Not prime")

#task7
# random_num = random.randint(1, 10)
# attempt = int(input("Enter a number between 1 and 10: "))
# while attempt!=random_num:
#     attempt = int(input("Enter a number between 1 and 10: "))
#
# print("You got it!")

#task8

# for i in range(n,0,-1):
#     print("*" * i)
#
# while n>0:
#     print("*" * n)
#     n -= 1


#task9
# num_max = 0
# while n>0:
#     digit = n % 10
#     print("Digit: " f"{digit}")
#     if digit>num_max:
#         num_max = digit
#     n //= 10
# print("The number is max =", num_max)

#task10
# n1=0
# n2=1
# next_n = n1 + n2
# print(n1, n2, end=" ")
# for i in range(2,n):
#     next_n = n1 + n2
#     print(next_n)
#     n1 = n2
#     n2 = next_n
#


#task11
count = 0
# while n>0:
#     digits = n%10
#     n //= 10
#     count += 1
# print(count)

# str_num = str(n)
# for num in str_num:
#     count+=1
# print(count)

#task12
factorial_n = 1
for i in range(1,n+1):
    factorial_n = factorial_n * i
print(factorial_n)