


#task1
def multiply(a, b):
    return a * b
print(multiply(2,5))

#task2
def greet(name, greeting = "Hello"):
    print(greeting + ", " + name)

greet("Nazarii")
greet("Vova", "Goodbye")

#task3
def summ(*args):
    sum_num = 0
    for num in args:
        sum_num += num
    return sum_num

print(summ(1,2,3))
print(summ(10, 20, 30, 40))

#task4
def user_info(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

user_info(name = "Vlad", age = 22, city = "Kyiv")

#task5
def show_info(title, *args, **kwargs):
    print(title)
    print(*args)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show_info("User Data", "Python","Developer", name = "Nazar", age = 22)

#task6
def filter_numbers(numbers, *args):
    return [num for num in numbers if num not in args]
print(filter_numbers([1,2,3,4,5], 2,4))

#task7
def add_users(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


add_users(Anna = 22, Ivan = 30, Maria = 25)


#task7
def stats(mode, *args):
    if mode == "sum":
        return sum(args)
    elif mode == "avg":
        return sum(args) / len(args)
    elif mode == "max":
        return max(args)

print(stats("sum", 1, 2, 3, 4, 5))
print(stats("avg", 10, 20, 30))
print(stats("max", 5, 100, 50))