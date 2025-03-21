class CustomList:
    def __init__(self):
        self.arr = []

    def __contains__(self, item):
        return item in self.arr

    def __str__(self):
        return f"({self.arr})"