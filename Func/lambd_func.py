#task1
from functools import reduce

square = lambda x: x * x
print(square(5))
print(square(8))
#task2
sum_nums = lambda x, y: x + y
print(sum_nums(2, 3))
#task3
isEven = lambda num: num % 2 == 0
print(isEven(6))
#task4
length = lambda s: len(s)
print(length("abc"))

#task5
words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)

#task6
starts_with_P = lambda s: s.startswith("P")
print(starts_with_P("Python"))  # Очікуваний результат: True
print(starts_with_P("Java"))

#task7
numbers = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)

#task8
numbers2 = [10, 15, 20, 25, 30, 35]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers2))
print(even_numbers)

#task9
numbers3 = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers3)
print(product)

#task10
words2 = ["apple", "banana", "avocado", "cherry", "apricot"]
filtered_words = list(filter(lambda word: word.startswith("a"), words2))
print(filtered_words)

