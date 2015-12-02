# Vishwas Siravara
#UIN: 623009600
import sys
import copy 
true_clauses = []
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

def satisfied( clauses ):
    decided_global = True
    for clause in clauses:
        decided = True
        decided2 = True
        for key in clause:
            # if key is false negation of key is true 
            if clause[ key ] == "-" and symbol_assignment[ key ] == False:
                decided = True
                decided2 = True
                break
            elif clause[key] == "+" and symbol_assignment[key] == True:
                decided = True
                decided2 = True
                break
            elif clause[key] == "+" and symbol_assignment[key] == False:
                decided2 = False
                continue
            elif clause[key] == "-" and symbol_assignment[key] == True:
                decided2 = False
                continue
            else:
                decided = False
        if decided2 == True and decided == True:
            if clause not in true_clauses:
                true_clauses.append( clause )
            continue
        elif decided == True and decided2 == False:
            if clause in true_clauses:
                true_clauses.remove( clause )
            return False
        else:
            # partial assignment , if some clause is not decided 
            decided_global = False
    if decided_global:
        return True
i = 0 
def dpll( knowledge_base, symbols ):
    global i
    global true_clauses
    print " Model: "
    print symbol_assignment
    # need the reference back when false is returned
    t_clauses = copy.deepcopy( true_clauses )
    i += 1
    if satisfied( knowledge_base):
        print 1
        return True
    elif satisfied( knowledge_base) == False:
        return False
    
    pvh = pureValueHeuristic( knowledge_base, symbols)
    if pvh != None:
        sym = pvh[0]
        symbols.remove( sym )
        if pvh[1] == '+':
            symbol_assignment[sym] = True
            print '%s %s: %s' % ("Setting Pure Symbol: ", sym , True )
        else:
            symbol_assignment[sym] = False
            print '%s %s: %s' % ("Setting Pure Symbol: ", sym , False )
        # remove reference to symbols 
        new_symbols = copy.deepcopy( symbols )
        return dpll( knowledge_base, new_symbols )
    
    uch = unitClauseHeuristic( knowledge_base, symbol_assignment )
    if uch != None:
        print "Unit clause heuristic"
        sym = uch[0]
        symbols.remove( sym )
        if uch[1] == '+':
            symbol_assignment[sym] = True
            print '%s %s: %s' % ("Setting symbol from unit clause heuristic: ", sym , True )
        else:
            symbol_assignment[sym] = False
            print '%s %s: %s' % ("Setting symbol from unit clause heuristic: ", sym , False )
        # remove reference to symbols 
        new_symbols = copy.deepcopy( symbols )
        return dpll( knowledge_base, new_symbols )

    
    sym = symbols.pop()
    symbol_assignment[sym] = True
    print "setting " + sym + " : " + "True"
    new_symbols = copy.deepcopy( symbols )
    print new_symbols
    x =  dpll( knowledge_base, new_symbols )
    y = None
    if x == False:
        symbol_assignment[sym] = False
        print "setting " + sym + " : " + "False" 
        #reset symbol_assignment here as it is pass by reference
        print new_symbols
        for symbol in new_symbols:
                symbol_assignment[symbol] = None
        # get back the clauses which were true earlier
        true_clauses = copy.deepcopy( t_clauses )
        #print symbols
        y = dpll( knowledge_base, new_symbols )
    if y != None:
        if y == False:
            print "Backtrack"
            return False
    return x or y 
def pureValueHeuristic( knowledge_base, symbols ):
    for symbol in symbols:
        symbol_sign = None
        for clause in knowledge_base:
            flag = True
            if clause in true_clauses:
                continue
            elif symbol in clause:
                if symbol_sign == None:
                    symbol_sign = clause[symbol]
                    continue
                elif symbol_sign == clause[symbol]:
                    continue
                else:
                    flag = False
                    break
        if flag:
            return symbol, symbol_sign

def unitClauseHeuristic(  knowledge_base, symbol_assignment ):
    for clause in knowledge_base:
        count = 0
        for key in clause:
            flag = False
            if clause[key] == "-" and symbol_assignment[ key ] == False:
                flag = True
                break
            elif clause[key] == "+" and symbol_assignment[ key ] == True:
                flag = True
                break
            elif clause[key] == "-" and symbol_assignment[ key ] == True:
                continue
            elif clause[key] == "+" and symbol_assignment[ key ] == False:
                continue
            else:
                count += 1
                sym = key
                sign = clause[ key ]
        if count == 1 and flag == False:
            return sym , sign
if len(sys.argv) != 3:
    print 'usage: python resolution.py filename "job1 job2 job 3 " '
    sys.exit(1)
line = sys.argv[2]
knowledge_base =  parse( sys.argv[1] )
cl = line.split()
for clause in cl:
    print clause
    if clause[0] == '-':
        knowledge_base.append( { clause : '-' } )
    else:
        knowledge_base.append( { clause : '+' } )
symbols = set( [] )
for clause in knowledge_base:
    for key in clause:
        symbols.add( key )
#print knowledge_base
symbol_assignment = { key: None for key in symbols }
if dpll( knowledge_base,  symbols ):
    print "----------------- Assignenments -------------------"
    for key in symbol_assignment:
        if symbol_assignment[ key ] == True:
            print '%s: %s' % ( key, symbol_assignment[ key ] )
    print '%s: %d' % ( "count", i )
else:
    print " Assignment not possible "


#print symbol_assignment
#print unitClauseHeuristic( knowledge_base, symbol_assignment)
