import logging


with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
    
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())


with open('example.txt', 'w') as file:
    file.write("I`m 22 year old.")

lines = ["Java\n", "Python\n", "Go\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)


logging.basicConfig(level=logging.DEBUG, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")