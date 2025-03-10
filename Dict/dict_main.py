import json
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

# for key in my_dict:
#     if my_dict[key] == value_dict:
#         print(f"Ключ для значення '{value_dict}': {key}")
#         found = True
#         break
# if not found:
#     print("Not found")

#task8
# my_dict_swapped = {
#     value: key
#     for key, value in my_dict.items()
# }
# print(my_dict_swapped)

#task9
# my_dict2 = {
#     "city": "Brovary",
#     "country": "Ukraine"
# }
# my_dict3 = {**my_dict, **my_dict2}
# print(my_dict3)

#task10
# my_dict4 = {
#     "Nazarii": {"age": 22, "grade": "A"},
#     "Marichka": {"age": 21, "grade": "B"}
# }
# name = input("Enter name: ")
# if name in my_dict4:
#     print(my_dict4[name])
# else:
#     print("Name does not exist")

#task11
my_dict5 = {
    "a": 30,
    "b": 10,
    "c": 20
}
# sorted_my_dict5 = sorted(my_dict5.items(), key=lambda kv: kv[1])
# print(sorted_my_dict5)

#task12
# max_value = min_value = next(iter(my_dict5.values()))
# for key, value in my_dict5.items():
#     if value > max_value:
#         max_value = value
#     if value < min_value:
#         min_value = value
#
# print(max_value, min_value)

#task13
# text = input("Enter text: ").lower()
# char_counts = {}
# for char in text:
#     if char.isalpha():
#         char_counts[char] = char_counts.get(char, 0) + 1
# print(char_counts)
#
# #task14
# words = text.split()
# words_count = {}
# for word in words:
#     words_count[word] = words_count.get(word, 0) + 1
#
# max_word = max(words_count, key=words_count.get)
# max_count = words_count[max_word]
# print(max_word)

#task15
json_string = json.dumps(my_dict, ensure_ascii=False)
print(json_string)