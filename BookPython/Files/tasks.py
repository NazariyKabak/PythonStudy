import random


# #task1
# def open_file():
#     my_file = open('my_name.txt', 'w')
#     my_file.write('Nazarii')
#     my_file.close()
#
#
# #task2
# def read_file():
#     my_file = open('my_name.txt', 'r')
#     print(my_file.read())
#     my_file.close()
#
#
# #task3
# def write_file():
#     my_file = open('number_list.txt', 'w')
#     for number in range(1, 101):
#         my_file.write(str(number) + '\n')
#     my_file.close()
#
#
# #task4
# def read_file2():
#     my_file = open('number_list.txt', 'r')
#     total = 0
#     for number in my_file:
#         total += int(number)
#         print(number.rstrip('\n'))
#     my_file.close()
#     print(total)


#task1
def read_file_nums():
    my_file = open('number_list.txt', 'r')
    # total = 0
    for number in my_file:
        # total += int(number)
        print(number.rstrip('\n'))
    my_file.close()
    # print(total)


#task2
def read_file_nums2():
    file_name = input("Enter the file name: ")
    my_file = open(file_name, 'r')
    count_line = 0
    while count_line < 5:
        line = my_file.readline()
        count_line += 1
        print(line.rstrip('\n'))
    my_file.close()


#task3
def read_file_nums3():
    file_name = input("Enter the file name: ")
    my_file = open(file_name, 'r')
    count_line = 1
    for line in my_file:
        print(f'line {count_line}: {line.rstrip('\n')}')
        count_line += 1


#task4
def read_file_nums4():
    file_name = input("Enter the file name: ")
    my_file = open(file_name, 'r')
    count_line = 0
    for line in my_file:
        count_line += 1
    print(count_line)


#task5
def read_file_nums5():
    my_file = open('number_list.txt', 'r')
    total = 0
    for number in my_file:
        total += int(number)
        print(number.rstrip('\n'))
    my_file.close()
    print(total)


#task6
def read_file_nums6():
    my_file = open('number_list.txt', 'r')
    total = 0
    count = 0
    for number in my_file:
        total += int(number)
        count += 1
    my_file.close()
    average = total / count
    print(average)


#task7
def read_file_nums7():
    my_file = open('number_random_list.txt', 'w')
    count = int(input("Enter the number of random numbers: "))
    for number in range(count):
        random_num = random.randint(1, 500)
        my_file.write(str(random_num) + '\n')

    my_file.close()


#task8
def read_file_nums8():
    my_file = open('number_random_list.txt', 'r')
    total = 0
    count = 0
    for number in my_file:
        total += int(number)
        print(number.rstrip('\n'))
        count += 1
    my_file.close()
    print(total, count)


#task9
def read_file_nums9():
    try:
        name_file = input("Enter the file name: ")
        my_file = open(name_file, 'r')
        total = 0
        count = 0
        for number in my_file:
            total += int(number)
            count += 1
        my_file.close()
        average = total / count
        print(average)
    except IOError:
        print("File not found")
    except ValueError:
        print("Value error")


#task10
def write_file_golf():
    another = 'yes'
    golf_file = open("gold_data.txt", "a")
    while another == 'yes' or another == 'Yes':
        print("Введіть дані про гольфіста: ")
        name = input("Enter name: ")
        score = int(input("Enter score: "))
        golf_file.write(f"{name}\n")
        golf_file.write(f"{score}\n")

        print("Бажаєте що додати один запис?")
        another = input("Yes or No? ")
    golf_file.close()
    print("Дані додані у файл!")


def read_file_golf():
    golf_file = open("gold_data.txt", "r")
    name = golf_file.readline()
    while name != '':
        score = int(golf_file.readline())
        name = name.rstrip('\n')
        print(f'Name: {name}')
        print(f'Score: {score}')

        name = golf_file.readline()

    golf_file.close()


#task11
def write_file_personal_data():
    name = input("Enter name: ")
    dscr = input("Enter description: ")
    html_content = f"""<!DOCTYPE html>
    <html>
    <head>
        <title>{name}'s Personal Page</title>
    </head>
    <body>
        <center><h1>{name}</h1></center>
        <hr>
        <p>{dscr}</p>
        <hr>
    </body>
    </html>
    """
    with open("personal_data.html", "w", encoding="utf-8") as file:
        file.write(html_content)


def main():
    # write_file()
    write_file_personal_data()


if __name__ == '__main__':
    main()
