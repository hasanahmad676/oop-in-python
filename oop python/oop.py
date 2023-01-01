class product:
    def __init__(self, name, code,unit_price):
        self.name = name
        self.code = code
        self.unit_price = unit_price
    quantity = int(input("Enter the quantity: "))
    def total_price():
        total_price = quantity * unit_price
        print("The total price is: ", total_price)
        
        
class discount:
    def __init__(self, discount_rate, discount_type):
        self.discount_rate = discount_rate
        self.discount_type = discount_type
    def discount_calculator():
        discount= product.unit_price*discount_rate
        if discount_type == "percentage":
            print("Discount is: ",discount)
        elif discount_type == "amount":
            print("Discount is: ",discount)
        else:
            print("Invalid discount type")
p1 = product("Pen", "P001", 10)
t1=discount(10, "percentage")
t2=discount(10, "amount")
t3=discount(10, "invalid")
p=product.total_price()
        
        
    
