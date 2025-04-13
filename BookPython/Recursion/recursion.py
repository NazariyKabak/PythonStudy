#task1


def traffic_sign(n):
    if n == 0:
        return 0
    else:
        print('Не паркуватись')
        return traffic_sign(n - 1)


#task1
def recursion_print(n):
    if n == 0:
        return 0
    else:
        recursion_print(n - 1)
        print(n)


# recursion_print(10)


#task2
def task2(x, y):
    if x == 1:
        return y
    else:
        return y + task2(x - 1, y)


# print(task2(7, 4))


#task3
def task3(n):
    if n == 0:
        return
    task3(n - 1)
    print("*" * n)


# print(task3(5))


#task4
def task4(arr):
    # max_nums = arr[0]
    if len(arr) == 1:
        return arr[0]
    else:
        max_nums = task4(arr[1:])

        if arr[0] > max_nums:
            return arr[0]
        else:
            return max_nums


nums = [1, 8, 10, 4, 5]


# print(task4(nums))


#task5
def task5(arr):
    sum_nums = 0
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + task5(arr[1:])


# print(task5(nums))


#task6
def task6(n):
    if n == 0:
        return 0
    else:
        return n + task6(n - 1)


print(task6(10))


#task7
def task7(x, y):
    if x == 1:
        return y
    else:
        return y * task7(x - 1, y)


print(task7(2, 3))


#task8
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(0, 5))
print(ackermann(1, 2))  # 4
print(ackermann(2, 2))  # 7
print(ackermann(3, 2))
