import graph_AL as graph
import connected_components as cc
import random
import numpy as np

#Part 1
def hamiltonian_randomized(V,E,max_trials=500000):
    for i in range(max_trials):
        Eh = random.sample(E,V)
        gEh = graph.Graph(len(Eh))
        for e in Eh:
            gEh.insert_edge(e.source, e.dest)
        #gEh.draw()#Uncomment to see each subset chosen.
        n, f = cc.connected_components(gEh)
        #Continue if only one connected component
        if n == 1:
            in_degree = True
            #Check that in-degree of each vertex is 2
            for v in range(len(gEh.al)):
                #If in-degree is not 2, stop checking and begin new trial
                if len(gEh.al[v]) != 2:
                    in_degree = False
                    break
            #If in-degree of each vertex is 2, return Hamiltonian Cycle
            if in_degree:
                print('Trials Taken: ', i)
                return Eh
    return None

#Part 2
#Additional method used to more easily identify currently unnecessary root nodes in a dsf
def has_children(dsf,i):
    for n in dsf.parent:
        if n == i:
            return True
    return False
#Method to determine wheter a set of edges satisfies Hamiltonian paths (and cycles)
def isHamPath(numV,E):
    if E is not None:
        g = graph.Graph(numV)
        for e in E:
            g.insert_edge(e.source, e.dest)
        n, f = cc.connected_components(g)
        #Since all nodes of original graph must be included to properly insert subset of edges,
        #one must check if any connected components consist solely of a root, 
        #thus not mattering to the current subset at large.
        for node in range(len(f.parent)):
            if not has_children(f, node) and f.find(node) == node:
                n-=1
        #Continue if only one (relevant) connected component
        if n == 1:
            #Check that in-degree of each vertex is 2 or less
            for v in range(len(g.al)):
                #If in-degree is above 2, stop checking
                if len(g.al[v]) > 2:
                    return False
            #If in-degree of each vertex is 2 or less, return Hamiltonian Path
            return True
    return False
#Method that recursively adds edges through traceback that end up forming a Hamiltonian cycle
def hamiltonian_backtrack(V,E,numV):
    duplicate = False
    #Base Cases (Need one to prevent incomplete cycles from being returned)
    if len(E) == 1:
        return [E[0]]
    if len(E) == 0 or len(V) == 0:
        return []
#!!!    if len(V) > len(E):#Something like this, but not quite.
#!!!        return [None]
    if len(V) > 0:
        for e in E[1:]:
            if E[0].source == e.dest and E[0].dest == e.source:
                duplicate = True
                break
        if not duplicate:
            if E[0].source in V:
                V.remove(E[0].source)
            hamPath = hamiltonian_backtrack(V,E[1:],numV)
            if None not in hamPath:
                if isHamPath(numV,[E[0]]+hamPath):
                    return [E[0]] + hamPath
                if E[0].source not in V:
                    V.append(E[0].source)
    return hamiltonian_backtrack(V,E[1:],numV)

#Part 3
def edit_distance(s1,s2):
    vowels = ['A','a','E','e','I','i','O','o','U','u']
    consonants = []
    #Add uppercase consonants by ASCII value
    for i in range(65,91):
        if chr(i) not in vowels:
            consonants.append(chr(i))
    #Add lowercase consonants by ASCII value
    for i in range(97,123):
        if chr(i) not in vowels:
            consonants.append(chr(i))
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[0,:] = np.arange(len(s2)+1)
    d[:,0] = np.arange(len(s1)+1)
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] ==s2[j-1]:
                d[i,j] =d[i-1,j-1]
            else:
                #Check if both are vowels or consonants before adding change to min(n), replacing the letters
                if (s1[i-1] in vowels and s2[j-1] in vowels) or (s1[i-1] in consonants and s2[j-1] in consonants):
                    n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                    d[i,j] = min(n)+1
                #If not matching types, both removal and addition must occur, so add 1 to max(n), not min(n)
                else:
                    n = [d[i,j-1],d[i-1,j-1],d[i-1,j]]
                    d[i,j] = max(n)+1
    return d[-1,-1]

