'''
Created on 29 feb. 2016

@author: Vlad
'''

class Graph:
    def __init__(self, n):
        '''
        Creates an undirected graph with n vertices and no edges
        @param n: number of vertices
        @precondition: n > 0, n whole number
        '''
        self.__adj = {}
        self.__n = n # no. of vertices
        self.__m = 0 # no. of edges
        for i in range(n):
            self.__adj[i] = []
        
    def __str__(self):
        pass
    
    def __repr__(self):
        return str(self)
    
    def getV(self):
        '''
        Function to get the number of vertices
        @return n: number of vertices
        @postcondition: n > 0, n whole number
        '''
        return self.__n
    
    def getE(self):
        '''
        Function to get the number of edges
        @return m: number of edges
        @postcondition: m >= 0, m whole number
        '''
        return self.__m
    
    def isEdge(self, x, y):
        '''
        Checks if there is an edge between the vertices x and y
        @param x: source vertex
        @param y: target vertex
        @raise KeyError: if x is not a valid vertex
        @return True: if there is an (directed) edge from x to y
        @return False: otherwise
        '''
        if x not in self.__adj.keys():
            raise KeyError
        return y in self.__adj[x]
    
    def degree(self, x):
        '''
        Function to get the degree of a given vertex
        @param x: vertex
        @precondition: 0 <= x < n
        @raise KeyError: if x is not a valid vertex
        @return: deg(x)
        '''
        if x not in self.__adj.keys():
            raise KeyError
        return len(self.__adj[x])
    
    def iterate(self, x):
        '''
        Function to iterate through the set of incident edges of a given vertex
        @param x: vertex
        @precondition: 0 <= x < n
        @raise KeyError: if x is not a valid vertex
        @return: iterator that provides the second vertex of the current edge having the first vertex x
        '''
        if x not in self.__adj.keys():
            raise KeyError
        return self.__adj[x]
    
    def addEdge(self, x, y):
        '''
        Function to add an edge.
        @param x: edge's first vertex
        @param y: edge's second vertex
        @precondition: 0 <= x, y < n; there is no edge between x and y
        @raise KeyError: if x or y are not valid vertices
        @return True: if edge successfully added
        @return False: otherwise
        '''
        if x not in self.__adj.keys() or y not in self.__adj.keys():
            raise KeyError
        if self.isEdge(x, y):
            return False # there is already and edge between x and y
        self.__adj[x].append(y)
        self.__adj[y].append(x)
        self.__m += 1
        return True
        
    def removeEdge(self, x, y):
        '''
        Function to remove an edge
        @param x: edge's first vertex
        @param y: edge's second vertex
        @precondition: there is an edge between the vertices x and y
        @raise ValueError: if there is no edge between x and y
        '''
        if not self.isEdge(x, y):
            raise ValueError
        if y in self.__adj[x]:
            self.__adj[x].remove(y)
        if x in self.__adj[y]:
            self.__adj[y].remove(x)
        self.__m -= 1
        
    def addVertex(self, x):
        '''
        Function to add a vertex
        @param x: vertex
        @precondition: the vertex does not exist already
        @raise ValueError: if vertex already exists
        '''
        if x in self.__adj.keys():
            raise ValueError("Vertex already exists.")
        self.__adj[x] = []
        self.__n += 1
        
    def removeVertex(self, x):
        '''
        Function to remove a vertex. This function also removes the edges that are incident to the vertex to be removed
        @param x: vertex to be removed
        @precondition: x is a valid vertex
        @raise KeyError: if x is not a valid vertex
        '''
        if x not in self.__adj.keys():
            raise KeyError("Invalid vertex id.")
        edges = [] # stores the edge keys to be removed
        for v in self.__adj[x]:
            e = (v, x) # do no make it a set because it will not support indexing
            edges.append(e)
            self.__adj[v].remove(x)
        for e in edges: # remove incident edges
            if self.isEdge(e[0], e[1]):
                self.removeEdge(e[0], e[1])
        del self.__adj[x]
        self.__n -= 1

