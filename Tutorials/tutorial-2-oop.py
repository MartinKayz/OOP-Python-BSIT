print("Student Management System")

class Student:

    def __init__(self, name, age, access_no):
        self.name = name
        self.age = age
        self.access_no = access_no
        print(f"A new Student instance {self.name} of the Student class has been created")



# Creating objects of the students

sarah = Student("Sarah", "cow", "a34805")
james = Student("James", 34, "A34353")

print(sarah.access_no)
print(sarah.age)

# Validating the data given 

