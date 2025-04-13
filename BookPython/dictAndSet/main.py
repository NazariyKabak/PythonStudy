import pickle

phonebook = {'Крис': '555-1111',
             'Кети': '555-2222',
             'Джанна': '555-3333'}


def example1(dict):
    output_file = open('phonebook.dat', 'wb')
    pickle.dump(dict, output_file)
    output_file.close()
    return output_file


def example1_1():
    input_file = open('phonebook.dat', 'rb')
    pb = pickle.load(input_file)
    print(pb)


example1_1()


def save_data(file):
    person = {}
    person["name"] = input("Enter person's name: ")
    person["age"] = int(input("Enter person's age: "))
    person["height"] = float(input("Enter person's height: "))
    pickle.dump(person, file)


def main():
    # again = 'y'
    #
    # output_file = open('info.dat', 'wb')
    #
    # while again.upper() == 'Y':
    #     save_data(output_file)
    #     again = input("Do you want to save your data? (y/n): ")
    #
    # output_file.close()
    end_of_file = False

    input_file = open('info.dat', 'rb')
    while not end_of_file:
        try:
            person = pickle.load(input_file)
            display_data(person)
        except EOFError:
            end_of_file = True

    input_file.close()


def display_data(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
    print("Height:", person["height"])
    print()


if __name__ == '__main__':
    main()
