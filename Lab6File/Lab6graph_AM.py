# Adjacency matrix representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL as al
import graph_EL as el

#Code provided by Dr. Fuentes excepted where noted as Parts 1 and 2
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.am = np.zeros((vertices,vertices),dtype=int) - 1
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AM'
        
    #Part 1
    #1(a)
    def insert_edge(self,source,dest,weight=1):
        if source >= len(self.am) or dest>=len(self.am) or source <0 or dest<0:
            print('Error, vertex number out of range')
        if weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.am[source][dest] = weight 
            if not self.directed:
                self.am[dest][source] = weight
    #1(b)
    def delete_edge(self,source,dest):
        if source >= len(self.am) or dest>=len(self.am) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            self.am[source][dest] = -1
            if not self.directed:
                self.am[dest][source] = -1
    #1(c)           
    def display(self):
        for i in range(len(self.am)):
            for j in range(len(self.am)):
                print(self.am[i,j], end = '\t')
            print()
        print()
    #3(c)
    def as_EL(self):
        g = el.Graph(len(self.am), self.weighted, self.directed)
        for i in range(len(self.am)):
            for j in range(len(self.am)):
                if self.am[i,j] > -1:
                    g.insert_edge(i, j, self.am[i,j])
        return g
    #3(b)
    def as_AM(self):
        return self
    #3(a)
    def as_AL(self):
        g = al.Graph(len(self.am), self.weighted, self.directed)
        for i in range(len(self.am)):
            for j in range(len(self.am)):
                if self.am[i,j] > -1:
                    g.insert_edge(i, j, self.am[i,j])
        return g
    
    #Part 2
    def BFS(self):
        print("BFS")
        frontier = []
        discover = []
        path = [[] for i in range(len(self.am))]
        
        frontier.append(self.am[0])
        discover.append(0)
        path[0].append(0)
        
        while frontier != []:
            curV = frontier.pop(0)
            i = 0
            for e in range(len(curV)):
                if curV[e] != -1 and e not in discover:
                    frontier.append(self.am[e])
                    discover.append(e)
                    if e not in path[i]:
                        path[i].append(e)
                        i += 1
                        
        print("Path from 0 to 15: ")
        for v in path[0]:
            print(v, end = ' ')
        if path[0][-1] != 15:
            for p in path:
                if p[-1] == 15:
                    for v in p:
                        print(v, end = ' ')
                    break
        print()
        
    def DFS(self):
        print("DFS")
        stack = []
        visit = []
        path = [[] for i in range(len(self.am))]
        
        stack.append(self.am[0])
        path[0].append(0)
        
        while stack != []:
            curV = stack.pop()
            i = -1
            for e in range(len(self.am)):
                if curV[e] != -1:
                    i += 1
            for e in range(len(self.am)):
                if curV[e] != -1 and e not in visit:
                    visit.append(e)
                    stack.append(self.am[e])
                    if e not in path[i]:
                        path[i].append(e)
                        i -= 1
        
        print("Path from 0 to 15: ")
        for v in path[0]:
            print(v, end = ' ')
        if path[0][-1] != 15:
            for p in path:
                if p[-1] == 15:
                    for v in p:
                        if v == 0:
                            pass
                        else:
                            print(v, end = ' ')
                    break
        print()
