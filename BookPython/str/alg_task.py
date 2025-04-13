#task1
choice = "y"
# while choice.upper() == "Y":
#     print("Welcome to the game!")
#     choice = input("Do you want to play? (y/n): ")
# print("Thank you for playing!")

#task2
mystring = " 1Hello2, Worl3d!.com"
count_space = 0
for string in mystring:
    if string == " ":
        count_space += 1
print(count_space)

#task3
count_num = 0
for string in mystring:
    if string.isdigit():
        count_num += 1
print(count_num)

#task4
count_letter_lowercase = 0
for string in mystring:
    if string.islower():
        count_letter_lowercase += 1
print(count_letter_lowercase)


#task5
def check_end(string):
    if string.endswith(".com"):
        return True
    else:
        return False


print(check_end(mystring))

#task6
str1 = "Titanic"
str2 = ""
for char in str1:
    if char == 't':
        str2 += char.upper()
    else:
        str2 += char
print(str2)


#task7
def revers_str(word):
    reversed_word = ''
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word


word = "Hello"
print(revers_str(word))

#task8
print(mystring[:3])


#task9
def srez(word):
    return word[-3:]


print(srez(mystring))

#task10
str_list = "пирожки>молоко>стряпня"
new_list = str_list.split(">")
print(new_list)