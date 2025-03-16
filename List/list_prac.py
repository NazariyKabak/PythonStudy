#task1 Видалити всі дублікатні елементи у списку
import itertools
import random

from pygments.lexers import q


def delete_duplicates(arr):
    new_arr = []
    for item in arr:
        if item not in new_arr:
            new_arr.append(item)
    return new_arr


# print(delete_duplicates([1, 2, 4, 4, 5, 6]))


#task2 Перемішати елементи списку (без shuffle())
def shuffle_list(arr):
    random.shuffle(arr)
    return arr


# print(shuffle_list([1, 2, 4, 4, 5, 6]))


#task3 Знайти індекс мінімального і максимального елемента
def min_max_index(arr):
    max_el = arr[0]
    min_el = arr[0]
    min_index = 0
    max_index = 0
    for el in range(1, len(arr)):
        if arr[el] > max_el:
            max_el = arr[el]
            max_index = el
        if arr[el] < min_el:
            min_el = arr[el]
            min_index = el
    return max_index, min_index


# print(min_max_index([1, 12, 4, 4, -2, 6]))

#task4  Змінити місцями найбільший та найменший елемент
def change_place(arr):
    max_index, min_index = min_max_index(arr)
    arr[max_index], arr[min_index] = arr[min_index], arr[max_index]
    return arr


# print(change_place([1, 12, 4, 4, -2, 6]))


#task5 Об'єднати два списки без extend() та +
def combine_list(arr1, arr2):
    new_arr = []
    for el in arr1:
        new_arr.append(el)
    for el in arr2:
        new_arr.append(el)
    return new_arr


# print(combine_list([1, 2, 3], [4, 5, 6]))


#task6 Розбити список на парні та непарні числа
def break_even_odd(arr):
    even_arr = []
    odd_arr = []
    for el in arr:
        if el % 2 == 0:
            even_arr.append(el)
        else:
            odd_arr.append(el)
    return even_arr, odd_arr


# print(break_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))


#task7 Знайти другу найбільшу цифру у списку
def second_max_num(arr):
    if len(arr) < 2:
        print("Недостатньо елементів")
    max_num = arr[0]
    second_max = arr[0]
    for el in arr:
        if el > max_num:
            second_max = max_num
            max_num = el
        elif second_max < el < max_num:
            second_max = el
    return second_max


# print(second_max_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


#task8 Обчислити добуток всіх елементів списку
def product_element(arr):
    product = 1
    for el in arr:
        product *= el
    return product


#task9 Перемістити всі 0 у кінець списку ([0, 1, 0, 3, 12] → [1, 3, 12, 0, 0])
def move_zeros(arr):
    non_zero = [num for num in arr if num != 0]
    zeros = [0] * arr.count(0)
    return non_zero + zeros


# print(move_zeros([1, 2, 0, 4, 0, 6, 0, 8, 9]))


def move_zeros_in_place(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return arr


# print(move_zeros_in_place([1, 2, 0, 4, 0, 6, 0, 8, 9]))


#task10 Перевірити, чи всі елементи списку однакові
def check_same(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            return False
    return True


# print(check_same([1, 1, 1, 1, 1, 1]))

#task11 Обчислити суму елементів матриці (двовимірного списку)
def sum_element_in_matrix(matrix):
    sum_el = 0
    for i in range(len(matrix)):
        for j in range(len(matrix) + 1):
            sum_el += matrix[i][j]

    return sum_el


# print(sum_element_in_matrix([
#     [1, 2, 3],
#     [4, 5, 6]]))


#task12 Знайти сліди магічного квадрату (сума рядків = сума стовпців)
def magic_square(arr):
    if not arr:
        return "Матриця порожня"
    sum_row = 0
    sum_col = 0
    n = len(arr)
    sum_row = [sum(row) for row in arr]
    sum_col = [sum(arr[j][i] for j in range(n)) for i in range(n)]
    return sum_col, sum_row


print(magic_square([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]))


#task13 Перетворити список списків у плоский список (flatten())
def flatten(arr):
    flat_list = []
    for sublist in arr:
        for item in sublist:
            flat_list.append(item)
    return flat_list


#task14
def median(arr):
    arr.sort()
    n = len(arr)
    mid = n // 2

    if n % 2 == 1:
        return arr[mid]
    else:
        return (arr[mid] + arr[mid - 1]) / 2


#task15
def generate_permutations(arr):
    return list(itertools.permutations(arr))
