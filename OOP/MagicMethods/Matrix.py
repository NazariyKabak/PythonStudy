from pygments.lexers import j


class Matrix:
    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Matrix must have same dimensions")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix must have same dimensions")
        new_data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(new_data)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix must have same dimensions")
        new_data = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(new_data)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_data = [[self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(new_data)
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Matrix must have same dimensions")
            new_data = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)]
                        for i in range(self.rows)]
            return Matrix(new_data)
        else:
            raise TypeError("Matrix must have same dimensions")

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])