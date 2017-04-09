class Graph:
    def __init__(self):
        ''' Constructor '''
        self.__adj = {}
        
    def __str__(self):
        s = "Vertices: "
        s += str(list(self.__adj.keys())) + "\n"
        s += "Edges: "
        e = []
        for u in self.__adj.keys():
            for v in self.__adj[u]:
                if u < v:
                    e.append((u, v))
        s += str(e)
        return s
    
    def __repr__(self):
        return str(self)
        
    def iterate(self):
        ''' List of all vertices '''
        return list(self.__adj.keys())
    
    def iterateX(self, x):
        ''' Neighbours of vertex x '''
        if x not in self.__adj.keys():
            raise KeyError
        return self.__adj[x]
    
    def getN(self):
        ''' Number of vertices '''
        return len(self.__adj.keys())
    
    def getM(self):
        ''' Number of edges '''
        e = []
        for u in self.__adj.keys():
            for v in self.__adj[u]:
                if u < v:
                    e.append((u, v))
        return len(e)
    
    def isEdge(self, x, y):
        ''' Checks if {x, y} is an edge '''
        if x not in self.__adj.keys():
            raise KeyError
        return y in self.__adj[x]
    
    def degree(self, x):
        ''' Provides the degree of a vertex '''
        if x not in self.__adj.keys():
            raise KeyError
        return len(self.__adj[x])
        
    def addEdge(self, x, y):
        if x not in self.__adj.keys() or y not in self.__adj.keys():
            raise KeyError
        if self.isEdge(x, y):
            return False
        self.__adj[x].append(y)
        self.__adj[y].append(x)
#         self.__m += 1
        return True

    def removeEdge(self, x, y):
        if not self.isEdge(x, y):
            raise ValueError
        if y in self.__adj[x]:
            self.__adj[x].remove(y)
        if x in self.__adj[y]:
            self.__adj[y].remove(x)
#         self.__m -= 1
        
    def addVertex(self, x):
        if x in self.__adj.keys():
            raise ValueError("Vertex already exists.")
        self.__adj[x] = []
#         self.__n += 1
        
    def removeVertex(self, x):
        if x not in self.__adj.keys():
            raise KeyError("Invalid vertex id.")
        edges = []
        for v in self.__adj[x]:
            e = (v, x)
            edges.append(e)
            self.__adj[v].remove(x)
        for e in edges:
            if self.isEdge(e[0], e[1]):
                self.removeEdge(e[0], e[1])
        del self.__adj[x]
#         self.__n -= 1    
