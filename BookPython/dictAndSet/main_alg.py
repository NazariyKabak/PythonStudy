import pickle

#task1
dict_1 = {"a": 1,
          "b": 2,
          "c": 3}

#task2
dict_2 = dict()
dict2_2 = {}

#task3
dct = {"Джеймс": 22, "Джим": 28}
if "Джеймс" in dct:
    print(dct["Джеймс"])

#task4
if "Джим" in dct:
    del dct["Джим"]
print(dct)

#task5
set_1 = {3, 20, 54, 40}
print(set_1)

#task6
set_2 = {3, 54, 65, 1, 3}
set_3 = set_1.union(set_2)
print(set_3)

#task7 елементи знаходяться одночасно в двох множинах

set_4 = set_1.intersection(set_2)
print(set_4)

#task8
set_5 = set_1.difference(set_2)
print(set_5)

#task9
set_6 = set_2.difference(set_1)
print(set_6)

#task10
set_7 = set_1.symmetric_difference(set_2)
print(set_7)

#task11
numbers = [1, 2, 3, 4, 5]
dict_11 = dict()

for number in numbers:
    dict_11[number] = number * 10

print(dict_11)

#task12
test_averages = {"Джанель": 98,
                 "Сем": 87,
                 "Дженнивер": 92,
                 "Томас": 74,
                 "Салли": 89,
                 "Зеб": 84}

high_scores = dict()

for key, value in test_averages.items():
    if value >= 90:
        high_scores[key] = value

print(high_scores)


def save_file(dct):
    input_file = open("mydata.dat", "wb")
    pickle.dump(dct, input_file)
    input_file.close()


# save_file(dct)

def load_file():
    output_file = open("mydata.dat", "rb")
    data = pickle.load(output_file)
    print(data)


load_file()
