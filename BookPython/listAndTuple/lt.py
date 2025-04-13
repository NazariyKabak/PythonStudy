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
def read_file_5():
    accounts = []
    with open('charge_accounts.txt', 'r') as f:
        for line in f:
            accounts.append(line.strip())
    return accounts


def search(arr):
    choice = input("Enter your choice: ")
    find = False
    for x in arr:
        if x == choice:
            print("Yes!")
            find = True
    if not find:
        print("No!")


#task6
# def more_n(arr, n):
#     for i in arr:
#         if i > n:
#             print(i)

#task7
# def write_in_file():
#     file = open('test_answer.txt', 'w')
#     another = "yes"
#     while another == "yes":
#         number_question = int(input("Enter question: "))
#         answer = input("Enter answer: ")
#         file.write(f"{number_question}. {answer}\n")
#         print("Ще5 додати?")
#         another = input("yes/no: ")
#     file.close()
#
#
# def read_in_file(file_name):
#     file = open(file_name, 'r')
#     answers = []
#     for line in file:
#         parts = line.strip().split('. ')
#         if len(parts) == 2:
#             answers.append(parts[1].upper())
#     return answers
#
#
# def check_exam():
#     correct_answer = read_in_file("test_answer.txt")
#     student_answer = read_in_file("student_answer.txt")
#
#     correct_count = 0
#     incorrect_questions = []
#
#     for i in range(len(correct_answer)):
#         if i < len(student_answer) and student_answer[i] == correct_answer[i]:
#             correct_count += 1
#         else:
#             incorrect_questions.append(i + 1)
#
#     total = len(correct_answer)
#     print(f"Правильних відповідей: {correct_count}")
#     print(f" Неправильних відповідей: {total - correct_count}")
#
#     if correct_count >= 15:
#         print("Ви склали іспит!")
#     else:
#         print("Ви НЕ склали іспит.")
#
#     if incorrect_questions:
#         print("Помилки в питаннях:", incorrect_questions)


#task8
def read_boys_file_():
    boys_name = []
    with open('BoyNames.txt', 'r') as f:
        for line in f:
            boys_name.append(line.strip())
    return boys_name


def read_girls_file():
    girls_name = []
    with open('GirlNames.txt', 'r') as f:
        for line in f:
            girls_name.append(line.strip())
    return girls_name


def input_user(arr_boys, arr2_girls):
    print("1 - Знайти ім'я дівчинки")
    print("2 - Знайти ім'я хлопчика")
    print("3 - Знайти обидва імені")
    choice = int(input("Enter your choice: "))
    found = False
    if choice == 1:
        name = input("Enter your name: ")
        if name in arr2_girls:
            print("Yes!")
            found = True
    elif choice == 2:
        name = input("Enter your name: ")
        if name in arr_boys:
            print("Yes!")
            found = True
    elif choice == 3:
        name_girl = input("Enter your name: ")
        name_boys = input("Enter your name: ")
        if name_boys in arr_boys:
            print("Yes!")
            found = True
        if name_girl in arr2_girls:
            print("Yes!")
            found = True
    else:
        print("Invalid choice.")

    if not found:
        print("No!")


#task9
def read_file_9():
    with open('USPopulation.txt', 'r') as f:
        population = [int(line.strip()) for line in f]
    return population


def analyze_population(population):
    changes = []
    for i in range(len(population) - 1):
        change = population[i + 1] - population[i]
        changes.append(change)
    avg_change = sum(changes) / len(changes)
    max_change = max(changes)
    min_change = min(changes)

    year_max = 1950 + changes.index(max_change) + 1
    year_min = 1950 + changes.index(min_change) + 1
    print(f"Середньорічна зміна: {avg_change:.2f}")
    print(f"Найбільший приріст: {max_change} у {year_max} році")
    print(f"Найменший приріст: {min_change} у {year_min} році")


#task10
def read_file_10():
    with open('WorldSeriesWinners.txt', 'r') as f:
        winners = [line.strip() for line in f]
    return winners


def analyze_winners(winners):
    team = input("Enter your team: ")
    winner_count = 0
    for winner in winners:
        if winner.lower() == team.lower():  # порівнюємо нечутливо до регістру
            winner_count += 1

    return winner_count

    # most_wins = max(winner_count.values())
    # most_wins_team = [team for team, count in winner_count.items() if count == most_wins]
    #
    # print(f"Команда з найбільшою кількістю перемог: {most_wins_team} ({most_wins} перемог)")


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


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    pop = read_file_9()
    print(pop)


main()
