class Insect: #superclass
	def __init__(self, species):
		self.__species = species
	def set_species(self, species):
		self.__species = species
	def get_species(self):
		return self.__species
	def get_habit(self):
		self.__habit = 'I love to fly '
		return self.__habit
	def __str__(self):
		return 'I am a(n) ' + self.get_species() + '. '+\
		'My hobby is: ' + self.get_habit()
	
class Mosquito(Insect):
	def __init__(self, species):
		Insect.__init__(self, species) #inherited from super class

	def get_habit(self):
		self.__hobby = 'I love to suck human'
		return self.__hobby
class Bug(Insect):
	def __init__(self, species):
		Insect.__init__(self, species)

	def get_habit(self):
		self.__passion = 'I love to suck plant sap'
		return self.__passion
