import random

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


def victorina(dct):
    points = 0
    again = "y"
    while again.upper() == "Y":
        random_state = random.choice(list(dct.keys()))
        print(f"State: {random_state}")
        capital = input("Enter capital: ")
        while capital.strip().lower() != dct[random_state].lower():
            print("Invalid capital")
            capital = input("Enter capital: ")
        points += 1
        print("Correct!")
        again = input("Do you wish to continue? (Y/N): ")

    print(f"\nВікторина завершена! Ви набрали {points} балів.")


victorina(states_capitals)
