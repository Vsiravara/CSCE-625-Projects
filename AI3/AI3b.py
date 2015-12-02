#Vishwas Siravara
#UIN: 623009600

import itertools
import copy
count = 0 
english_domain = [ [2, 3, 4, 5], [ "Red"], [ "Hershey", "Smarties", "Snickers"], ["OJ",  "Milk"], [ "Horse", "Zebra", "Snails", "Fox"] ]
spainaird_domain = [ [ 2, 3, 4, 5 ], ["Blue", "Green",  "Ivory" ], [ "Hershey", "Smarties", "Snickers"], ["OJ", "Milk", "Coffee"], ["Dog"] ]
norwegian_domain = [ [1], ["Yellow"], [  "Kitkat" ], ["Water"], [ "Zebra", "Fox"]]
ukranian_domain = [ [2, 3, 4, 5], [ "Blue", "Green",  "Ivory" ], ["Hershey", "Smarties"],["Tea"] ,["Horse", "Zebra", "Snails", "Fox"] ]
japenese_domain = [ [2, 3, 4, 5], [ "Blue", "Green",  "Ivory" ], ["Milkyway"], ["Milk", "Coffee"], ["Horse", "Zebra", "Fox"] ]
class Person:
	def __init__( self , name ):
		self.color = None
		self.name = name
		self.drink = None
		self.food = None
		self.animal = None
		self.number = None
		self.domain = []
	def setdomain( self, domain ):
		self.domain = domain
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
	def getdomain( self ):
		return self.domain
	def __str__( self ):
		print self.name + " " + self.color + " " + self.food + " " + self.drink + " " + str ( self.number ) + " " + self.animal 



def consistency_check( people ):
	for person in people:
		if person.getcolor() == "Blue" and person.getnumber() != 2:
			
			return False
		if person.getnumber() == 2 and person.getcolor() != "Blue":
			
			return False
		# Smarties eater owns snails
		if person.getanimal() == "Snails" and person.getfood() != "Smarties":
			
			return False
		if person.getfood() == "Smarties" and person.getanimal() != "Snails":
			
			return False
		if person.getfood() == "Snickers" and person.getdrink() != "OJ":
			
			return False
		if person.getdrink() == "OJ" and person.getfood() != "Snickers":
			
			return False
		if person.getdrink() == "Coffee" and person.getcolor() != "Green":
			
			return False
		if person.getcolor() == "Green" and person.getdrink() != "Coffee":
			
			return False
		if person.getdrink() == "Milk" and person.getnumber() != 3:
			
			return False
		if person.getnumber() == 3 and person.getdrink() != "Milk":
			
			return False
		if person.getnumber() == 2 and person.getanimal() != "Horse":
			
			return False
		if person.getanimal() == "Horse" and person.getnumber() != 2:
			
			return False
		# green house is right of ivory house
		if person.getcolor() == "Green":
			temp_list = list( people )
			temp_list.remove( person )
			for man in temp_list:
				if man.getcolor() == "Ivory" and man.getnumber()  != person.getnumber() - 1 :
					
					return False
				else:
					continue
		if person.getcolor() == "Ivory":
			temp_list = list( people )
			temp_list.remove( person )
			for man in temp_list:
				if man.getcolor() == "Green" and man.getnumber()  != person.getnumber() + 1:
					
					return False
				else:
					continue
		if person.getfood() == "Hershey":
			if person.getanimal() == "Fox":
				
				return False
			# check left neighbour and right neighbour if left or right neighbour is legal or assigned , if only one is assigned and both are legal the return true .
			left_neighbour = person.getnumber() - 1
			right_neighbour = person.getnumber() + 1
			temp_list = list( people )
			temp_list.remove( person )
			if left_neighbour < 1:
				for man in temp_list:
					if man.getnumber() == right_neighbour and man.getanimal() != "Fox":
						
						return False
			if right_neighbour > 5:
				for man in temp_list:
					if man.getnumber() == left_neighbour and man.getanimal() != "Fox":
						
						return False
			else:
				neighborleft = None
				neighborright= None
				for man in temp_list:
					if man.getnumber() == left_neighbour:
						neighborleft = man 
					elif man.getnumber() == right_neighbour:
						neighborright = man 
					else:
						continue
				if neighborright != None and neighborleft != None:
					if neighborright.getanimal() != "Fox" and neighborleft.getanimal() != "Fox":
						
						return False


		if person.getanimal() == "Fox":
			if person.getfood() == "Hershey":
				
				return False
			left_neighbour = person.getnumber() - 1
			right_neighbour = person.getnumber() + 1
			temp_list = list( people )
			temp_list.remove( person )
			if left_neighbour < 1:
				for man in temp_list:
					if man.getnumber() == right_neighbour and man.getfood() != "Hershey":
						
						return False
			if right_neighbour > 5:
				for man in temp_list:
					if man.getnumber() == left_neighbour and man.getfood() != "Hershey":
						
						return False
			else:
				neighborleft = None
				neighborright= None
				for man in temp_list:
					if man.getnumber() == left_neighbour:
						neighborleft = man 
					elif man.getnumber() == right_neighbour:
						neighborright = man 
					else:
						continue
				if neighborright != None and neighborleft != None:
					if neighborright.getfood() != "Hershey" and neighborleft.getfood() != "Hershey":
						
						return False

	return True

