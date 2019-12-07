# Edge list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL as al
import graph_AM as am

#Code provided by Dr. Fuentes excepted where noted as Parts 1 and 2
class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.el = []
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
    #Part 1
    #1(a)    
    def insert_edge(self,source,dest,weight=1):
        if source >= self.vertices or dest >= self.vertices or source <0 or dest<0:
            print('Error, vertex number out of range')
        if weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            #Sorted
            index = 0
            for i in range(len(self.el)):
                if self.el[i].dest > dest and self.el[i].source == source:
                    index = i
                    break
                elif self.el[i].source > source:
                    index = i
                    break
                elif i == len(self.el) - 1:
                    index = i + 1
            self.el = self.el[:index] + [Edge(source,dest,weight)] + self.el[index:]
            if not self.directed:
                for i in range(len(self.el)):
                    if self.el[i].dest > source and self.el[i].source == dest:
                        index = i + 1
                        break
                    elif self.el[i].source > dest:
                        index = i
                        break
                    elif i == len(self.el) - 1:
                        index = i + 1
                self.el = self.el[:index] + [Edge(dest,source,weight)] + self.el[index:]
    #1(b)
    def delete_edge(self,source,dest):
        if source >= self.vertices or dest>=self.vertices or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            for i in range(len(self.el)):
                if self.el[i].source == source and self.el[i].dest == dest:
                    self.el.remove(self.el[i])
                    break
            if not self.directed:
                for i in range(len(self.el)):
                    if self.el[i].source == dest and self.el[i].dest == source:
                        self.el.remove(self.el[i])
                        break
    #1(c)          
    def display(self):
        print('[',end='')
        for e in self.el:
            print('('+str(e.source)+','+str(e.dest)+','+str(e.weight)+')',end='')  
        print(']')
    #3(c)       
    def as_EL(self):
        return self
    #3(b)
    def as_AM(self):
        g = am.Graph(self.vertices, self.weighted, self.directed)
        for e in self.el:
            g.insert_edge(e.source, e.dest, e.weight)
        return g
    #3(a)
    def as_AL(self):
        g = al.Graph(self.vertices, self.weighted, self.directed)
        for e in self.el:
            g.insert_edge(e.source, e.dest, e.weight)
        return g
    
    #Part 2
    def BFS(self):
        print("BFS")
        frontier = []
        discover = []
        path = []
        
        frontier.append(self.el[0])
        discover.append(self.el[0])
        path.append(0)
        
        while frontier != []:
            curV = frontier.pop(0)
            for e in self.el:
                if e.source == curV.dest and e not in discover:
                    frontier.append(e)
                    discover.append(e)
                    if e.source not in path:
                        path.append(e.source)
                if e.source > curV.dest:
                    break
        if e.dest not in path:
            path.append(e.dest)
        
        print("Path from 0 to 15: ")
        for v in path:
            print(v, end = ' ')
            if v == 15:
                break
        print()
        
    def DFS(self):
        print("DFS")
        stack = []
        visit = []
        path = []
        
        stack.append(self.el[0])
        path.append(0)
        
        while stack != []:
            curV = stack.pop()
            if curV not in visit:
                visit.append(curV)
                for e in self.el:
                    if e.source == curV.dest and e not in stack:
                        stack.append(e)
                        if e.source not in path:
                            path.append(e.source)
                    if e.source > curV.dest:
                        break
        
        print("Path from 0 to 15: ")
        for v in path:
            print(v, end = ' ')
            if v == 15:
                break
