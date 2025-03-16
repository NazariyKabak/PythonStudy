from OOP.Basic.BankAccount import BankAccount
from OOP.Basic.Car import Car
from OOP.Basic.Cat import Cat
from OOP.Basic.Dog import Dog
from OOP.Basic.MathUtils import MathUtils
from OOP.Basic.Person import Person
from OOP.Basic.Student import Student

#task 1,2,3

p1 = Person('John', 20)

print(p1.name, p1.age)
print(p1.greet())
print(p1.species)

#task4
car1 = Car('Volkswagen', "Passat", 1999)
car1.display_info()

#task5
account1 = BankAccount(1000)
print(account1.get_balance())
account1.deposit(500)
account1.withdraw(200)
print(account1.get_balance())

#task6
print(Student.get_school_name())

#task7
print(MathUtils.add(3,5))

#task8
cat = Cat()
print(cat.speak())
dog = Dog()
print(dog.speak())