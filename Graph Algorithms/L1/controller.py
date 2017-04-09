'''
Created on 19 mar. 2016

@author: Vlad
'''

from graph import DiGraph

class Controller:
    def __init__(self, filename):
        self.__fName = filename
        self.__graph = None
        self.__loadFromFile()
        
    def __loadFromFile(self):
        # may raise IOError if invalid filename
        f = open(self.__fName, "r")
        n, m = f.readline().strip().split()
        n = int(n)
        m = int(m)
        self.__graph = DiGraph(n)
        for i in range(m):
            x, y, cost = f.readline().strip().split()
            x = int(x)
            y = int(y)
            cost = int(cost)
            self.__graph.addEdge(x, y)
            self.__graph.setCost(x, y, cost)
    
    def graph(self):
        return self.__graph
        
    