if __name__ == "__main__":
    #Generate graph which has guaranteed Hamiltonian Cycle
    gHam = graph.Graph(7)
    gHam.insert_edge(0,len(gHam.al)-1)
    for i in range(len(gHam.al) - 1):
        #Insert edge to connect each vertex to next vertex in succession
        gHam.insert_edge(i, i+1)
        #Insert random edges to properly test hamiltonian_randomized() method
        s,d = random.randrange(0, len(gHam.al)-1),random.randrange(0, len(gHam.al)-1)
        gHam.insert_edge(s,d)
    #gHam.as_EL().display()#Uncomment to see edge list of inital graph.
    gHam.draw()
    
    #Attempt to find Hamiltonian Cycle (Should be found)
    #Randomized
    gHamCycle = hamiltonian_randomized(len(gHam.al),gHam.as_EL().el)
    if gHamCycle is not None:
        gEh = graph.Graph(len(gHamCycle))
        for e in gHamCycle:
            gEh.insert_edge(e.source, e.dest)
        gEh.draw()
    else:
        print('Hamiltonian Cycle not found.')
    #Backtracking
    vertexList = [None] * len(gHam.al)
    for i in range(len(gHam.al)):
        vertexList[i] = [i]
    vertexList = list(range(0,len(gHam.al)))
    gHamCycle = hamiltonian_backtrack(vertexList,gHam.as_EL().el,len(gHam.al))
    if None not in gHamCycle:
        gEh = graph.Graph(len(gHam.al))
        print('gHamCycle:', end=' ')
        for e in gHamCycle:
            print('(',e.source,e.dest,')',end=' ')
            gEh.insert_edge(e.source, e.dest)
        print()
        gEh.draw()
    else:
        print('Hamiltonian Cycle not found.')

    #Generate graph which does not have guaranteed Hamiltonian Cycle
    g = graph.Graph(4)
    g.insert_edge(0,len(g.al)-1)
    for i in range(len(g.al) - 1):
        #Insert random edges into graph
        s,d = random.randrange(0, len(g.al)-1),random.randrange(0, len(g.al)-1)
        g.insert_edge(s,d)
    g.draw()
    
    #Attempt to find Hamiltonian Cycle (Should generally not be found)
    #Randomized
    gHamCycle = hamiltonian_randomized(len(g.al),g.as_EL().el)
    if gHamCycle is not None:
        gEh = graph.Graph(len(gHamCycle))
        for e in gHamCycle:
            gEh.insert_edge(e.source, e.dest)
        gEh.draw()
    else:
        print('Hamiltonian Cycle not found.')
    #Backtracking
    vertexList = [None] * len(g.al)
    for i in range(len(g.al)):
        vertexList[i] = [i]
    vertexList = list(range(0,len(g.al)))
    gHamCycle = hamiltonian_backtrack(vertexList,g.as_EL().el,len(g.al))
    if None not in gHamCycle:
        gEh = graph.Graph(len(g.al))
        print('gHamCycle:', end=' ')
        for e in gHamCycle:
            print('(',e.source,e.dest,')',end=' ')
            gEh.insert_edge(e.source, e.dest)
        print()
        gEh.draw()
    else:
        print('Hamiltonian Cycle not found.')
    
    #Check modified edit_distance function
    print('Edit Distance from "sand" to "sound": ', edit_distance('sand', 'sound'))
    print('Edit Distance from "corn" to "coat": ', edit_distance('corn', 'coat'))
    print('Edit Distance from "feet" to "feel": ', edit_distance('feet', 'feel'))
    print('Edit Distance from "trash" to "unicorn": ', edit_distance('trash', 'unicorn'))
    print('Edit Distance from "alabama', 'mississippi'))
