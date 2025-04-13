def main():
    # outfile = open("philosophers.txt", "w")
    #
    # outfile.write("Джон Люкк\n")
    # outfile.write("Девід Х'юм\n")
    # outfile.write("Едмунд Берк\n")
    # infile = open("philosophers.txt", 'r')
    # line1 = infile.readline()
    # line2 = infile.readline()
    # line3 = infile.readline()
    #
    # infile.close()
    #
    # print(line1)
    # print(line2)
    # print(line3)
    # write_in_file()
    read_in_file()
    # write_in_file_num()


def write_in_file():
    print("Write 3 names: ")

    name1 = input("Name: ")
    name2 = input("Name: ")
    name3 = input("Name: ")

    my_file = open("friends.txt", 'w')
    my_file.write(name1 + '\n')
    my_file.write(name2 + '\n')
    my_file.write(name3 + '\n')

    my_file.close()
    print("Complete.")


def read_in_file():
    my_file = open("friends.txt", 'r')
    # line = my_file.readline()
    for line in my_file:
        print(line)
    my_file.close()


def write_in_file_num():
    my_file = open("nums.txt", 'w')
    for i in range(1, 11):
        my_file.write(str(i) + '\n')
    my_file.close()


if __name__ == '__main__':
    main()
