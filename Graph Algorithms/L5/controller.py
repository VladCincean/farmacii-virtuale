from graph import Graph
from copy import deepcopy
from random import randint, shuffle
from queue import PriorityQueue

class Controller:
    def __init__(self):
        '''
        Constructor for controller
        '''
        self.__g = Graph()
#         self.initGraph()
        
    def initGraph(self):
        self.__g = Graph()
        self.__g.addVertex(1)
        self.__g.addVertex(2)
        self.__g.addVertex(3)
        self.__g.addVertex(4)
        self.__g.addEdge(1, 2)
        self.__g.addEdge(2, 3)
        self.__g.addEdge(3, 4)
        self.__g.addEdge(4, 1)
        self.__g.addEdge(1, 3)
        self.__g.addEdge(2, 4)
        
    def loadGraph(self, vertices, edges):
        self.__g = Graph()
        for v in vertices:
            if v not in self.__g.iterate():
                self.__g.addVertex(v)
        for e in edges:
            if not self.__g.isEdge(e[0], e[1]):
                self.__g.addEdge(e[0], e[1])
            
    def getGraph(self):
        return self.__g
        
    def approxVertexCover(self):
        g = deepcopy(self.__g)
        S = []
        E = []
        for u in g.iterate():
            E += [[u, v] for v in g.iterateX(u) if [v, u] not in E]
        while E != []:
            pos = randint(0, len(E) - 1)
            u = E[pos][0]
            v = E[pos][1]
            S += [u, v]
            copyOfE = E[:]
            for edge in copyOfE:
                if u in edge or v in edge:
                    E.remove(edge)
        return S
            
    def cleverGreedy(self):
        g = deepcopy(self.__g)
        C = []
        E = []  # all edges
        for u in g.iterate():
            E += [[u, v] for v in g.iterateX(u) if [v, u] not in E]
        D = {} 
        for u in g.iterate():
            D[u] = g.degree(u)
        while E != []:
            maxDeg = max(list(D.values()))
            v = None
            for i in list(D.keys()):
                if D[i] == maxDeg:
                    v = i
                    break
            if v == None:
                break
            C.append(v)
            copyOfE = E[:]
            for edge in copyOfE:
                if v in edge:
                    D[edge[0]] -= 1
                    D[edge[1]] -= 1
                    E.remove(edge)
            del D[v]
        return C
    
#     def branchAndBound(self):
#         g = deepcopy(self.__g)
#         best = g.getN()      # or, is it better +infinity ?? math.inf
#         subProb = []
#         pass
    
    def Alom(self, g = None):
        if g == None:
            g = deepcopy(self.__g)
        A = []
        E = []              # all edges
        V = g.iterate()     # all vertices
        for u in V:
            E += [[u, v] for v in g.iterateX(u) if [v, u] not in E]
        D = {}              # vertex : degree of the current configuration
        for u in V:
            D[u] = g.degree(u)
        while E != []:
            maxDeg = max(list(D.values()))
            verticesOfMaxDeg = []
            for i in D.keys():
                if D[i] == maxDeg:
                    verticesOfMaxDeg.append(i)
            # now, choose a vertex of max degree which has at least one incident edge that is not
            # covered by other vertices of max degree, or an arbitrary one if no such vertex found
            shuffle(verticesOfMaxDeg)
            v = verticesOfMaxDeg[0]
            for i in verticesOfMaxDeg:
                x = 0
                for j in V:
                    if [i, j] in E or [j, i] in E:
                        if j in verticesOfMaxDeg:
                            x += 1
                if x < maxDeg:
                    v = i
                    break
            A.append(v)             # add v to solution
            copyOfE = E[:]
            for edge in copyOfE:
                if v in edge:
                    D[edge[0]] -= 1
                    D[edge[1]] -= 1
                    E.remove(edge)  # remove incident edges on v
            del D[v]                # remove key v from degrees map
            V.remove(v)             # remove v from V (all vertices)
        return A

    def AlomExtended(self):
        A = self.__g.iterate()      # first, initiate A with all vertices
        for v in self.__g.iterate():
#         for v in range(10):
            g = deepcopy(self.__g)
            g.removeVertex(v)
            Ap = self.Alom(g)
            Ap += [v]
            if len(Ap) < len(A):
                A = Ap[:]
        return A
    
    def isCover(self, cover):
        g = deepcopy(self.__g)
        for v in cover:
            g.removeEdge(v)
        if g.getM() == 0:
            return True
        return False          

    def generateAndTest(self):
        g = deepcopy(self.__g)
        # generate the first 2^n - 1 binary numbers
        N = []
        for i in range(g.getN() + 1):
            N += [x for x in range(1 << g.getN()) if bin(x).count("1") == i]
        for i in range(len(N)):
            S = []
            for j in range(g.getN() + 1):
                if 2 ** j & N[i] != 0:
                    S += [g.iterate()[j]]
            s = deepcopy(g)
            for v in S:
                s.removeVertex(v)
            if s.getM() == 0:
                return S
    
    def branchAndBound_Test(self):
        g = deepcopy(self.__g)
        current = self.approxVertexCover()()    # current best solution
        LB = len(current) // 2                  # lower bound
        UB = len(current)                       # upper bound
        q = PriorityQueue() # m (nb. of edges) is the priority
            # (sub-cover, available vertices, remaining vertices, current lower bound)
        q.put((None, tuple(g.iterate()), tuple(g.iterate()), LB), g.getM())
        
        while not q.empty():
            subP = q.pop()
            
            if subP[0] == None:
                subCover = []
            else:
                subCover = list(subP[0])
            
            availableVertices = subP[1]
            remainingGraph = subP[2] #...
            currentLB = subP[3]
            
    def branchAndBound(self):
        g = deepcopy(self.__g)
        current = self.approxVertexCover()()    # current best solution
        LB = len(current) // 2                  # lower bound
        UB = len(current)                       # upper bound
        q = PriorityQueue()
#         q.put(((tuple(g.iterate()), tuple(g.iterate()), LB), g.getM()))
        # (sub-cover)
        q.put((list()), g.getM())
        while not q.empty():
            subP = q.pop()
            subCover = list(subP[0])
            
            
