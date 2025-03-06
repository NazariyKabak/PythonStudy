#task1
numbers = list(map(int, input("Enter numbers (через пробіл): ").split()))
# count = 0
# for number in numbers:
#     count += 1
# print(count)

#task2
# numbers =[int(number) for number in numbers]
# last_element = numbers.pop()
# print(last_element)

#task3
# revers_numbers = []
# while len(numbers)>0:
#     revers_numbers.append(numbers.pop())
# print(revers_numbers)

#task4
# max_num = numbers[0]
# min_num = numbers[0]
# for number in numbers:
#     number = int(number)
#     if number > max_num:
#         max_num = number
#     if number < min_num:
#         min_num = number
# print(max_num, min_num)

#task5
# sum_num = 0
# for number in numbers:
#     sum_num += int(number)
# print(sum_num)

#task6
# count_Even =0
# count_Odd =0
# for number in numbers:
#     number = int(number)
#     if number % 2 == 0:
#         count_Even += 1
#     else:
#         count_Odd += 1
# print(f"CountEven: {count_Even}", f"CountOdd: {count_Odd}")

#task7
n = int(input("Enter number: "))
# found = False
# for number in numbers:
#     number = int(number)
#     if n == number:
#         found = True
#         break
# print(found)
#task8
# x=0
# new_numbers = []
# for number in numbers:
#     number = int(number)
#     if number != n:
#         new_numbers.append(number)
# print(new_numbers)

#task9
# for i in range(len(numbers)):
#     for j in range(len(numbers)-1):
#         if numbers[j] > numbers[j+1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j+1]
#             numbers[j+1] = temp
# print(numbers)

#task10
# numbers2 = input("Enter numbers: ").split()
# # for num in numbers2:
# #     numbers.append(num)
# print(numbers)

#task11

# isUnique = True
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             isUnique = False
#             break
#     if not isUnique:
#         break
# print(isUnique)

#task12
# if len(numbers) < 2:
#     print("Недостатньо елементів")
# else:
#     max_num = max_second_num = float('-inf')
# for num in numbers: #8
#     num = int(num)
#     if num > max_num:#8>0
#         max_second_num = max_num
#         max_num = num
#     elif num > max_second_num and num != max_num:
#             max_second_num = num
#
# print(max_second_num)
# print(max_num)
#
# #task13
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(unique_numbers)
#
# #task14
# max_seq=[]
# current_seq=[numbers[0]]
# for i in range(1,len(numbers)):
#     if numbers[i] > numbers[i-1]:
#         current_seq.append(numbers[i])
#     else:
#         if len(current_seq) > len(max_seq):
#             max_seq = current_seq
#         current_seq = [numbers[i]]
# if len(current_seq) > len(max_seq):
#     max_seq = current_seq
# print("Найдовша зростаюча послідовність:", " ".join(map(str, max_seq)))

#task15
n=n%len(numbers)
for _ in range(n):
    last_element = numbers[-1]
    for index in range(len(numbers)-1, 0, -1):
        numbers[index] = numbers[index-1]
    numbers[0] = last_element
print(numbers)