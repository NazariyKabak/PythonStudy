from task1 import Pet
from task2.car import Car
from task3.information import Information
from task4.employee import Employee
from task5.retail_item import RetailItem


def main():
    retail_item1 = RetailItem("Піджак", 12, 59.95)
    retail_item2 = RetailItem("Дизайнерські джинси", 40, 34.95)
    retail_item3 = RetailItem("Рубашка", 20, 24.95)
    product = [retail_item1, retail_item2, retail_item3]
    num = 1
    for item in product:
        print(f"Товар номер - {num}", item)
        num += 1


if __name__ == '__main__':
    main()
