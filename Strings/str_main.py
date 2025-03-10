#task1 Довжина рядка
from operator import index

count_char = 0
word = input("Enter a word: ")
for char in word:
    count_char += 1
print(count_char)

#task2 Перевірка першої літери
if word[0].isupper():
    print("The word is a uppercase.")
else:
    print("The word is a lowercase.")

#task3 Останній символ
print(word[-1])

#task4 Перевернутий рядок
reversed_word = ''
for char in range(len(word) - 1, -1, -1):
    reversed_word += word[char]
print(reversed_word)

#task5 Чи є рядок числом?
isDigit = True
for char in word:
    if not char.isdigit():
        isDigit = False
        break

print(isDigit)

#task6 Кількість голосних та приголосних
vowels = "aeiouAEIOU"
count_vowels = 0
count_consonants = 0
for char in word:
    if char in vowels:
        count_vowels += 1
    elif char.isalpha():
        count_consonants += 1
print(count_vowels)
print(count_consonants)

#task7 Підрахунок певної літери
count_letter = 0
letter = input("Enter a letter: ")
for char in range(len(word)):
    if letter == word[char]:
        count_letter += 1

print(count_letter)

#task8 Перетворення реєстру
new_word = ""
for char in word:
    if char.islower():
        new_word += char.upper()
    else:
        new_word += char.lower()

print(new_word)

#task9 Перевірка паліндрому
isPalidrome = False
reversed_word = ''
for char in range(len(word) - 1, -1, -1):
    reversed_word += word[char]

if reversed_word == word:
    isPalidrome = True
print(isPalidrome)

#task10 Замінити всі пропуски на -
new_word2 = ""
for char in word:
    if char == " ":
        new_word2 += "-"
    else:
        new_word2 += char
print(new_word2)

#task11 Перетворити першу літеру кожного слова у велику (як у заголовку)
new_text = ""
capitalize_next = True
for char in word:
    if capitalize_next and char.isalpha():
        new_text += char.upper()
        capitalize_next = False
    else:
        new_text += char.lower()

    if char == " ":
        capitalize_next = True
print(new_text)

#task12 Найдовше слово у реченні
max_word = ""
current_word = ""
for char in word:
    if char == " ":
        if len(current_word) > len(max_word):
            max_word = current_word
        current_word = ""
    else:
        current_word += char

print(max_word)

#task13 Перевірка email-адреси
# has_at = False
# has_dot_after_at = False
# at_index = -1
# email_you= input("Enter an email: ")
# for char in range(len(email_you)):
#     if email_you[char]=='@':
#         if has_at:
#             print("Email неправильний: більше одного @")
#             exit()
#         has_at = True
#         at_index = char
#
# if not has_at or at_index == 0 or at_index == len(email_you)-1:
#     print("Email incorrect")
#     exit()
#
# for i in range(at_index+1, len(email_you)):
#     if email_you[i]=='.':
#         if i == at_index+1:
#             print("Email неправильний: . не може йти одразу після @")
#             exit()
#         has_dot_after_at = True
#
# if not has_dot_after_at or email_you[-1]==".":
#     print("Email incorrect")
# else:
#     print("Email correct")

#task14 Підрахунок слів у реченні
count_word = 0
in_word = False
for char in word:
    if char != " " and not in_word:
        count_word += 1
        in_word = True
    elif char == " ":
        in_word = False
print(count_word)

#task15 Парольний перевіряльник
has_num = False
has_char_upper = False
if len(word) >= 8:
    for char in word:
        if char.isdigit():
            has_num = True
        if char.isupper():
            has_char_upper = True
    if has_num and has_char_upper:
        print("Пароль надійний")
    else:
        print("Пароль ненадійний")
else:
    print("Пароль занадто короткий")
