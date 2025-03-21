products = []


def add_product(self, product):
    products.append(product)
    print(f"Added {product}")


def remove_product(self, product):
    if product in products:
        products.remove(product)
        print(f"Removed {product}")
    else:
        print("Product not found")


def calculate_total(self):
    total = 0
    for p in self.products:
        total += p.price
    return total