def counter( li ):
	count = 0
	for x in li:
		count += len( x )
	return count


english = Person("English")
english.setdomain( english_domain )
spanish = Person("Spanish")
spanish.setdomain( spainaird_domain )
norwegian = Person("Norwegian")
norwegian.setdomain( norwegian_domain )
ukranian = Person("Ukranian")
ukranian.setdomain( ukranian_domain )
japanese = Person("Japanese")
japanese.setdomain( japenese_domain )
people = [ english,spanish, norwegian, ukranian, japanese ]

def domain_values( domain ):
	return list( itertools.product( *domain) )
#should return the person with the smallest domain 
def mrv_heuristic( people ):
	temp_list = []
	for person in people:
		temp_list.append( sum( len(li) for li in person.getdomain() ))
	minDomainLen = min( x for x in temp_list )
	for person in people:
		if minDomainLen == sum( len(li) for li in person.getdomain() ):
			break
		else:
			continue
	print "Length of remaining Domain :" + str ( minDomainLen )
	return person 


#print consistency_check( people )

def printer( person ):
	print "Name :" + person.getname()
	print "House number:" + str( person.getnumber() )
	print "House Color :" + person.getcolor()
	print "Food :" + person.getfood()
	print "Drink :" + person.getdrink()
	print "Animal :" + person.getanimal()
	print " ----- "

#person = mrv_heuristic( people )
#print person.getname()
#changing people with each call and removing previously visited in visited 
def backtrack( people, visited ):
	#check for solution 
	global count
	flag = True
	for person in people:
		if person.getname() == None or person.getnumber() == None or person.getanimal() == None or person.getfood() == None or person.getdrink() == None or person.getcolor() == None:
			flag = False
		else:
			continue
	if flag:
		return people
	# choose the person with minimum remaining values 
	
	
	person = mrv_heuristic( visited )
	print "Min heuristic ( minimum values remaining ) node selected : "
	print person.getname()

	assingments = domain_values( person.getdomain() )
	for assignment in assingments:
		person.setnumber( assignment[0] )
		person.setcolor( assignment[1] )
		person.setfood( assignment[2] )
		person.setdrink( assignment[3] )
		person.setanimal( assignment[4] )
		count += 1
		if consistency_check( people ):
			
			visited.remove( person )
			temp = []
			for man in visited:
				temp.append( ( man.getdomain() , man.getname() ) ) 
			temp1 = copy.deepcopy( temp )

			for man in visited:
				
				if person.getnumber() in man.getdomain()[0]:
					man.getdomain()[0].remove( person.getnumber() )
				if person.getcolor() in man.getdomain()[1]:
					man.getdomain()[1].remove(person.getcolor() )
				if person.getfood() in man.getdomain()[2]:
					man.getdomain()[2].remove( person.getfood() )
				if person.getdrink() in man.getdomain()[3]:
					man.getdomain()[3].remove( person.getdrink() )
				if person.getanimal() in man.getdomain()[4]:
					man.getdomain()[4].remove( person.getanimal() )
				
			result = backtrack( people, visited )
			if result != None:
				return result 
			else:
				print "Backtrack"
				# need to add back the deleted domain values 
				for i in range( len(visited) ):
					for tu in temp1:
						if tu[1] == visited[i].getname():
							visited[i].setdomain( tu[0] )
						else:
							continue
					
				
				visited.append( person )
				continue

		else:
			#remove assignments of the person 
			person.setnumber( None )
			person.setcolor( None )
			person.setdrink( None )
			person.setfood( None )
			person.setanimal( None )
			continue
	return None

result = backtrack( people, list( people) )
print "---------------------------Solution---------------------- "
for man in result:
	printer( man )
print count