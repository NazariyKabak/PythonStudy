#task1


numbers = list(map(int, input("Enter numbers (через пробіл): ").split()))
t_numbers = tuple(numbers)
count = 0
for _ in t_numbers:
    count += 1
print(count)

#task2

# numbers2 = list(t_numbers)
# numbers2 = [int(number) for number in numbers2]
# last_element = numbers2.pop()
# print(last_element)

#task3
# new_numbers = ()
# for i in range(len(t_numbers) - 1, -1, -1):
#     new_numbers += (t_numbers[i],)
# print(new_numbers)
#
# #task4
# min_num = max_num = t_numbers[0]
# for num in t_numbers:
#     if min_num > num:
#         min_num = num
#     if max_num < num:
#         max_num = num
#
# print(min_num, max_num)

#task5

# sum_el = 0
# for num in t_numbers:
#     sum_el += num
#
# print(sum_el)

#task6
# num_even = 0
# num_odd = 0
# for num in t_numbers:
#     if num % 2 == 0:
#         num_even += 1
#     else:
#         num_odd += 1
#
# print(num_even, num_odd)

#task7
n = int(input("Enter number: "))
# is_in_tuple = False
# for num in t_numbers:
#     if num == n:
#         is_in_tuple = True
#         break
#
# print(is_in_tuple)

#task8
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
#
# tuple3 = tuple1+tuple2
# print(tuple3)

#task9
# count_numbers = 0
# for num in t_numbers:
#     if num == n:
#         count_numbers += 1
#
# print(count_numbers)
#task10
# isUnique = True
# for i in range(len(t_numbers)):
#     for j in range(i+1, len(t_numbers)):
#         if t_numbers[i] == t_numbers[j]:
#             isUnique = False
#             break
#     if not isUnique:
#         break
# print(isUnique)

#task11
# if len(t_numbers) < 2:
#     print("Недостатньо елементів")
#
# max_num = 0
# max_second_num = 0
# for num in t_numbers:
#     if num > max_num:
#         max_second_num = max_num
#         max_num = num
#     elif max_second_num < num != max_num:
#         max_second_num = num
# print(max_second_num)

#task12
# unique_numbers = ()
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers += (num,)
#
# print(unique_numbers)

#task13
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

#task14
t_numbers_list = list(t_numbers)
n = n % len(t_numbers_list)
for _ in range(n):
    last_element = t_numbers_list[-1]
    for i in range(len(t_numbers_list) - 1, 0, -1):
        t_numbers_list[i] = t_numbers_list[i - 1]
    t_numbers_list[0] = last_element
print(t_numbers_list)
