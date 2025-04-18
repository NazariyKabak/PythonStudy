import os
import pickle

from task1 import Pet
from task2.car import Car
from task3.information import Information
from task4.employee import Employee
from task5.retail_item import RetailItem


employees = dict()
def print_menu():
    print("1. Знайти робітника імені")
    print("2. Додати його в словник.")
    print("3. Змінити дані.")
    print("4. Видалити робітника.")
    print("5. Menu!")
    print("6. Показати всі контакти!")
    print("0. Вийти\n")


def search_emp(dct):
    id = input("Enter the name: ")
    if id in dct:
        print(dct[id])
    else:
        print("Not found.")


def add_contact(dct):
    name = input("Enter the name: ")
    id = input("Enter the id: ")
    department = input("Enter the department: ")
    job_title = input("Enter the job title: ")
    dct[id] = Employee(name, department, job_title)
    print("Робітник доданий.")


def change_data_emp(dct):
    id = input("Enter the name: ")
    new_name = input("Enter the new email: ")
    new_department = input("Enter the new department: ")
    new_job_title = input("Enter the new job title: ")
    dct[id] = new_name, new_department, new_job_title
    print("Email змінено")


def delete_contact(dct):
    id = input("Enter the name: ")
    if id in dct:
        del dct[id]
    print(f"Контакт {id} видалено")


def print_all_contacts(dct):
    for key, value in dct.items():
        print(f"{key}: {value}")


def load_contacts():
    if os.path.exists("employee.dat"):
        with open("employee.dat", "rb") as file:
            return pickle.load(file)
    return {}


def save_contacts(dct):
    with open("employee.dat", "wb") as file:
        pickle.dump(dct, file)


def main():
    pass



if __name__ == '__main__':
    main()


