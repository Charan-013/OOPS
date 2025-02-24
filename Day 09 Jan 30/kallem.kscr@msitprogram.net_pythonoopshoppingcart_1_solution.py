class Item:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.quantity = 0

    def initilize(self, item_Name, item_Price, item_Quantity):
        self.name = item_Name
        self.price = item_Price
        self.quantity = item_Quantity

    def update_quantity(self, item_Quantity):
        self.quantity = item_Quantity


class Cart:
    def __init__(self):
        self.items = {}
        self.total = 0

    def add_Item(self, item_Name, item_Price, item_Quantity):
        if item_Name not in self.items:
            self.items[item_Name] = [item_Price, item_Quantity]
            print(f"Item added to cart: {item_Name}")
        else:
            self.items[item_Name][1] += item_Quantity
            # print(f"Item added to cart: {item_Name}")
            print(f"Quantity updated for item: {item_Name}")
        self.calculate_Total_Amount()

        # print(self.items)

    def remove_Item(self, item_Name):
        new_items = {}
        for k, v in self.items.items():
            if k == item_Name:
                print(f"Item removed from cart: {item_Name}")
                continue
            elif k != item_Name:
                new_items[k] = v
        if item_Name not in self.items:
            print(f"Item not found in the cart: {item_Name}")
        self.items = new_items
        # print(self.items)
        self.calculate_Total_Amount()

    def display_Items(self):
        if not self.items:
            print(f"Cart is empty.")
        else:
            # Items in Cart:
            # Camera - $812.00 × 2 = $1624.00
            # Charger - $985.00 × 4 = $3940.00
            # Total Amount: $5564.00
            print(f"Items in Cart:")
            for k, v in self.items.items():
                print(f"{k} - ${v[0]:.2f} × {v[1]} = ${v[0]*v[1]:.2f}")
            # print(self.total)
            self.calculate_Total_Amount()
            print(f"Total Amount: ${self.total:.2f}")

    def calculate_Total_Amount(self):
        total = 0
        for k, v in self.items.items():
            total += v[0] * v[1]
        self.total = total
        # print(f"Total Amount: ${self.total:.2f}")

    def apply_Discount(self):
        new_total = self.total - (self.total * 0.1)
        print(f"Total after 10% discount: ${new_total:.2f}")

    def apply_Coupon(self):
        pass

    def checkOut(self):
        pass


def e_shopping():
    shopping = Cart()
    while True:
        try:
            inp = input().strip()

            if not inp:
                break

            if inp.startswith("Add Item "):
                inp = inp.split("Add Item ")
                item_Name, item_Price, item_Quantity = inp[1].split(", ")
                item_Price = float(item_Price)
                item_Quantity = int(item_Quantity)
                # print(item_Name)
                # print(item_Price)
                # print(item_Quantity)
                shopping.add_Item(item_Name, item_Price, item_Quantity)

            elif inp.startswith("Remove Item "):
                inp = inp.split("Remove Item ")
                item_Name = inp[1]
                # print(item_Name)
                shopping.remove_Item(item_Name)

            elif inp.startswith("DisplayCart"):
                shopping.display_Items()

            elif inp.startswith("ApplyDiscount"):
                shopping.apply_Discount()
        except EOFError:
            break


e_shopping()
