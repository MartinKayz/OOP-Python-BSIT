import numbers
# from turtle import numinput


print("Store Management System")

# item1 = "Phone"
# item1_price = 300000
# item1_quantity = 100

# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))


class Item:
    # Adding Behaviour to the objects
    def __init__(self,name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        print("Hey, I have been created!")

    def calculate_discount(self, x, y):
        return x * y

    
    def __repr__(self):
        return f"Item ('{self.name}', {self.price}, {self.quantity})"


car = Item("Tesla", 100, 5000)
gun = Item("M16", 30, 4000)

# print(car.calculate_discount("100", 8))
# Make sure the user enters only integers for the above method call



# phone = Item()
# phone.name = "Itel6"
# phone.version = "Andriod 12"
# phone.price = 2000

# earphones = Item()
# earphones.price = 1000
# calling methods of class

# print(phone.calculate_discount(0.8, phone.price))
# print(earphones.calculate_discount(0.5, earphones.price))


# # print(type(phone))
# print(phone.name)
# print(phone.price)
# print(phone.version)





