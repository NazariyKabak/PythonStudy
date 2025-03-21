class CustomDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data.get(key, "Немає такого ключа!")

    def __setitem__(self, key, value):
        self.data[key] = value

    def __str__(self):
        return str(self.data)
