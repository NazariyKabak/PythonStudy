# #task1
import random
#
#
# def input_arr():
#     list_day = []
#     for day in range(7):
#         day = int(input("Enter a sum sales: "))
#         list_day.append(day)
#     return list_day
#
#
# def sum_sales(arr):
#     sum_sales_week = 0
#     for i in arr:
#         sum_sales_week += i
#     return sum_sales_week
#
#
#
# #task2
# def random_number():
#     random_num_list = []
#     for _ in range(7):
#         random_num_list.append(random.randint(0, 9))
#     return random_num_list
#
# #task3
# MONTH = 12
# def input_month():
#     month_arr = []
#     for month in range(MONTH):
#         month = int(input("Enter a month: "))
#         month_arr.append(month)
#     return month_arr
#
#
# def total(arr):
#     total = 0
#     for i in arr:
#         total += i
#     return total
#
#
#
# def avg(arr, total):
#     avg = total / len(arr)
#     return avg
#
#
# def precipitation_min_max(arr):
#     precipitation_min = arr[0]
#     precipitation_max = arr[0]
#     for i in arr:
#         if i < precipitation_min:
#             precipitation_min = i
#         if i > precipitation_max:
#             precipitation_max = i
#     return precipitation_min, precipitation_max



#task4
# COUNT_ELEMENTS = 20
# def input_arr():
#     nums = []
#     for _ in range(COUNT_ELEMENTS):
#         nums.append(int(input()))
#     return nums
#
# def sum_nums(arr):
#     sum_num = 0
#     for num in arr:
#         sum_num += num
#     return sum_num
#
# def min_max(arr):
#     return min(arr), max(arr)
#
# def avg(arr):
#     return sum(arr) / len(arr)
#task5


#task6
# def more_n(arr, n):
#     for i in arr:
#         if i > n:
#             print(i)



#task11
# def generate_matrix():
#     rows = 3
#     cols = 3
#     matrix = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
#     return matrix
# def magic_square(arr):
#
#     sum_rows = [sum(row) for row in arr]
#     sum_col = [sum(arr[row][col] for row in range(len(arr))) for col in range(len(arr[0]))]
#
#     return sum_col == sum_rows
#
#     # for row in range(len(arr)):
#     #     sum_rows = 0
#     #     for col in range(len(arr[row])):
#     #         sum_rows += arr[row][col]
#     #     print(f'Сума рядка {row}: {sum_rows}')
#     #     # return sum_rows
#     #
#     #
#     # for col in range(len(arr[0])):
#     #     sum_cols = 0
#     #     for row in range(len(arr)):
#     #         sum_cols += arr[row][col]
#     #     print(f'Сума стовпчика {col} = {sum_cols}')
#     # return  sum_rows, sum_col


#task12
def input_n():
    n = int(input())
    return n


def arr_nums(n):
    return list(range(2, n))


def is_prime(arr):
    is_Prime = True
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            is_Prime = False
            break
        print(f'{i} {is_Prime}')


def main():
    pass
main()