class GraphC(Graph):
    def __init__(self, n):
        '''
        Creates a undirected graph with n vertices and no edges
        @param n: number of vertices
        @precondition: n > 0, n whole number
        '''
        Graph.__init__(self, n)
        self.__edges = {} # set(x,y): cost
        
    def __str__(self):
        pass
    
    def getCost(self, x, y):
        '''
        Function to retrieve the information attached to a specific edge (the cost)
        @param x: edge's first vertex
        @param y: edge's second vertex
        @precondition: there must be an edge between x and y
        @raise KeyError: if there is no edge between x and y
        @return: cost(x, y)
        '''
        if not self.isEdge(x, y):
            raise KeyError
        return self.__edges[set(x, y)]
    
    def setCost(self, x, y, cost):
        '''
        Function to modify the information attached to a specific edge (the cost)
        @param x: edge's first vertex
        @param y: edge's second vertex
        @param cost: edge's new cost
        @precondition: there must be an edge between x and y
        @raise KeyError: if there is no edge between x and y
        '''
        if not self.isEdge(x, y):
            raise KeyError
        self.__edges[set(x, y)] = cost
    
    def addEdge(self, x, y):
        '''
        Function to add an edge. This function sets the cost of the edge to 'None'
        @param x: edge's first vertex
        @param y: edge's second vertex
        @precondition: 0 <= x, y < n; there is no edge between x and y
        @raise KeyError: if x or y are not valid vertices
        @return True: if edge successfully added
        @return False: otherwise
        '''
        if Graph.addEdge(self, x, y):
            self.__edges[set(x, y)] = None
            return True
        return False
        
    def removeEdge(self, x, y):
        '''
        Function to remove an edge
        @param x: edge's first vertex
        @param y: edge's second vertex
        @precondition: there is an edge between the vertices x and y
        @raise ValueError: if there is no edge between x and y
        '''
        Graph.removeEdge(self, x, y)
        if set(x, y) in self.__edges.keys():
            del self.__edges[set(x, y)]

class DiGraph:
    def __init__(self, n):
        '''
        Creates a directed graph with n vertices and no edges
        @param n: number of vertices
        @precondition: n > 0, n whole number
        '''
        self.__dictOut = {}
        self.__dictIn = {}
        self.__n = n #no. of vertices
        self.__m = 0 #no. of edges
        for i in range(n):
            self.__dictOut[i] = []
            self.__dictIn[i] = []
        
    def __str__(self):
        s = "dictOut = " + str(self.__dictOut) + "\n"
        s += "dictIn = " + str(self.__dictIn) + "\n"
        return s
    
    def __repr__(self):
        return str(self)
    
    def getV(self):
        '''
        Function to get the number of vertices
        @return n: number of vertices
        @postcondition: n > 0, n whole number
        '''
        return self.__n
    
    def getE(self):
        '''
        Function to get the number of edges
        @return m: number of edges
        @postcondition: m >= 0, m whole number
        '''
        return self.__m
    
    def isEdge(self, x, y):
        '''
        Checks if there is an edge between the vertices x and y
        @param x: source vertex
        @param y: target vertex
        @raise KeyError: if x, y are not a valid vertices
        @return True: if there is an (directed) edge from x to y
        @return False: otherwise
        '''
        if x not in self.__dictOut.keys() or y not in self.__dictIn.keys():
            raise KeyError
        return y in self.__dictOut[x]
    
    def outDegree(self, x):
        '''
        Function to get the out-degree of a given vertex
        @param x: vertex
        @precondition: 0 <= x < n
        @raise KeyError: if x is not a valid vertex
        @return: outdeg(x)
        '''
        if x not in self.__dictOut.keys():
            raise KeyError
        return len(self.__dictOut[x])

    def inDegree(self, x):
        '''
        Function to get the in-degree of a given vertex
        @param x: vertex
        @precondition: 0 <= x < n
        @raise KeyError: if x is not a valid vertex
        @return: indeg(x)
        '''
        if x not in self.__dictIn.keys():
            raise KeyError
        return len(self.__dictIn[x])
    
    def iterateOut(self, x):
        '''
        Function to iterate through the set of out-bound edges of a specific vertex
        @param x: source vertex
        @precondition: 0 <= x < n
        @raise KeyError: if x is not a valid vertex
        @return: iterator that provides the target vertex of the current edge
        '''
        if x not in self.__dictOut.keys():
            raise KeyError
        return self.__dictOut[x]
    
    def iterateIn(self, y):
        '''
        Function to iterate through the set of in-bound edges of a specific vertex
        @param y: target vertex
        @precondition: 0 <= x < n
        @raise KeyError: if x is not a valid vertex
        @return: iterator that provides the source vertex of the current edge
        '''
        if y not in self.__dictIn.keys():
            raise KeyError
        return self.__dictIn[y]
    
    # optional 2...
    def addEdge(self, x, y):
        '''
        Function to add an edge.
        @param x: edge's source vertex
        @param y: edge's target vertex
        @precondition: 0 <= x, y < n; there is no edge between x and y
        @raise KeyError: if x or y are not valid vertices
        @raise ValueError: if edge (x,y) already exists
        '''
        if x not in self.__dictOut.keys() or y not in self.__dictIn.keys():
            raise KeyError("Invalid vertex (vertices).")
        if self.isEdge(x, y):
            raise ValueError("Edge already exist.")
        self.__dictOut[x].append(y)
        self.__dictIn[y].append(x)
        self.__m += 1
        
    def removeEdge(self, x, y):
        '''
        Function to remove an edge
        @param x: edge's source vertex
        @param y: edge's target vertex
        @precondition: there is an edge between the vertices x and y
        @raise ValueError: if there is no edge between x and y
        '''
        if not self.isEdge(x, y):
            raise ValueError("There is no edge (" + str(x) + ", " + str(y) + ")")
        if y in self.__dictOut[x]:
            self.__dictOut[x].remove(y)
        if x in self.__dictIn[y]:
            self.__dictIn[y].remove(x)
        self.__m -= 1
    
    def addVertex(self, x):
        '''
        Function to add a vertex
        @param x: vertex
        @precondition: the vertex does not exist already
        @raise ValueError: if vertex already exists
        '''
        if x in self.__dictOut.keys():
            raise ValueError("Vertex already exists.")
        self.__dictOut[x] = []
        self.__dictIn[x] = []
        self.__n += 1
        
    def removeVertex(self, x):
        '''
        Function to remove a vertex. This function also removes the edges that are incident to the vertex to be removed
        @param x: vertex to be removed
        @precondition: x is a valid vertex
        @raise KeyError: if x is not a valid vertex
        '''
        if x not in self.__dictOut.keys():
            raise KeyError("Invalid vertex id.")
        edges = [] # stores the edge keys to be removed
        for v in self.__dictOut[x]: # out-bound edges
            e = (x, v)
            edges.append(e)
        for v in self.__dictIn[x]: # in-bound edges
            e = (v, x)
            edges.append(e)
        for e in edges: # remove incident edges
            if self.isEdge(e[0], e[1]):
                self.removeEdge(e[0], e[1])
        del self.__dictOut[x]
        del self.__dictIn[x]
        self.__n -= 1

