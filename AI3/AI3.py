#Vishwas Siravara
#UIN: 623009600
import itertools
JOBS = [ "Nurse", "Teacher", "Police", "Guard", "Clerk", "Chef", "Actor", "Boxer" ]
class Person:
	def __init__( self , name, gender ):
		self.jobs = []
		self.gender = gender
		self.name = name 

	def getjob( self ):
		return self.jobs

	def getgender( self ):
		return self.gender

	def setjob( self , job1, job2 ):
		self.jobs = []
		self.jobs.append( job1 )
		self.jobs.append( job2 )

	def getjob( self ):
		return self.jobs

	def getname( self ):
		return self.name
	def removejob( self ):
		self.jobs = []

	def __str__( self ):
		pass
people = [  Person("Thelma", "F"), Person("Steve", "M"), Person("Pete", "M"), Person("Roberta", "F") ]

def domain_values( domain ):
	return list ( itertools.combinations( domain, 2	) )

def consistency_checker( person ):
	jobs = list ( person.getjob() )
	if "Chef" in jobs and "Police" in jobs:
		return False

	if person.getname() == "Roberta":
		if  "Nurse" in jobs or "Boxer" in jobs or "Chef" in jobs or "Police" in jobs or "Actor" in jobs or "Clerk" in jobs:
			return False

	elif person.getname() == "Thelma":
		if "Actor" in jobs or "Clerk" in jobs or "Nurse" in jobs:
			return False

	elif person.getname() == "Steve":
		if "Chef" in jobs:
			return False
	else:
		if "Nurse" in jobs or "Teacher" in jobs or "Police" in jobs or "Chef" in jobs:
			return False 

	return True

def backtrack( people , domain ):
	#check if solution
	if len( domain ) == 0:
		#print 1
		return people
    #choose an unassigned variable
	for person in people:
		if person.getjob() == []:
			break 
	assignments = domain_values( domain )
	for jobs in assignments:
		#print person.getname() 
		#print person.getjob()
		#print jobs
		person.setjob( jobs[0], jobs[1] )
		if consistency_checker( person ):
			# remove the 2 jobs from the domain 
			#print person.getname()
			#print person.getjob()
			newdomain = list( domain )
			newdomain.remove( jobs[0] )
			newdomain.remove( jobs[1] )
			#print newdomain
			result = backtrack( people, newdomain )
			# check if result is correct
			if result != None:
				return result
			else:
				#print " backtrack "
				person.removejob()
				continue
		else:
			person.removejob()
			continue
	return None

result = backtrack( people, JOBS )
for person in result:
	print "Name :" + person.getname()
	print "Jobs :" 
	print person.getjob() 

