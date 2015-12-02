
"""
Vishwas Siravara
UIN: 623009600
"""
import time
import math
import sys
from heapq import *
class Graph:
	def __init__(self):
		self.edgecount = 641
		self.nodes = 275
		f = open(sys.argv[1])
		next(f)
		self.iterations = 0
		self.coordinates = []
		self.edgelist = []
		count = 0
		for line in f:
			if count == 275:
				break
			else:
				self.coordinates.append([ int(i) for i in line.split()[1:] ])
				count += 1
		next(f)

		for line in f:
			self.edgelist.append([ int(i) for i in line.split()[1:] ])

	
	def getLocation( self, vertex ):
		return self.coordinates[vertex]

	def adjecent( self, node ):
		adj = []
		for li in self.edgelist:
			if li[0] == node:
				adj.append( li[1] )
			elif li[1] == node:
				adj.append(li[0])
			else:
				continue
		return adj
	def setiterations( self ):
		self.iterations += 1
	def getiterations( self):
		return self.iterations
	def getindex( self, xcord, ycord):
		i = 0
		for x,y in self.coordinates :
			if x == xcord and y == ycord:
				return i
			else:
				i += 1

		return -1 

class Node:
	def __init__(self, vertex):
		self.parent = None
		self.vertex = vertex

	def set_parent( self, parent):
		self.parent = parent

	def get_parent( self ):
		return self.parent

	def get_vertex( self ):
		return self.vertex

def make_node( vertex ):
	return Node( vertex )

def bfs( graph, initial, goal):
	frontier = []
	visited = set([])
	graph.iterations = 0
	size = 0
	initial.set_parent( initial )
	visited.add( initial.get_vertex() )
	if initial.get_vertex() == goal.get_vertex():
		return initial
	else:
		frontier.insert(0, initial )

		while frontier:
			if len( frontier ) > size:
				size = len(frontier)
			graph.setiterations()
			parent = frontier.pop()
			adj_list = graph.adjecent( parent.get_vertex() )
			for vertex in adj_list:
				if vertex not in visited:
					node = Node( vertex )
					node.set_parent(parent)
					if node.get_vertex() == goal.get_vertex():
						print " lenght of visited is " + str(len(visited))
						print " max frontier size is " + str( size )
						return node
					else:
						frontier.insert(0, node )
						visited.add( node.get_vertex() )
				else:
					continue

def distance( node1, node2):
	return math.sqrt( ( node1[0] - node2[0] ) ** 2 + ( node1[1]  - node2[1] ) ** 2 )

def dfs( graph, initial, goal):
	size = 0
	graph.iterations = 0
	frontier = []
	visited = set([])
	initial.set_parent( initial )
	visited.add( initial.get_vertex() )
	if initial.get_vertex() == goal.get_vertex():
		return initial
	else:
		frontier.append( initial)
		while frontier:
			if len( frontier ) > size:
				size = len(frontier)
			graph.setiterations()
			parent = frontier.pop()
			#print parent.get_vertex()
			if parent.get_vertex() == goal.get_vertex():
						#print node.get_vertex()
						print " lenght of visited is " + str(len(visited))
						print " max lenght of frontier is "	+ str( size )
							
						return parent

			adj_list = graph.adjecent( parent.get_vertex() )

			for vertex in adj_list:
				if vertex not in visited:
					node = Node( vertex )
					node.set_parent( parent )
					frontier.append( node )
					visited.add( node.get_vertex() )
				else:
					continue

def gbfs( graph, initial, goal):
	frontier = []
	size = 0
	visited = set([])
	graph.iterations = 0
	initial.set_parent( initial )
	visited.add( initial.get_vertex() )
	if initial.get_vertex() == goal.get_vertex():
		return initial
	else:
		heappush( frontier, ( distance( graph.getLocation( initial.get_vertex()), graph.getLocation( goal.get_vertex() ) ), initial ) )
		while frontier:
			if len( frontier ) > size:
				size = len(frontier)	
			graph.setiterations()
			element = heappop( frontier )
			#print parent.get_vertex()
			parent = element[ 1 ]
		
			adj_list = graph.adjecent( parent.get_vertex() )
			for vertex in adj_list:
				if vertex not in visited:
					node = Node( vertex )
					node.set_parent( parent )
					#print node.get_vertex()
				    
					if node.get_vertex() == goal.get_vertex():
						print " lenght of visited is " + str(len(visited))
						print " lenght of frontier is "	+ str(size)
						return node
					else:
						heappush( frontier, ( distance( graph.getLocation( node.get_vertex()), graph.getLocation( goal.get_vertex() ) ), node ) )
						visited.add( node.get_vertex() )
				else:
					continue
def getpath( goal ):
	path = []
	path.append( goal )
	coordinates = []
	coordinates.append( graph.getLocation( goal.get_vertex() ) )
	while goal.get_parent() !=  goal:
		goal = goal.get_parent()
		coordinates.insert( 0, graph.getLocation( goal.get_vertex() ))
		path.insert(0, goal )
	for node in path:
		print node.get_vertex()
	print " Path with coordinates "
	for coordinate in coordinates:
		print coordinate
	print "Path length " + str( len(path) )

if len(sys.argv) != 6:
	print " Enter 5 arguements ( filename) , x-codinate of point 1, y coordinate of point 1,x-codinate of point 2, y coordinate of point 2"
	sys.exit()
graph = Graph()
x1 = int(sys.argv[2])
y1 = int(sys.argv[3])
x2 = int( sys.argv[4] )
y2 = int( sys.argv[5] )
index1 = graph.getindex( x1, y1 )
index2 = graph.getindex( x2, y2 )
if index1 == -1 or index2 == -1:
	print " coordintes out of range "
	sys.exit()
print "--------BFS--------------"
start = time.time()
goal = bfs( graph, Node(index1), Node(index2) )
stop = time.time() 
print " Iterations is " + str( graph.getiterations() )
print " Time taken bfs "
print stop - start
print " Path for bfs is: "
getpath( goal )

print "------------DFS-------------"
start = time.time()
goal = dfs( graph, Node(index1), Node(index2) )
stop = time.time() 
print " Iterations is " + str( graph.getiterations() )
print " Time taken for dfs "
print stop - start
print " Path for dfs is: "
getpath( goal )

print "------------GBFS---------------"
start = time.time()
goal = gbfs( graph, Node(index1), Node(index2) )
stop = time.time() 
print " Iterations is " + str( graph.getiterations() )
print " Time taken for gbfs "
print stop - start
print " Path for gbfs is: "
getpath( goal )
















