# #task1
# def initials(fio):
#     initials_name = fio[0] + "."
#     for i in range(len(fio)):
#         if fio[i] == " ":
#             initials_name += fio[i + 1] + "."
#     return initials_name
#
#
# print(initials("Nazarii Kabak Volodimyrovych"))
#
#
# #task2
# def sum_num_in_string(string):
#     # num = int(string)
#     sum_num = 0
#     # while num > 0:
#     #     digit = num % 10
#     #     sum_num += digit
#     #     num = num // 10
#     for i in range(len(string)):
#         if string[i].isdigit():
#             sum_num += int(string[i])
#     return sum_num
#
#
# print(sum_num_in_string("2514"))
#
#
# #task3
# def print_date(date):
#     arr = date.split(".")
#     month = ""
#     if arr[1] == "01":
#         month = "January"
#     elif arr[1] == "02":
#         month = "February"
#     elif arr[1] == "03":
#         month = "March"
#     elif arr[1] == "04":
#         month = "April"
#     elif arr[1] == "05":
#         month = "May"
#     elif arr[1] == "06":
#         month = "June"
#     elif arr[1] == "07":
#         month = "July"
#     elif arr[1] == "08":
#         month = "August"
#     elif arr[1] == "09":
#         month = "September"
#     elif arr[1] == "10":
#         month = "October"
#     elif arr[1] == "11":
#         month = "November"
#     elif arr[1] == "12":
#         month = "December"
#     else:
#         print("Error")
#
#     new_date = arr[0] + " " + month + " " + arr[2] + " y."
#     return new_date
#
#
# print(print_date("12.03.2024"))
#
#
# #task4
# # morse_code = {
# #     'A': '.-', 'B': '-...', 'C': '-.-.',
# #     'D': '-..', 'E': '.', 'F': '..-.',
# #     '1': '.----', '2': '..---', ' ': 'пробел', ',': '--..--', '.': '.-.-.-',
# #     '?': '..--..'
# # }
# #
# # user_input = input("Enter symbol")
# # for char in user_input:
# #     if char in morse_code:
# #         print(morse_code[char], end="")
# #     else:
# #         print('?', end=' ')
#
#
# #task5
# def translate_number_phone(number):
#     translate_num = ""
#     for char in number:
#         if char.isdigit():
#             translate_num += char
#         elif char == "-":
#             translate_num += char
#         elif char.isalpha():
#             if char == "A" or char == "B" or char == "C":
#                 translate_num += "2"
#             elif char == "D" or char == "E" or char == "F":
#                 translate_num += "3"
#             elif char == "G" or char == "H" or char == "I":
#                 translate_num += "4"
#             elif char == "L" or char == "J" or char == "K":
#                 translate_num += "5"
#             elif char == "M" or char == "N" or char == "O":
#                 translate_num += "6"
#             elif char == "P" or char == "Q" or char == "R" or char == "S":
#                 translate_num += "7"
#             elif char == "T" or char == "U" or char == "V":
#                 translate_num += "8"
#             elif char == "W" or char == "X" or char == "Y" or char == "Z":
#                 translate_num += "9"
#     return translate_num
#
#
# print(translate_number_phone("555-GET-FOOD"))
#
#
# #task6
def read_file(filename):
    with open(filename, "r") as file:
        line = file.readlines()
    return line


