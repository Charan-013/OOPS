class MenuItem:
    def __init__(self,itemID,name,price):
        self.itemID = itemID
        self.name = name
        self.price = price

    def getItemDEtails(self):
        return f"{self.itemID} {self.name} {self.price}"

class Order:
    def __init__(self,orderID,items,tableNNumber):
        self.orderID = orderID
        self.items = items
        self.tableNumber = tableNNumber
    
    def addItem(self,item):
        self.items.append(item)
    
    def removeItem(self,itemID):
        for ele in self.items:
            if ele.itemID == itemID:
                del ele
                return True
        return False

    def calculateTotal(self):
        total = 0
        for ele in self.items:
            total += ele.price
        return total
    
class OrderManager:
    def __init__(self,orders):
        self.orders = orders
    
    def createOrder(self,order):
        self.orders.append(order)

    def cancelOrder(self,orderID):
        for ele in self.orders:
            if ele.orderID == orderID:
                del ele
                return True
        return False
        
    def getOrder(self,orderID):
        for ele in self.orders:
            if ele.orderID == orderID:
                return ele
    


def main():
    # Create menu items
    item1 = MenuItem(1, "Burger", 8.5)
    item2 = MenuItem(2, "Fries", 3.0)
    item3 = MenuItem(3, "Soda", 2.0)
    # Create an order and add items
    order = Order(101, [], 5)
    order.addItem(item1)
    order.addItem(item2)
    order.addItem(item3)
    total = order.calculateTotal()
    print("Calculated total:", total)
    # Remove an item and recalc total

    removed = order.removeItem(2)
    print("Item 2 removed:", removed)
    print("New total after removal:", order.calculateTotal())
    # Test OrderManager functionality
    om = OrderManager([])
    om.createOrder(order)
    retrieved_order = om.getOrder(101)
    print("Retrieved order for table", retrieved_order.tableNumber)
    cancelled = om.cancelOrder(101)
    print("Order cancellation status:", cancelled)
if __name__ == '__main__':
    main()