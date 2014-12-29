class Parent() :	# created parent class
	def __init__(self, last_name, eye_color):	# define init function
		print ("Parent Constructor Called")
		self.last_name = last_name	# assigning parameters to class variables
		self.eye_color = eye_color

billy_cyrus = Parent ("Cyrus","blue")	# passing values to parameter
print (billy_cyrus.last_name)
