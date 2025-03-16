import math
import random
from my_utils import greet, square, is_even
import datetime
from calculator import add, subtract, multiply, divide
from password_generator import random_password
#task1
print(math.sqrt(64))
print(math.factorial(7))
print(f'{math.pi}')

#task2
random_num = random.randint(1, 100)
print(random_num)
fruit = ['apple', 'banana', 'orange']
print(random.choice(fruit))
nums = [1, 2, 3,4,5]
random.shuffle(nums)
print(nums)


#task3
print(square(3))
print(is_even(3))
print(greet("Nazarii"))

#task4
print(datetime.datetime.today())
print(datetime.date.today())
print(datetime.date.today() + datetime.timedelta(days=7))

#task5

print(add(2,3))
print(subtract(2,3))
print(multiply(2,3))
print(divide(2,3))

#task6


#task8
print(random_password())
