class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age



    def greet(self):
        return f'Hello {self.name}!'