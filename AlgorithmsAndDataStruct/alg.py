#task1
from collections import deque


def check_parentheses(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
    return not stack


expression = "(5+3) * (2+7)"
print(check_parentheses(expression))


#task2
def customer_queue():
    queue = deque()
    queue.append("Customer 1")
    queue.append("Customer 2")
    queue.append("Customer 3")
    while queue:
        print(f"{queue.popleft()} is being served")


customer_queue()


#task3
def bfs(graph, start, target):
    queue = deque([start])
    visited = set()
    path = {start: [start]}

    while queue:
        node = queue.popleft()
        if node == target:
            return path[node]

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                path[neighbor] = path[node] + [neighbor]

    return None


#task4
def count_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


text = "hello world"
print(count_char(text))


#task5
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))


#task6
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort(arr))


#task7
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    sorted_arr = []
    while left and right:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    sorted_arr.extend(left or right)
    return sorted_arr


print(merge_sort(arr))


#task8
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


#task9
def knapsack(weight, values, W):
    n = len(weight)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weight[i - 1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]


weights = [2, 3, 4, 5]  # Ваги предметів
values = [3, 4, 5, 6]  # Вартість предметів
W = 5
print(knapsack(weights, values, W))

