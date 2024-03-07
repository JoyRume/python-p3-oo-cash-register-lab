class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []

    def add_item(self, title, price, qty=1):
        self.total += price * qty
        for _ in range(qty):
            self.items.append(title)
        self.transactions.append((title, price * qty))

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total - (self.total * self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print('There is no discount to apply.')

    def void_last_transaction(self):
        if self.transactions:
            last_item, last_price = self.transactions.pop()
            self.total -= last_price
            print(f"Last transaction for {last_item} with price {last_price} has been voided.")
        else:
            print("There are no transactions to void.")
