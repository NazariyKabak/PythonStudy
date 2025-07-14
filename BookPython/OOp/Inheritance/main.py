from BookPython.OOp.Inheritance.Alg.task1.Poodle import Poodle
from BookPython.OOp.Inheritance.Prac.task1.productionWorker import ProductionWorker
from BookPython.OOp.Inheritance.Prac.task3.customer import Customer

# poodle_1 = Poodle("Gucci", 5, 15.6, "crop", "yes")
# print(poodle_1)

# production_worker = ProductionWorker("Nazarii", 1, 1, 4000)
# production_worker.work_shift_definition(1)

customer_1 = Customer("Nazarii", "Kyiv", "0980401397", 1, True)
print(customer_1.get_notify())
