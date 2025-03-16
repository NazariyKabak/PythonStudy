#task1
arr = [1, 2, 3]
tuple_arr = tuple(arr)
# print(tuple_arr)

#task2
tupl_1 = (1, 2, 3)
tupl_2 = (4, 5, 6)
tupl_3 = ()
for i in tupl_1:
    tupl_3 += i,
for i in tupl_2:
    tupl_3 += i,


# print(tupl_3)

#task3

def check_common_elements(tuple_1, tuple_2):
    for num in tuple_1:
        if num in tuple_2:
            print(num)


check_common_elements((1, 3, 65), (3, 4, 1))


#task4
def delete_element(tuple_1, n):
    new_tuple = []
    for num in tuple_1:
        if num != n:
            new_tuple.append(num)
    return tuple(new_tuple)


#task5
def set_tuple(tuple_1, tuple_2):
    return set(tuple_1).issubset(set(tuple_2))
