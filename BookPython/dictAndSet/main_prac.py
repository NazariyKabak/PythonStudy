import os
import random
import pickle

# #task1
# rooms = {
#     "CS101": 3004,
#     "CS102": 4501,
#     "CS103": 6755,
#     "CS104": 1244,
#     "CS105": 1411
# }
#
# # Словник 2: Номер курсу -> Преподаватель
# instructors = {
#     "CS101": "Хайнс",
#     "CS102": "Альварадо",
#     "CS103": "Рич",
#     "NT110": "Берк",
#     "CM241": "Ли"
# }
#
# # Словник 3: Номер курсу -> Час
# times = {
#     "CS101": "8:00",
#     "CS102": "9:00",
#     "CS103": "10:00",
#     "NT110": "11:00",
#     "CM241": "13:00"
# }
#
#
# def display_info(dict1, dict2, dict3):
#     info = []
#
#     again = "y"
#     while again.upper() == "Y":
#         key_input = input("Enter key: ")
#         if key_input not in dict1:
#             print("Not found key")
#             key_input = input("Enter key: ")
#
#         info = []
#         for key in dict1:
#             if key == key_input:
#                 info.append(dict1[key])
#
#         for key in dict2:
#             if key == key_input:
#                 info.append(dict2[key])
#
#         for key in dict3:
#             if key == key_input:
#                 info.append(dict3[key])
#         print(info)
#         again = input("Do you want to continue? (y/n): ")
#     # return info
#
#
# # print(display_info(rooms, instructors, times))
# display_info(rooms, instructors, times)

#task2
states_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

# def victorina(dct):
#     points = 0
#     again = "y"
#     while again.upper() == "Y":
#         random_state = random.choice(list(dct.keys()))
#         print(f"State: {random_state}")
#         capital = input("Enter capital: ")
#         while capital.strip().lower() != dct[random_state].lower():
#             print("Invalid capital")
#             capital = input("Enter capital: ")
#         points += 1
#         print("Correct!")
#         again = input("Do you wish to continue? (Y/N): ")
#
#     print(f"\nВікторина завершена! Ви набрали {points} балів.")
#
#
# victorina(states_capitals)

#task3

codes = {
    'A': '%',
    'a': '9',
    'B': '@',
    'b': '#',
    'C': '&',
    'c': '*',
    'D': '1',
    'd': '2',
    'E': '!',
    'e': '3',
    'F': '$',
    'f': '4',
    'G': '^',
    'g': '5',
    'H': '?',
    'h': '6',
    'I': '=',
    'i': '7',
    'J': '+',
    'j': '8',
    'K': '<',
    'k': '>',
    'L': '|',
    'l': '~',
    'M': '{',
    'm': '}',
    'N': '[',
    'n': ']',
    'O': '/',
    'o': '\\',
    'P': ';',
    'p': ':',
    'Q': ',',
    'q': '.',
    'R': '`',
    'r': '-',
    'S': '0',
    's': '(',
    'T': ')',
    't': '_',
    'U': '"',
    'u': "'",
    'V': 'a',
    'v': 'b',
    'W': 'c',
    'w': 'd',
    'X': 'e',
    'x': 'f',
    'Y': 'g',
    'y': 'h',
    'Z': 'i',
    'z': 'j',
    ' ': ' '  # щоб не втрачати пробіли
}


# def encrypt_file(filename1, filename2):
#     with open(filename1, 'r') as f:
#         text = f.read()
#     encrypted_text = ''
#     for char in text:
#         encrypted_text += codes.get(char, char)
#
#     with open(filename2, 'w') as f:
#         f.write(encrypted_text)


# print(encrypt_file("input.txt", "output.txt"))

#task4
def unique_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    words = (text.replace('.', '').replace(',', '').replace('-', '')
             .replace('«', '').replace('»', '').replace('“', '')
             .replace('”', '').lower().split())
    unique_word = set(words)

    return unique_word


#task5
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()

    cleaned_text = (text.replace('.', '')
                    .replace(',', '')
                    .replace('-', '')
                    .replace('«', '')
                    .replace('»', '')
                    .replace('“', '')
                    .replace('”', '')
                    .lower())
    words = cleaned_text.split()

    count_word = dict()
    count = 1

    for word in words:
        if word in count_word:
            count_word[word] += 1
        else:
            count_word[word] = 1

    return count_word


# print(count_words('unique_words.txt'))


#task6
def read_file1(filename):
    with open(filename, 'r') as file:
        text1 = file.read()

    words1 = (text1.replace('.', '').replace(',', '').replace('-', '')
              .replace('«', '').replace('»', '').replace('“', '')
              .replace('”', '').lower().split())

    set_1 = set(words1)

    return set_1


def read_file2(filename):
    with open(filename, 'r') as file:
        text2 = file.read()

    words2 = (text2.replace('.', '').replace(',', '').replace('-', '')
              .replace('«', '').replace('»', '').replace('“', '')
              .replace('”', '').lower().split())

    set_2 = set(words2)
    return set_2


def equal_sets(set_1, set_2):
    set_3 = set_1.union(set_2)

    set_intersection = set_1.intersection(set_2)
    set_difference = set_2.difference(set_1)
    set_difference2 = set_1.difference(set_2)
    set_symetric_difference = set_1.symmetric_difference(set_2)
    print("🔷 Всі унікальні слова з обох файлів:")
    print(set_1.union(set_2), "\n")

    print("✅ Слова, які зустрічаються в обох файлах:")
    print(set_1.intersection(set_2), "\n")

    print("📁 Слова з другого файлу, яких немає в першому:")
    print(set_2.difference(set_1), "\n")

    print("📁 Слова з першого файлу, яких немає в другому:")
    print(set_1.difference(set_2), "\n")

    print("🔀 Симетрична різниця (є тільки в одному з файлів):")
    print(set_1.symmetric_difference(set_2))


