class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price):
        if item in self.cart:
            self.cart[item] += price 
        else:
            self.cart[item] = price

    def remove_item(self, item):
        print("Cart after removing items:")
        if item in self.cart:
            del self.cart[item]
        else:
            print(f"Item '{item}' not found in the cart.")
        total = sum(self.cart.values())
        print("Total Updated value of your cart is :",total)


    def printCart(self):
        print("Current items in cart: ")
        total = sum(self.cart.values())
        print("Toal Value of your cart :",total)


cart = ShoppingCart()
cart.add_item("Orange", 100)
cart.add_item("Lemon", 75)
cart.add_item("Apple", 50)  
cart.add_item("Watermelon", 50)  
cart.printCart()
cart.remove_item("Orange")