class DiGraphC(DiGraph):
    def __init__(self, n):
        '''
        Creates a directed graph with n vertices and no edges
        @param n: number of vertices
        @precondition: n > 0, n whole number
        '''
        DiGraph.__init__(self, n)
        self.__edges = {} # (x,y):cost
        
#     def __str__(self):
#         s = "dictOut = " + str(self.__dictOut) + "\n"
#         s += "dictIn = " + str(self.__dictIn) + "\n"
#         s += "edges = " + str(self.__edges) + "\n"
#         return s
    
    def getCost(self, x, y):
        '''
        Function to retrieve the information attached to a specific edge (the cost)
        @param x: edge's source vertex
        @param y: edge's target vertex
        @precondition: there must be an (directed) edge between x and y
        @raise KeyError: if there is no edge between x and y
        @return: cost(x, y)
        '''
        if not self.isEdge(x, y):
            raise KeyError
        return self.__edges[(x, y)]
    
    def setCost(self, x, y, cost):
        '''
        Function to modify the information attached to a specific edge (the cost)
        @param x: edge's source vertex
        @param y: edge's target vertex
        @param cost: edge's new cost
        @precondition: there must be an (directed) edge between x and y
        @raise KeyError: if there is no edge between x and y
        '''
        if not self.isEdge(x, y):
            raise KeyError
        self.__edges[(x, y)] = cost
    
    # optional 2...
    def addEdge(self, x, y):
        '''
        Function to add an edge. This function sets the cost of the edge to 'None'
        @param x: edge's source vertex
        @param y: edge's target vertex
        @precondition: 0 <= x, y < n; there is no edge between x and y
        @raise KeyError: if x or y are not valid vertices
        @raise ValueError: if edge (x,y) already exists
        '''
        DiGraph.addEdge(self, x, y)
        self.__edges[(x, y)] = None
        
    def removeEdge(self, x, y):
        '''
        Function to remove an edge
        @param x: edge's source vertex
        @param y: edge's target vertex
        @precondition: there is an edge between the vertices x and y
        @raise ValueError: if there is no edge between x and y
        '''
        DiGraph.removeEdge(self, x, y)
        if (x, y) in self.__edges.keys():
            del self.__edges[(x, y)]
        
