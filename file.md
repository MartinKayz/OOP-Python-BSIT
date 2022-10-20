# STORE MANAGEMENT SYSTEM: OOP Tutorial 1


### Keeping a track of all item details

for example: 
- Item is Sugar
- Price of Sugar is 3000
- There are 5 kg of sugar in the store
- If sold, the price total of all the sugar is 5*3000

### How do we represent this the old fashioned way

```

item1 = "sugar"
item1_price = 3000
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

```

### What are the types of this data in Python3

```
print(f'Item1 is of type {type(item1)}')
print(f'item1_price is of type {type(item1_price)}')
print(f'Item1_quantity is of type {type(item1_quantity)}')
print(f'item1_price_total is of type {type(item1_price_total)}')

```

### How can we create our own data types in Python

#### We make `classes` 

### How to make a class

``` 
class Item:
    pass

```
### How to make instances of a class

```
item1 = Item()

```

*What is the type of item1?*

`print(type(item1))`


**What are classes and Objects?**

A class is like a blue print for a house. Sort of a design used to make a house

An object is an instance of a class, it is derived from a class definition

*Objects have data and behaviours*

---

**Data of Objects**

Each object ideally as data that related to it, what we normally refer to as attributes in the Database world

> In general, once we create an object, we can associate data to that object for example

```
item1.name = "Sugar"
item1.price = 3000
item1.quantity = 5
```

**Behaviours of objects**

As we have already seen, once an object has been defined, it has the right to data then ...

2. It has the right to life ( Action )

### Methods (Functions that live inside a class)

Modify our class definition to add some methods of items in your store

```
class Item:
    def calculate_total_price(self):
        pass
```

> **Rule of Thumb**: All methods in a class must have atleast the **self** parameter

*Modifying our code again*

```
def calculate_total_price(self, x, y):
    return x * y

```

Coming back to our code ( main block )

`Lets call our newly defined method`

```
print(item1.calculate_total_price(item1.price, item1.quantity))
```

## Do Cool Things Always

Each time you have a class defined, and you create an instance of that class, the `__init__` method is called, whether you have defined it or not

>Let us experiment and see, 

 ```
 class Item:
    
    def __init__(self):
        print("I am now created")



item1 = Item()
item2 = Item()


```

**Defining data of objects the cool way**

> Use the **init** method

```
    def __init__(self, name):
        print(f"I {name} am now created")
```
**Dynamically assigning data to objects at creation**

Since the *self* parameter is always passed to any method, it means that the actual object calling the method is passed in the method as the first argument

So with this trick under our belt, we can assign the data passed as arguments at object instantiation to the actual object being created

for example

```
class Item:
    ...
    ...
    ...
    def __init__(self, name):
        self.name = name



item1 = Item("Sugar")

print(item1.name)
```

> **Rule of Thumb** Once you define your `__init__` method to accept more data(parameters), you **MUST** state that data when instantiating an object, otherwise we are bound for errors

*let us complete our __init__ method*

```
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price= price
        self.quantity = quantity

        # Printing summary of data created
        print(f"An instance called {self.name} has been created")

item1 = Item("Sugar", 3000, 4)
item2 = Item("Blueband", 2500, 2)

print(item1.name)
print(item2.quantity)
print(item1.price)
print(item2.name)
```

**It is possible to also supply default values to parameters**

e.g 
```
    ...
    ...
    ...
    def __init__(self, name, price, quantity = 0):
        ...
        ...
        ...
```

In the above case, you can instantiate an object without supplying a value for quantity since it already has a default value

Supplying a value for a parameter with a default value simply overrides it

```
    ....
    ...
    ...
    
item3 = Item("Matchbox", 200)

```

**Try Some Hacking on the Class**

```
item1 = Item("Sugar", "100", 1)
item2 = Item("Laptop", "1000", 3)

```

The code above behaves in unexpected ways as it multiplies the string with integer to give us a certain kind of code

**How to validate data tyoes of attributes**

```
    def __init__(self, name:str, price:int):
        ...
        ...
        ...
```

**Validate the recieved values**

``` 
def __init__(self, ...):
    ...
    ...
    ...
    assert price >= 0
    assert quantity >= 0
```

**Making our own Assert error messages**

```
def __init__(self, ...):
    assert price >= 0, f"Price {price} is not greater than Zero!"
    




