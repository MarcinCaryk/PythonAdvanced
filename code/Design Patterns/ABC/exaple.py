from abc import ABC, abstractmethod

class Polygon(ABC):
	def __init__(self, sides):
		self.sides = sides

	@abstractmethod
	def noofsides(self):
		'''Returned information how many squares have
		:param sides
		'''
		pass


class Triangle(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have {} sides".format(self.sides))

class Pentagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have {} sides".format(self.sides))

class Hexagon(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have {} sides".format(self.sides))

class Quadrilateral(Polygon):

	# overriding abstract method
	def noofsides(self):
		print("I have {} sides".format(self.sides))

# Driver code
# a = Polygon(3)
# a.noofsides()

R = Triangle(3)
R.noofsides()

K = Quadrilateral(4)
K.noofsides()

R = Pentagon(5)
R.noofsides()

K = Hexagon(6)
K.noofsides()
