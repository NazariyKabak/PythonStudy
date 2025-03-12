# todos = []
#
# while True:
#     user_action = input("Type add, show, edit or exit: ")
#     match user_action:
#         case "add":
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case "show":
#             for i in todos:
#                 print(i)
#         case "edit":
#             index = int(input("Enter a index: "))
#             new_element = input("Enter new element: ")
#             todos[index] = new_element
#         case "exit":
#             break


filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]
for filename in filenames:
    for i in filename:
        if i == " ":
            i = "-"

print(filenames)