#
#
# def count_words(arr):
#     count_word = 0
#     count_sentences = len(arr)
#     for sentence in arr:
#         words = sentence.split()
#         count_word += len(words)
#     avg = count_word / count_sentences
#     return avg
#
#
# # sentences = read_file("text.txt")
# # print(sentences)
# # print(count_words(sentences))
#
#
# #task7
# def analyze_symbol(arr):
#     count_letter_upper = 0
#     count_letter_lower = 0
#     count_num = 0
#     count_space = 0
#     for line in arr:
#         # words = line.split()
#         for word in line:
#             if word.isalpha():
#                 if word.isupper():
#                     count_letter_upper += 1
#                 elif word.islower():
#                     count_letter_lower += 1
#             elif word.isdigit():
#                 count_num += 1
#             elif word == " ":
#                 count_space += 1
#     return count_letter_upper, count_letter_lower, count_num, count_space
#
#
# arrays = read_file("text7.txt")
# print(analyze_symbol(arrays))
#
#
# #task8
# def correct_sentence(sentences):
#     # Список для збереження відредагованих речень
#     corrected = []
#
#     # Тимчасове речення (накопичує символи)
#     sentence = ""
#
#     for char in sentences:
#         sentence += char
#         # Якщо зустрічаємо кінець речення — обробляємо
#         if char in ".!?":
#             sentence = sentence.strip()  # прибираємо пробіли
#             if sentence:
#                 # Перша літера — велика, решта без змін
#                 corrected.append(sentence[0].upper() + sentence[1:])
#             sentence = ""
#
#     # Якщо після останнього знаку ще щось є — додаємо (наприклад, без крапки в кінці)
#     if sentence.strip():
#         sentence = sentence.strip()
#         corrected.append(sentence[0].upper() + sentence[1:])
#
#     # Об'єднуємо назад у строку
#     return " ".join(corrected)
#
#
# print(correct_sentence("привіт! мене звати Назарій."))
#
#
# #task9
# def count_letter(sentences):
#     vowels = "aeiouAEIOU"
#     count_vowels = 0
#     count_consonants = 0
#     for char in sentences:
#         if char in vowels:
#             count_vowels += 1
#         elif char.isalpha():
#             count_consonants += 1
#     print(count_vowels)
#     print(count_consonants)
#
#
# #task10
# def often_symbol(word):
#     letters = []
#     max_count = 0
#     most_common_char = ""
#     for letter in word:
#         letters.append(letter)
#
#     for letter in range(len(letters)):
#         count = 0
#         for letter2 in range(len(letters)):
#             if letters[letter] == letters[letter2]:
#                 count += 1
#                 print(letters[letter])
#         if count > max_count:
#             max_count = count
#             most_common_char = letters[letter]
#     return most_common_char, max_count
#
#
# print(often_symbol("aabbbcccc"))
#
#
# #task11
# def word_separator(sentence):
#     new_sentence = ""
#     for char in range(len(sentence)):
#         if sentence[char].isupper():
#             new_sentence += " "
#         new_sentence += sentence[char]
#     return new_sentence
#
#
# print(word_separator("ЗупинисьІВідчуйЗапахТроянд"))
#
#
# #task12
# def task12(sentence):
#     words = sentence.split()
#     new_sentence = ""
#     for word in words:
#         first_letter = word[0]
#         for letter in range(1, len(word)):
#             new_sentence += word[letter]
#         new_sentence += first_letter + "ки" + " "
#     return new_sentence
#
#
# def task12_2(sentence):
#     words = sentence.split()
#     new_words = []
#     for word in words:
#         first_letter = word[0]
#         new_word = word[1:] + first_letter + "ки"
#         new_words.append(new_word)
#     return " ".join(new_words)
#
#
# print(task12("Проспал почти всю ночь"))
# print(task12_2("Проспал почти всю ночь"))
#
#
# #task13
def read_data(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    all_number = []
    powerball_number = []
    for line in lines:
        parts = list(map(int, line.strip().split()))
        all_number.append(parts[:-1])
        powerball_number.append(parts[-1])
    return all_number, powerball_number


def flatten(lst):
    return [item for sublist in lst for item in sublist]


def count_frequencies(numbers, max_num):
    freq = [0] * (max_num + 1)
    for number in numbers:
        freq[number] += 1
    return freq


def most_common_numbers(numbers, top_n=10):
    flat = flatten(numbers)
    freq = count_frequencies(flat, 69)
    result = []
    for i in range(1, len(freq)):
        result.append((i, freq[i]))
    result.sort(key=lambda x: x[1], reverse=True)
    return result[:top_n]


def least_common_numbers(numbers, bottom_n=10):
    flat = flatten(numbers)
    freq = count_frequencies(flat, 69)
    result = []
    for i in range(1, len(freq)):
        result.append((i, freq[i]))
    result.sort(key=lambda x: x[1])
    return result[:bottom_n]


def matured_numbers(numbers, top_n=10):
    flat = flatten(numbers)
    last_seen = [-1] * 70  # з 0 по 69
    for idx, draw in enumerate(numbers):
        for num in draw:
            last_seen[num] = idx
    result = []
    for i in range(1, 70):
        if last_seen[i] != -1:
            result.append((i, last_seen[i]))
    result.sort(key=lambda x: x[1])
    return result[:top_n]


def frequency_all(numbers, number_range):
    flat = flatten(numbers)
    freq = count_frequencies(flat, number_range)
    result = []
    for i in range(1, number_range + 1):
        result.append((i, freq[i]))
    return result


# main_numbers, powerball_numbers = read_data("pbnumbers.txt")
# print(main_numbers)
# print(powerball_numbers)
# print(most_common_numbers(main_numbers))
# print(least_common_numbers(main_numbers))
# print(matured_numbers(main_numbers))
# print(frequency_all(main_numbers, 69))
# print(frequency_all([[num] for num in powerball_numbers], 26))


#task14
def read_gas_prices(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    data = []
    for line in lines:
        line = line.strip()
        date, price = line.split(':')
        data.append((date, float(price)))
    return data


def avg_price_year(data):
    years = []
    for date, _ in data:
        year = date.split('-')[2]
        if year not in years:
            years.append(year)
    for year in years:
        sum_price = 0
        count = 0
        for date, price in data:
            if date.split('-')[2] == year:
                sum_price += price
                count += 1
        avg_price = sum_price / count
        print(f"{year}: {avg_price:.3f}")


def avg_price_month(data):
    year_months = []
    for date, _ in data:
        month = date.split('-')[0]
        year = date.split('-')[2]
        ym = f"{year}-{month}"
        if ym not in year_months:
            year_months.append(ym)

    for ym in year_months:
        sum_price = 0
        count = 0
        for date, price in data:
            month = date.split('-')[0]
            year = date.split('-')[2]
            if f"{year}-{month}" == ym:
                sum_price += price
                count += 1
        avg = sum_price / count
        print(f"{ym}: {avg:.3f}")


def max_min_price_in_year(data):
    years = []
    for date, _ in data:
        year = date.split('-')[2]
        if year not in years:
            years.append(year)

    for year in years:
        min_price = float('inf')
        max_price = float('-inf')
        for date, price in data:
            if date.split('-')[2] == year:
                if price < min_price:
                    min_price = price
                if price > max_price:
                    max_price = price
        print(f"{year}: min = {min_price:.3f}, max = {max_price:.3f}")


def sort_prices_ascending(data, output_filename):
    sorted_data = sorted(data, key=lambda x: x[1])
    with open(output_filename, "w") as file:
        for date, price in sorted_data:
            file.write(f"{date}:{price:.3f}\n")
    print(f"[↑] Дані записано у файл: {output_filename}")


def sort_prices_descending(data, output_filename):
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
    with open(output_filename, "w") as file:
        for date, price in sorted_data:
            file.write(f"{date}:{price:.3f}\n")
    print(f"[↑] Дані записано у файл: {output_filename}")


gas_prices = read_gas_prices("GasPrices.txt")
print(gas_prices)
avg_price_year(gas_prices)
avg_price_month(gas_prices)
print(max_min_price_in_year(gas_prices))
sort_prices_ascending(gas_prices, "sorted_prices_asc.txt")
sort_prices_ascending(gas_prices, "sorted_prices_dsc.txt")