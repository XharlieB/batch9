class Alumno:
	name = ''
	lastName = ''
	cinta = ''
	edad = ''

	def __init__(self, name, lastName, cinta, edad):
		self.name = name
		self.lastName = lastName
		self.cinta = cinta
		self.edad = edad
	def getFullName(self):
		return '{0} {1}'.format(self.name, self.lastName)
	def getFullNameCinta(self):
		return '{0} {1} esta en la cinta {2}'.format(self.name, self.lastName, self.cinta)
	def getFullNameCintaEdad(self):
		return '{0} {1} esta en la cinta {2} y tiene {3} años'.format(self.name, self.lastName, self.cinta, self.edad)
	

