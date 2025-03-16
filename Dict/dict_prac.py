#task1 Перевірити, чи два словники рівні (мають однакові ключі та значення)


def equal_dict(dict_1, dict_2):
    if dict_1 == dict_2:
        return True
    return False


#task2 Злиття двох словників без update() та |
def combine_dict(dict_1, dict_2):
    dict_3 = {**dict_1, **dict_2}
    return dict_3


#task3 Перетворити список у словник, де ключ – це індекс
def transformation_list_to_dict(list_1):
    dict_1 = {}
    for i in range(len(list_1)):
        dict_1[i] = list_1[i]
    return dict_1


# print(transformation_list_to_dict([1, 2, 3]))

#task4 Знайти слово з найбільшою частотою у тексті

def most_frequent_word(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    max_word = max(word_count, key=word_count.get)
    return max_word, word_count[max_word]


#task5 Змінити всі ключі у словнику на великі літери (upper())
def key_upper(dict):
    return {key.upper(): value for key, value in dict.items()}


print(key_upper({"a": 1, "b": 2, "c": 3}))
