my_dict = {
    "name": "Nazarii",
    "age": "22",
    "gender": "Male",
}
# n = int(input("Enter number: "))
# for _ in range(n):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     my_dict[key] = value

#task1
# count = 0
# for key in my_dict:
#     count += 1
# print(count)

#task2
k = input("Enter key: ")
found = False
# for key in my_dict.keys():
#     if key == k:
#         found = True
#         print(k)
#         break
# print(found)

#task3
# for key in my_dict.keys():
#     if key == k:
#         found = True
#         print("Ключ є у словнику")
#         break
# print(found)

#task4
# value_dict = input("Enter value: ")
# my_dict[k] = value_dict

#task5
# new_dict = {}
# for key, value in my_dict.items():
#     if key != k:
#         new_dict[key] = value
#
#
# print(new_dict)

#task6
# text = input("Enter text: ")
# count_word = 0
# for key in my_dict:
#     if key in text:
#         count_word += 1
# print(count_word)

#task7
value_dict = input("Enter value: ")
# for key in my_dict:
#     if key == k:
#         print(my_dict[key])

for key in my_dict:
    if my_dict[key] == value_dict:
        print(f"Ключ для значення '{value_dict}': {key}")
        found = True
        break
if not found:
    print("Not found")

