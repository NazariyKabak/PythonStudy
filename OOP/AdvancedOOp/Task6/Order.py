class Order:
    def __init__(self, cart, discount):
        self.cart = cart
        self.discount = discount

    def checkout(self):
        total = self.cart.calculate_total()
        final_price = self.discount.get_discount(total)
        print(f"💰 Загальна сума: {total} грн")
        print(f"🎉 Після знижки: {final_price:.2f} грн")