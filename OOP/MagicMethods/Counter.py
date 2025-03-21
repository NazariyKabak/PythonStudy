from OOP.MagicMethods.Money import Money


class Counter:
    def __init__(self, c):
        self.c = c

    def __len__(self):
        return len(self.c)

