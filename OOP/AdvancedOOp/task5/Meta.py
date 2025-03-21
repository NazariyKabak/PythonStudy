class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Створюється клас {name}")
        dct["created_by"] = "Python"
        return super().__new__(cls, name, bases, dct)

