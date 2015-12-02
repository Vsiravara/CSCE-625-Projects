# Assignment 4
# Vishwas Siravara

import sys
import heapq
# parse file into list of hash table , if -x store key as x and value as - and for x store key as x and value as + in the dictionary 
def parse(filename): 
    clauses = []
    f = open(filename, 'ru')
    for line in f:
        if line not in ('\n', '\r\n') and line[0] != '#':
            clause = {}
            literals = line.split()
            for liter in literals:
                if liter[0] == '-':
                    clause[liter[1:]] = '-'
                else:
                    clause[liter] = '+'
            clauses.append(clause)
    return clauses

def printclause(clause):
    if len(clause) == 0:
        return '()'
    string = ""
    for key in clause.keys():
        string += " "
        if clause[key] == '-':
            string += '-' + key 
        else:
            string += key 
    
    return string

def resolve(clause1, clause2):
    newclause = clause1.copy()
    for liter in clause2.keys():
        if newclause.has_key(liter):
            if clause2[liter] != newclause[liter]:
                newclause.pop(liter)
        else:
            newclause[liter] = clause2[liter]
    return newclause

def isresolve(clause1, clause2):
    for liter1 in clause1.keys():
        for liter2 in clause2.keys():
            if liter1 == liter2 and clause1[liter1] != clause2[liter2]:
                return True
    return False

def resolver(clauses):
    count = 0
    candidates = []
    prooftree = {}
    for i in range(len(clauses)):
        prooftree[i] = []
        for j in range(i+1, len(clauses)):
            if isresolve(clauses[i], clauses[j]):
                heur = len(clauses[i]) + len(clauses[j])
                heapq.heappush(candidates, (heur, (i, j)))
    while not len(candidates) == 0:
        count += 1
        print count
        c = heapq.heappop(candidates)
        newclause = resolve(clauses[c[1][0]], clauses[c[1][1]])
        print "---------------------------------"
        print  " Queue size: " + str( len(candidates) )
        print "Clause selected : " +  printclause(clauses[c[1][0]]) + " , " +  printclause(clauses[c[1][1]])
        m = len(clauses)
        if len(newclause)== 0:
            print " Iterations count :" + str( count )
            clauses.append(newclause)
            prooftree[m] = [c[1][0], c[1][1]]
            print '%d: %s' % (m, printclause(newclause))
	    print "Empty Clause "
            print ' Successful '
            print '------------------'
            print 'trace:'
            recursetree(m, prooftree, clauses, 1)
            return True
        if newclause not in clauses:
            clauses.append(newclause)
            print " New clause added after resolution : " +  printclause(newclause)
            prooftree[m] = [c[1][0], c[1][1]]
            for k in range(m):
                if isresolve(newclause, clauses[k]):
                    heur = len(newclause) + len(clauses[k])
                    heapq.heappush(candidates, (heur, (k, m)))
    return False

def recursetree(m, prooftree, clauses, depth):
    parents = prooftree[m]
    if len(parents) == 0:
        print '%d: %s input' % ( m, printclause(clauses[m]))
    else:
        print ' %d: %s [%d,%d]' % ( m, printclause(clauses[m]), parents[0], parents[1])
        recursetree(parents[0], prooftree, clauses, depth+1)
        recursetree(parents[1], prooftree, clauses, depth+1)


if len(sys.argv) != 2:
    print 'usage: python resolution.py file'
    sys.exit(1)

filename = sys.argv[1]
clauses = parse(filename)
print clauses
print 'initial clauses:'
for i in range(len(clauses)):
    print '%d: %s' % (i, printclause(clauses[i]))
print '--------------------'

resolver(clauses)


