import random



#task1


str1 = input("Enter word: ")


# vowels = "aeiouAEIOU"
# count_vowels = 0
# for char in str1:
#     if char in vowels:
#         count_vowels += 1
# print(count_vowels)

#task2
# isPalidrome = False
# str1_reversed = ""
# for i in range(len(str1)-1, -1, -1):
#     str1_reversed += str1[i]
# print(str1_reversed)
# if str1_reversed == str1:
#     isPalidrome = True
# print(isPalidrome)

#task3

# new_word = ""
# for char in str1:
#     if char == " ":
#         new_word += "-"
#     else:
#         new_word += char
# print(new_word)

#task4

# max_word = ""
# current_word = ""
# for char in range(len(str1)):
#     if str1[char] == " ":
#         if len(current_word) > len(max_word):
#             max_word = current_word
#         current_word = ""
#     else:
#         current_word += str1[char]
# print(max_word)

#task5
# new_word = ""
# for char in str1:
#     if char.islower():
#         new_word += char.upper()
#     else:
#         new_word += char.lower()
# print(new_word)

#task6
# new_word = ""
# x = "-,:;."
# for char in str1:
#     if not char in x:
#         new_word += char
# print(new_word)

#task7
# new_text = ""
# for char in str1:
#     if char.isalpha():
#         if char == "z":
#             new_text += "a"
#         elif char == "Z":
#             new_text += "A"
#         else:
#             new_text += chr(ord(char)+1)
#     else:
#         new_text += char
# print(new_text)

#task8
# str2 = input("Enter word: ")
# isAnagram = False
# for char in str1:
#     if char.isalpha():
#         if char in str2:
#             isAnagram = True
#
# print(isAnagram)


#task9
# def shuffle_word(word):
#     if len(word) > 3:
#         middle = list(word[1:-1])
#         random.shuffle(middle)
#         return word[0] + ''.join(middle) + word[-1]
#     return word
#
#
# text = input("Enter text: ")
# words = text.split()
# shuffle_words = [shuffle_word(word) for word in words]
#
# new_sentence = ' '.join(shuffle_words)
# print(new_sentence)
#task10
# new_text = ""
# capitalize_next = True
# for char in str1:
#     if capitalize_next and char.isalpha():
#         new_text += char.upper()
#         capitalize_next = False
#     else:
#         new_text += char
#
#     if char == " ":
#         capitalize_next = True
# print(capitalize_next)


#task11
# n = int(input("Enter number of characters: "))
# for i in str1:
#     if ord(i) - n < 97:
#         print(chr(ord(i) - n + 26), end='')
#     else:
#         print(chr(ord(i) - n), end='')

#task12
# def longest_unique_lenght(s):
#     char_index = {}
#     start = 0
#     max_len = 0
#
#     for end in range(len(s)):
#         if s[end] in char_index and char_index[s[end]] >= start:
#             start = char_index[s[end]] + 1
#         char_index[s[end]] = end
#         max_len = max(max_len, end - start + 1)
#
#     return max_len
#
#
# text = input("Enter text: ")
# print(longest_unique_lenght(text))

#task13
# def are_anagrams(str1, str2):
#     return sorted(str1) == sorted(str2)


# word1 = input("Enter word: ")
# word2 = input("Enter word: ")

# if are_anagrams(word1, word2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")

#task14
# count_char = 1
# new_text = ""
# for char in range(1, len(str1)):
#     if str1[char] == str1[char - 1]:
#         count_char += 1
#     else:
#         new_text += str1[char - 1] + str(count_char)
#         count_char = 1
# new_text += str1[- 1] + str(count_char)
# print(new_text)

#task15
# permutations = [""]
# for char in str1:
#     new_permutation = []
#     for perm in permutations:
#         for i in range(len(perm)+1):
#             new_permutation.append(perm[:i] + char + perm[i:])
#     permutations = new_permutation
#
#
# for perm in permutations:
#     print(perm)