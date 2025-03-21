
from OOP.MagicMethods.Counter import Counter
from OOP.MagicMethods.CustomDict import CustomDict
from OOP.MagicMethods.Money import Money
from OOP.MagicMethods.Multiplier import Multiplier
from OOP.MagicMethods.MyRange import MyRange
from OOP.MagicMethods.Person import Person
from OOP.MagicMethods.Product import Product
from OOP.MagicMethods.Vector import Vector
#task1,2
p = Person("Nazarii", 22)
print(p)
print(repr(p))

#task3
wallet1 = Money('100')
wallet2 = Money('400')
print(wallet1.__add__(wallet2))

#task4
c = Counter(["Alice", "Bob", "Charlie"])
print(len(c))

#task5
m = Multiplier(200)
print(m(5))
print(m.__call__(5))

#task6
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)
print(v1 - v2)
# print(v1 * v2)

#task7
pr1 = Product("Laptop", 500)
pr2 = Product("Phone", 700)
print(pr1 == pr2)
print(pr1 < pr2)

#task8
d = CustomDict()
d["name"] = "Nazarii"
print(d["name"])
print(d["age"])

#task9
for i in MyRange(1,5):
    print(i)