set_1 = read_file1('file_1.txt')
set_2 = read_file2('file_2.txt')


# equal_sets(set_1, set_2)


#task7
def read_file_task7(filename):
    with open(filename, 'r') as file:
        text = file.read().splitlines()

    input_year = int(input("Enter year: "))
    year = 1903
    team_by_year = dict()
    team_win_count = dict()
    worlds_series_winner = dict()
    for team in text:
        # Пропускаємо роки, коли не проводилась серія
        if year in [1904, 1994]:
            year += 1
            continue
        team_by_year[year] = team

        if team in team_win_count:
            team_win_count[team] += 1
        else:
            team_win_count[team] = 1

        year += 1

    if input_year in team_by_year:
        print("Переможець:", team_by_year[input_year])
        print("Кількість перемог:", team_win_count[team_by_year[input_year]])
    else:
        print("У цей рік серію не проводили.")
    return team_by_year, team_win_count


# print(read_file_task7('world_series_winners.txt'))


#task8
def print_menu():
    print("1. Знайти адресу електронної пошти по імені")
    print("2. Додати ім'я та його email.")
    print("3. Змінити email користувача...")
    print("4. Видалити ім'я та email.")
    print("5. Menu!")
    print("6. Показати всі контакти!")
    print("0. Вийти\n")


def search_email(dct):
    name = input("Enter the name: ")
    if name in dct:
        print(dct[name])
    else:
        print("Not found.")


def add_contact(dct):
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    dct[name] = email
    print("Ім'я та email додані.")


def change_email(dct):
    name = input("Enter the name: ")
    new_email = input("Enter the new email: ")
    dct[name] = new_email
    print("Email змінено")


def delete_contact(dct):
    name = input("Enter the name: ")
    if name in dct:
        del dct[name]
    print(f"Контакт {name} видалено")


def print_all_contacts(dct):
    for key, value in dct.items():
        print(f"{key}: {value}")


def load_contacts():
    if os.path.exists("contact.dat"):
        with open("contact.dat", "rb") as file:
            return pickle.load(file)
    return {}


def save_contacts(dct):
    with open("contact.dat", "wb") as file:
        pickle.dump(dct, file)


def user_choice():
    contacts = load_contacts()
    print_menu()
    # dct = dict()
    choice = int(input("Enter number 1-5:"))
    again = 'y'
    while again.upper() == 'Y':
        match choice:
            case 1:
                search_email(contacts)
            case 2:
                add_contact(contacts)
            case 3:
                change_email(contacts)
            case 4:
                delete_contact(contacts)
            case 5:
                print_menu()
            case 6:
                print_all_contacts(contacts)
            case 0:
                save_contacts(contacts)
                print("Successfully saved.")
                break
            case _:
                print("Invalid choice.")
                choice = int(input("Enter number 1-5:"))

        again = input("Enter y/n!")
        if again == 'y' or again == 'Y':
            choice = int(input("Enter number 1-5:"))


# user_choice()


#task9
# cards = {
#     "2": 2,
#     "3": 3,
#     "4": 4,
#     "5": 5,
#     "6": 6,
#     "7": 7,
#     "8": 8,
#     "9": 9,
#     "10": 10,
#     "J": 10,
#     "Q": 10,
#     "K": 10,
#     "A": 11  # спочатку як 11, логіка зниження буде нижче
# }
#
# deck = []
# for card in cards:
#     deck.extend([card] * 4)
#
# random.shuffle(deck)
#
# cards_player1 = []
# cards_player2 = []
#
#
# def count_points(player_cards, cards_dict):
#     total = 0
#     ace_count = 0
#     for card in player_cards:
#         total += cards_dict[card]
#         if card == 'A':
#             ace_count += 1
#
#     while total > 21 and ace_count > 0:
#         total -= 10
#         ace_count -= 1
#     return total
#
#
# while True:
#     cards_player1.append(deck.pop())
#     cards_player2.append(deck.pop())
#
#     points1 = count_points(cards_player1, cards)
#     points2 = count_points(cards_player2, cards)
#
#     print(f"\nPlayer 1 cards: {cards_player1} | Points: {points1}")
#     print(f"Player 2 cards: {cards_player2} | Points: {points2}")
#
#     if points1 >= 21 or points2 >= 21:
#         break
#
#
# print("\n🏁 Game Over!")
#
# if points1 > 21 and points2 > 21:
#     print("Both players busted! 🤯 No winners.")
# elif points1 > 21:
#     print("Player 1 busted! Player 2 wins 🎉")
# elif points2 > 21:
#     print("Player 2 busted! Player 1 wins 🎉")
# elif points1 == points2:
#     print("It's a tie! 🤝")
# elif points1 == 21:
#     print("Player 1 hits 21! 🥇")
# elif points2 == 21:
#     print("Player 2 hits 21! 🥇")
# elif points1 > points2:
#     print("Player 1 wins! 💪")
# else:
#     print("Player 2 wins! 💪")


#task10
def read_file10(filename):
    index = dict()
    with open(filename, 'r') as file:
        line_number = 1
        for line in file:
            # Очищення рядка від пунктуації, перевод у нижній регістр
            line = line.strip().lower()
            line = line.replace('.', '').replace(',', '')
            words = line.split()

            for word in words:
                if word not in index:
                    index[word] = [line_number]
                else:
                    if line_number not in index[word]:
                        index[word].append(line_number)

            line_number += 1
    return index



print(read_file10('text.txt'))
