class Temperature:
    def __init__(self, temp):
        self.temp = temp

    def __round__(self, n=None):
        return round(self.temp, n)

    def __str__(self):
        return f"({self.temp})"