class Parent() :	# created parent class
	def __init__(self, last_name, eye_color):	# define init function
		print ("Parent Constructor Called")
		self.last_name = last_name	# assigning parameters to class variables
		self.eye_color = eye_color

class Child(Parent) :	# create child class
	def __init__(self, last_name, eye_color, number_of_toys):	# define child class init function
		print("Child Constructor Called")
		Parent.__init__(self,last_name, eye_color)
		self.number_of_toys = number_of_toys

#billy_cyrus = Parent ("Cyrus","blue")	# creating instance of parent class
#print (billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "Blue", 5)	# creating instance of child class
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)
