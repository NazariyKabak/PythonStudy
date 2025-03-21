class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        new_coeffs = [a + b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(new_coeffs)

    def __sub__(self, other):
        new_coeffs = [a - b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(new_coeffs)

    def __mul__(self, other):
        new_coeffs = [a * other for a in self.coefficients]
        return Polynomial(new_coeffs)

    def __str__(self):
        return " + ".join(f"{coef}x^{i}" for i, coef in enumerate(reversed(self.coefficients)))