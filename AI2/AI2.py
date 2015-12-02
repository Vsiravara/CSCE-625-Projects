
"""
Vishwas Siravara
UIN: 623009600
"""
import heapq
import time
import math
import sys
from heapq import *
import copy

MAPPING = { "A" : 0 , "B" : 1 , "C" : 2 , "D" : 3 , "E" : 4, \
           "F" : 5 , "G" : 6 , "H" : 7 , "I": 8 , "J" : 9 , "K" : 10, "L" : 11, \
           "M": 12, "N" : 13, "O" : 14 , "P" : 15, "Q" : 16 , "R" : 17, "S" : 18 \
          ,"T" : 19 , "U" : 20 , "V" : 21 , "W" : 22 , "X" : 23 , "Y" : 24 , "Z" : 25 }

class Node:
	def __init__(self):
		self.parent = None
		self.state = []
		self.children = []
		self.depth = 0
		self.heuristic = None

	def set_heuristics( self ):

		self.heuristic = num_of_alphabets( self.state ) + self.depth
		index = 0
		for alphabet in self.state[0]:
			if self.state[0].index( alphabet ) == MAPPING.get( alphabet ):
				self.heuristic -= 1
				index += 1	
			else:
				break	
		self.heuristic += len( self.state[0][index : ])	
	
	def get_heuristics(self):
		return self.heuristic

	def set_depth( self, depth):
		self.depth = depth

	def get_depth(self):
		return self.depth
		
	def get_state( self ):
		return self.state

	def set_parent( self, parent):
		self.parent = parent

	def set_state( self, state):
		self.state = state

	def get_parent( self ):
		return self.parent

	def childstates( self ):
		children = []
		# iterate over self state one stack at a time
		for i in range(len( self.state )):
			if len( self.state[i] ) == 0:
				continue
			else:
				for j in range(len( self.state )):
					if i == j:
						continue
					curr_stack = copy.deepcopy( self.state )
					curr_stack[j].append( curr_stack[i].pop() )
					children.append( curr_stack )
		
		return children

""" Define A* search """
def astar( root  ):
	frontier = []
	visited = set([])
	closed = set([])
	visited.add( tuple( tuple(ele) for ele in root.get_state() ))
	heappush( frontier, ( root.get_heuristics() , root ) )
	count = 0 
	while frontier :
		count += 1
		if count == 10000:
			print " Goal state not found , too many iterations "
			sys.exit()

		""" Debug checks
		for x, y in frontier:
			 
			print " Parent "
			print y.get_parent().get_depth()
			print y.get_parent().get_heuristics()
			print y.get_parent().get_state()
			print "_____"
			print "child"
			print y.get_depth()
			print x
			print y.get_state()

		print "------------------------------"
		"""

		element = heappop( frontier )
		parent = element[1]
		#print parent.get_heuristics()
		#print parent.get_state()

		closed.add( tuple( tuple(ele) for ele in parent.get_state() ))
		if goalreach( parent.get_state() ):
			print "Number of iterations are  " + str( count )
			print "Frontier size is :" + str(  len( frontier ) )
			return parent
		else:
			for child_state in parent.childstates():
				if tuple(tuple(ele) for ele in child_state) in closed:
					continue
				else:
					# set attributes of the child 
					child = Node()
					child.set_state( child_state )
					child.set_parent( parent )
					child.set_depth( parent.get_depth() + 1 )
					# set heuristic after setting depth
					child.set_heuristics()
					
					

					# check if child is in frontier 
					if tuple(tuple(ele) for ele in child.get_state() ) in visited:
						# iterate through heap , check if heuristic of node in heap is more than child, if so delete the heap element and add child
						index = 0
						for priority, node in frontier:
							if node.get_state() == child.get_state() :
								if child.get_heuristics() < node.get_heuristics():
									frontier[index] = frontier[-1 ]
									frontier.pop()
									heappush( frontier, ( child.get_heuristics(), child ))
									heapq.heapify( frontier )

									break
								else:
									# if heuristic of child is more than the state in heap set child to None for gc 
									child = None
									break
							else:
								index += 1
					else:
						heappush( frontier, ( child.get_heuristics(), child ) )
						visited.add( tuple( tuple(ele) for ele in child.get_state() ))	
		


def getpath( goal ):
	path = []
	path.append( goal )
	while goal.get_parent() !=  goal:
		goal = goal.get_parent()
		path.insert(0, goal )
	for node in path:
		print "Next move "
		print node.get_state()

def num_of_alphabets( stacks ):
	count = 0
	for stack in stacks:
		count += len(stack)
	return count
def goalreach( stacks ):
	count = 0
	for alphabet in stacks[0]:
		if stacks[0].index( alphabet ) == MAPPING.get( alphabet ):
			count += 1
		else:
			return False
	if count == num_of_alphabets( stacks ):
		return True
	else:
		return False
if len( sys.argv ) != 2:
	print "usage : python AI2.py < number of stacks >"
	sys.exit()
master = []
numOfStacks = int( sys.argv[1] )
for i in range(0, numOfStacks):
	print " Enter contents of stack " + str( i + 1 ) + " as a string  , Eg. BCA , if stack is empty just hit enter"
	sta = raw_input()

	if sta == None:
		master.append( [] )
	else:
		master.append( list( sta ) )
print " Initial state is " + str( master )

root = Node()
root.set_parent( root )
root.set_state( master )
root.set_depth( 0 ) 
root.set_heuristics()
#print root.childstates()
start = time.time()
goal = astar(root)
stop = time.time()
print "Run time is :" + str( stop - start )
print "Solution path is: "
getpath( goal )
print "Depth of goal state is " + str( goal.get_depth() )











