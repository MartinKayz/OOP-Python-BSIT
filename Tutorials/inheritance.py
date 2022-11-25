class Student:
	def __init__(self,regno,name,age):
		self.regno=regno
		self.name=name
		self.age=age

	def Study(self):
		return "Iam studying"
	def Play (self):
		return "Iam playing"
	def Discuss (self):
		return "I am Discussing"
	def __str__(self):
		return f"My name is {self.name}"
	

class NetworkAdmin(Student):
	def __init__(self,regno, name, age):
		super().__init__(regno,name,age)

#      def __str__(self):
#	      return f"Name:{self.name}\n Age:{self.age\n Regno:{self.regno}"
student1=NetworkAdmin("S18B34/132", "sAIDI", 30)
print(student1)






