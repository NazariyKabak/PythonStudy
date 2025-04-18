class Book:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_publisher(self, publisher):
        self.publisher = publisher

    def __str__(self):
        return f"{self.title} {self.author} {self.publisher}"


