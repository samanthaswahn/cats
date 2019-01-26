import random
class Cat:
	def __init__(self,colors=[],weight=0,length=0,breed='',vocal=0,speed=0,hunger=0,name=''):
		self.colors = colors
		self.weight = weight
		self.length = length
		self.breed = breed
		self.vocal = vocal
		self.speed = speed
		self.hunger = hunger
		self.name = name
	
	def stats(self):
		print "Name: " + str(self.name)
		print "Colors: " + ', '.join(self.colors)
		print "Weight: " + str(self.weight)
		print "Length: " + str(self.length) + " inches"
		print "Breed: " + str(self.breed)
		print "Vocal: " + str(self.vocal)
		print "Speed: " + str(self.speed)
		print "Hunger: " + str(self.hunger)

def catMaker(numberofcats):
	#Limit to 8 cats
	if numberofcats > 8:
		print "The max number of cats is 8"
		return

	names = ["Peppermint", "Caramel", "Whiskas", "Princess", "Cinnamon", "Stinky", "Fluffy", "Purrball"]
	

	def getWeight():
		_weight = random.randint(5,20)
		if _weight > 11 and _weight <= 15:
			return str(_weight) + " lbs. = chonk"
		elif _weight > 15:
			return str(_weight) + " lbs. = ohlawdy chonk"
		else:
			return str(_weight) + " lbs. = skinny boi"
	
	def getColors(numberofColors=2):
		if numberofColors > 8:
			numberofColors = 8
		_colors = []
		colors = ["Gray", "White", "Black", "Brown", "Tan", "Peach", "Orange", "Calico"]
		for i in range(0,numberofColors):
			_colors.append(colors[i])
		return _colors

	def getBreed():
		_breeds = ["Bengal", "Siamese", "Abyssinian", "American Curl", "Scottish Fold", "American Shorthair", "Street Mutt", "Persian"]
		return _breeds[random.randint(0,7)]

	def getName():
		_names = ["Peppermint", "Caramel", "Whiskas", "Princess", "Cinnamon", "Stinky", "Fluffy", "Purrball"]
		return _names[random.randint(0,7)]

	def getHunger():
		_hunger = ["Often", "Sometimes", "Never"]
		return _hunger[random.randint(0,2)]

	def getVocal():
		_vocal = ["Loud", "Quiet", "Talky", "Squeaky"]
		return _vocal[random.randint(0,3)]

	def getLength():
		return random.randint(12,24)

	for i in range(0,numberofcats):
		Cat(weight=getWeight(),breed=getBreed(),colors=getColors(random.randint(0,7)),name=getName(),hunger=getHunger(),vocal=getVocal(), length=getLength(),speed=getLength()).stats()
		print ''
		print ''

catMaker(3)

