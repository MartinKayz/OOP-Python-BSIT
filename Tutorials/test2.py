# Student Management System

# Creating the class and object in Python

class Student:
	# Class Attributes
	university = "Uganda Christian University"

	# Constructor with Instance Attributes
	def __init__(self, name, age):
		self.name = name
		self.age = age
	# Creating Methods of the class

	def study(self, book):
		return f"{self.name} is studying the {book} from the Library"

	def chilling(self, place):
		return f"{self.name} is chilling from the {place} in Mukono"

	

# instantiating the class objects

james = Student("Jim", 10)
sandra = Student("Sandra", 11)


# Accessing the class attributes
print(f"James is a student at {james.__class__.university}")


# Accessing the instance attributes
print(f"Sandra is an object with the name of {sandra.name}")


# Calling methods
print(james.study("Object Oriented Programming in Python"))

print(sandra.chilling("Casablanca"))

# Demonstrating Inheritance

class Musician(Student):
	# To inherit the attributes of the student class we call the super method
	def __init__(self):
		super().__init__("name", "age")
		self.name = "name"
		self.age = 24
		print("Musician is ready")
	
	# Defining custom methods of the Musician class
	def whoami(self):
		print("I am a musician")

	def myactivity(self):
		print("I sing songs")


# Creating more objects of the child class

isaac = Musician()

# calling methods of the parent class using the child object
isaac.study("Music in 2022")

# calling methods of the child class
isaac.myactivity()


