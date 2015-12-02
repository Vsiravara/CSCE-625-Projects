import copy
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

knowledge_base =  parse( "master.kb" )
symbols = set( [] )
for clause in knowledge_base:
    for key in clause:
        symbols.add( key )
symbol_assignment = { key: None for key in symbols }

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
            continue
        elif decided == True and decided2 == False:
            return False
        else:
            decided_global = False
    if decided_global:
        return True
i = 0 
def dpll( knowledge_base, symbols):
    global i
    i += 1
    if satisfied( knowledge_base ) :
        print 1
        return True
    elif satisfied( knowledge_base ) == False:
        return False
    """
    uch = unitClauseHeuristic( knowledge_base, symbol_assignment )
    if uch != None:
        print "Unit clause"
        sym = uch[0]
        symbols.remove( sym )
        print sym
        if uch[1] == '+':
            symbol_assignment[sym] = True
        else:
            symbol_assignment[sym] = False
        return dpll( knowledge_base, symbols )
    """
   

    sym = symbols.pop()
    symbol_assignment[sym] = True
    new_symbols = copy.deepcopy( symbols )
    print symbol_assignment
    print "setting " + sym + " to " + "True"
    x =  dpll( knowledge_base, symbols)
    y = None
    if x == False:
        symbol_assignment[sym] = False
        print "setting " + sym + " to " + "False" 
        print symbols
        for x in new_symbols:
            symbol_assignment[ x ] = None
        y = dpll( knowledge_base, symbols)
        print y
        print symbol_assignment
    if y != None:
        if y == False:
            print "Backtrack"
            symbols.add( sym )
            symbol_assignment[sym] = None
            return False
    #return ( x or y )
    
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

  
dpll( knowledge_base, symbols )
for key in symbol_assignment:
    if symbol_assignment[ key ] == True:
        print '%s: %s' % ( key, symbol_assignment[ key ] )
print '%s: %d' % ( "count", i )

#print symbol_assignment
#print unitClauseHeuristic( knowledge_base, symbol_assignment)