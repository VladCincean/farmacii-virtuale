'''
Created on 7 mai 2016

@author: Vlad
'''
class DiGraph:
    def __init__(self):
        self.__dictOut = {}
        self.__dictIn = {}
    
    def iterate(self):
        return self.__dictOut.keys()
    
    def iterateOut(self, x):
        if x not in self.__dictOut.keys():
            raise KeyError
        return self.__dictOut[x]
    
    def iterateIn(self, y):
        if y not in self.__dictIn.keys():
            raise KeyError
        return self.__dictIn[y]
    
    def isEdge(self, x, y):
        if x not in self.__dictOut.keys() or y not in self.__dictIn.keys():
            raise KeyError
        return y in self.__dictOut[x]
    
    def addVertex(self, x):
        if x in self.__dictOut.keys():
            raise ValueError("Vertex already exists.")
        self.__dictOut[x] = []
        self.__dictIn[x] = []
        
    def addEdge(self, x, y):
        if x not in self.__dictOut.keys() or y not in self.__dictIn.keys():
            raise KeyError("Invalid vertex (vertices).")
        if self.isEdge(x, y):
            raise ValueError("Edge already exist.")
        self.__dictOut[x].append(y)
        self.__dictIn[y].append(x)
