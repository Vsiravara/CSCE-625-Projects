import itertools
DOMAIN = [ [ 1 ,2 ,3 ,4,5 ], [ "English", "Spanish", "Norwegian", "Ukranian", "Japanese" ], [ "Red", "Green", "Ivory", "Yellow", "Blue" ], [ "Hershey", "Kitkat", "Smarties","Snickers", "Milkyway" ], [ "OJ", "Tea", "Coffee", "Milk", "Water" ], [ "Snails", "Horse", "Zebra", "Fox", "Dog" ]]
class Person:
	def __init__( self, number, name ):
		self.color = None
		self.name = None
		self.drink = None
		self.food = None
		self.animal = None
		self.number = None
	def setcolor( self , color ):
		self.color = color
	def setname( self, name ):
		self.name = name
	def setdrink( self, drink ):
		self.drink = drink 
	def setfood( self, food ):
		self.food = food
	def setanimal( self, animal ):
		self.animal = animal 
	def setnumber(self, number):
		self.number = number 
	def getcolor( self ):
		return self.color
	def getname( self ):
		return self.name
	def getdrink( self ):
		return self.drink
	def getfood( self ):
		return self.food
	def getanimal(self ):
		return self.animal 
	def getnumber(self ):
		return self.number
domain = list( itertools.product( *DOMAIN ))
print len( domain )

houses = [ House( 0 ), House( 1 ), House( 2 ), House( 3 ), House( 4 )]

def consistency_check( houses ):
	for house in houses:
		# English lives in red house 
		if house.getperson() == "English" and house.getcolor() != "Red":
			return False
		if house.getcolor() == "Red" and house.getperson() != "English":
			return False
		# Spainaird owns dog
		if house.getperson() == "Spanish" and house.getanimal() != "Dog":
			return False
		if house.getanimal() == "Dog" and house.getperson() != "Spanish":
			return False
		# Norwegian lives in the leftmost house
		if house.getperson() == "Norwegian" and house.getnumber() != 0:
			return False
		if house.getnumber() == 0 and house.getperson() != "Norwegian":
			return False
		# green house cannot be the first house since it has a neighbour on the left
		if house.getcolor() == "Green" and house.getnumber() == 0:
			return False
		# left of the green house is the ivory house 
		if house.getcolor() == "Green" and ( houses[ house.getnumber() - 1 ].getcolor() != "Ivory" or house[ house.getnumber() - 1].getcolor() != None ):
			return False
		# Ivory house cannot be the rightmost house 
		if house.getcolor() == "Ivory" and house.getnumber() == 4:
			return False
		# Ivory house has to be to the left of the Green house 
		if house.getcolor() == "Ivory" and ( houses[ house.getnumber() + 1 ].getcolor() != "Green" or house[ house.getnumber() + 1].getcolor() != None ):
			return False 
		# Kit kats are eaten in the yellow house
		if house.getcolor() == "Yellow" and house.getfood() != "Kitkat":
			return False
		if house.getfood() == "Kitkat" and house.getcolor() != "Yellow":
			return False
		# Smarties eater owns Snails
		if house.getfood() == "Smarties" and house.getanimal() != "Snails":
			return False
		if house.getanimal() == "Snails" and house.getfood() != "Smarties":
			return False
		# Snickers eater drinks OJ
		if house.getfood() == "Snickers" and house.getdrink() != "OJ":
			return False
		if house.getdrink() == "OJ" and house.getfood() != "Snickers":
			return False
		# Ukranian drinks tea
	 	if house.getperson() == "Ukranian" and house.getdrink() != "Tea":
	 		return False
	 	if house.getdrink() == "Tea" and house.getperson() != "Ukranian":
	 		return False
	 	#Japanese eats milky ways
	 	if house.getperson() == "Japanese" and house.getfood() != "Milkyway":
	 		return False
	 	if house.getfood() == "Milkyway" and house.getperson() != "Japanese":
	 		return False
	 	# coffee is drunk in the Green house
	 	if house.getcolor() == "Green" and house.getdrink() != "Coffee":
	 		return False

	 	if house.getdrink() == "Coffee" and house.getcolor() != "Green":
	 		return False
	 	# milk is drunk in the middle house ( 3 is the middle house )
	 	if house.getnumber() == 2 and house.getdrink() != "Milk":
	 		return False
	 	if house.getdrink() == "Milk" and house.getnumber() != 2:
	 		return False
	 	#the man who eats Hershey's leves in the house next to fox
	 	if house.getfood() == "Hershey":
	 		# hershey man cannot own a fox
	 		if house.getanimal() == "Fox":
	 			return False
	 		# if he lives in the leftmost house right neighbour should be fox 
	 		if house.getnumber() == 0 and ( houses[1].getanimal() != "Fox" or houses[1].getanimal() != None ):
	 			return False
	 		if house.getnumber == 4 and ( houses[3].getanimal() != "Fox" or houses[4].getanimal() != None ):
	 			return False
	 		#if it is not in the extremes check both neighbours for fox
	 		if ( houses[ house.getnumber() - 1].getanimal() != "Fox" or houses[ house.getnumber() - 1 ].getanimal() != None ) or ( houses[ house.getnumber() + 1].getanimal() != "Fox" or houses[ house.getnumber() + 1 ].getanimal() != None ) :
	 			return False
	 	# man with fox cannot eat Hershey bar
	 	if house.animal() == "Fox":
	 		if house.getfood() == "Hershey":
	 			return False
	 		if house.getnumber() == 0 and ( houses[1].getfood() != "Hershey" or houses[1].getfood() != None ):
	 			return False
	 		if house.getnumber() == 4 and ( houses[3].getfood() != "Hershey" or houses[3].getfood() != None ):
	 			return False
	 		#if it is not in the extremes check both neighbours for Hershey
	 		if ( houses[ house.getnumber() - 1].getfood() != "Hershey" or houses[ house.getnumber() - 1 ].getfood() != None ) or ( houses[ house.getnumber() + 1].getfood() != "Hershey" or houses[ house.getnumber() + 1 ].getfood() != None ) :
	 			return False

	 	if house.getperson() == "Norwegian":
	 		if house.getcolor() == "Blue":
	 			return False
	 		if houses[ house.getnumber() + 1 ].getcolor() != "Blue" or houses[ house.getnumber() + 1 ].getcolor() != None:
	 			return False
	 	if house.getcolor() == "Blue":
	 		if house.getperson() == "Norwegian":
	 			return False
	 		if house.getnumber() != 1:
	 			return False
	 		if houses[ house.getnumber() - 1].getperson() != "Norwegian" or houses[ house.getnumber() - 1].getperson() != "None":
	 			return False
	 	# kit kats are eaten next to horse house
	 	if house.getfood() == "Kitkat":
	 		if house.getanimal() == "Horse":
	 			return False
	 		if ( house.getnumber() == 0 and houses[1].getanimal() != "Horse" ) or ( house.getnumber() == 0 and houses[1].getanimal() != "None" ):
	 			return False
	 		if ( house.getnumber() == 4 and houses[3].getanimal() != "Horse" ) or ( house.getnumber() == 4 and houses[3].getanimal() != "None" ):
	 			return False




	 		
	return True
print consistency_check( houses )




