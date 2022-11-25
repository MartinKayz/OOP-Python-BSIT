class Student:

    def __init__(self, name, course, access_no):
        self.name = name
        self.course = course
        self.access_no = access_no
        # print("Hey I have come to life")
    
    def eat(self):
        print("I am eating")

    def drink(self):
        print("I am drinking")

    def sleep(self):
        print("I am sleeping")
    
    def wake(self):
        print(f" am Waking up")


    def __str__(self):
            return f"Hey this is {self.name} and my access number is {self.access_no} and my course is  {self.course}"


jim  = Student("Jim James", "BSIT", "A95623")

# print(jim.access_no)

Laura = Student("Laura n", "CS", "A9854")
print(Laura.access_no)

print(jim)
print(Laura)
desire = Student("Desire", "SOcial", "a45224")
print(desire)

