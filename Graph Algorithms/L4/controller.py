'''
Created on 7 mai 2016

@author: Vlad
'''
from graph import DiGraph
from queue import Queue

class Controller:
    def __init__(self):
        self.__g = DiGraph()    # vertex = activity
        self.__d = {}           # vertex : duration
        self.__ES = {}          # vertex : Earliest Start time
        self.__EF = {}          # vertex : Earliest Finish time
        self.__LS = {}          # vertex : Latest Start time
        self.__LF = {}          # vertex : Latest Finish time
        self.__total = 0        # total time of the project
        
    def initFromFile(self, file):
        f = open(file, "r")
        n = int(f.readline().strip())
        self.__init__()
        self.__g.addVertex("start")
        self.__d["start"] = 0
        self.__g.addVertex("end")
        self.__d["end"] = 0
        for i in range(1, n + 1, 1):
            self.__g.addVertex(i)
            self.__g.addEdge(i, "end")
        L = f.readline().strip().split()
        L = [int(x) for x in L]
        while len(L) > 1:
            self.__d[L[0]] = L[1]
            if len(L) > 2:
                for i in range(2, len(L), 1):
                    self.__g.addEdge(L[i], L[0])
            L = f.readline().strip().split()
            L = [int(x) for x in L]
        f.close()
    
    def clear(self):
        '''
        Clears all the activities and sets the project timing to zero.
        '''
        self.__init__()
    
    def getGraph(self):
        return self.__g
    
    def getDurationOf(self, x):
        if x not in self.__d.keys():
            raise KeyError
        return self.__d[x]
    
    def getES(self, x):
        if x not in self.__ES.keys():
            raise KeyError
        return self.__ES[x]
    
    def getLS(self, x):
        if x not in self.__LS.keys():
            raise KeyError
        return self.__LS[x]
    
    def getProjectTime(self):
        return self.__total
    
    def addActivity(self, act, duration):
        '''
        Add activity 'act' to the graph
        '''
        self.__g.addVertex(act)
        self.__d[act] = duration
        
    def setPrerequisites(self, act, prerequisites):
        '''
        Set the prerequisites for an activity
        Input: act - the activity
               prerequisites (list/iterable)
        '''
        for pre in prerequisites:
            self.__g.addEdge(pre, act)
        
    def toposort(self):
        '''
        Performs a topological sort of the vertices of a directed graph.
        It also checks if the digraph is a DAG.
        Returns: list of graph's vertices in toposort order
                 None, if the graph is NOT a DAG
        '''
        pred = {}
        q = Queue()
        q.put("start")      # put the "dummy" start activity in the queue
        pred["start"] = 0   # just to make sure it is at the beginning of the toposort
        s = []
#         for x in self.__g.iterate():
        for x in [x for x in self.__g.iterate() if x != "start"]:
            count = 0
            for y in self.__g.iterateIn(x):
                count += 1
            pred[x] = count
            if pred[x] == 0:
                q.put(x)
        while not q.empty():
            x = q.get()
            s.append(x)
            for y in self.__g.iterateOut(x):
                pred[y] -= 1
                if pred[y] == 0:
                    q.put(y)
        if len(s) == len(self.__g.iterate()):
            return s
        return None
    
    def computeTiming(self):
        '''
        Computes the timing of the project.
        !! Must be called before any attempt of timing request for an activity / whole project.
        !! After call, NO modification in the activities graph should be made
        Returns: nothing
        Raises: Exception in case the graph is not a DAG (and so, no scheduling can be made)
        '''
        acts = self.toposort()
        if acts == None:
            raise Exception("Error. Not a DAG.")
        
        self.__ES[acts[0]] = 0
        self.__EF[acts[0]] = self.__d[acts[0]]
        for j in range(1, len(acts), 1):
            L = [self.__EF[x] for x in self.__g.iterateIn(acts[j])]
            if len(L) > 0:
                self.__ES[acts[j]] = max(L)
            else:
                self.__ES[acts[j]] = 0
            self.__EF[acts[j]] = self.__ES[acts[j]] + self.__d[acts[j]]
            
        self.__total = self.__EF[acts[-1]]
        
#         self.__LF[acts[len(acts) - 1]] = self.__total
#         self.__LS[acts[len(acts) - 1]] = self.__total - self.__d[acts[len(acts) - 1]]
        self.__LF[acts[-1]] = self.__total
        self.__LS[acts[-1]] = self.__total - self.__d[acts[-1]]
        for i in range(len(acts) - 2, -1, -1):
            L = [self.__LS[x] for x in self.__g.iterateOut(acts[i])]
            if len(L) > 0:
                self.__LF[acts[i]] = min(L)
            else:
                self.__LF[acts[i]] = self.__total
            self.__LS[acts[i]] = self.__LF[acts[i]] - self.__d[acts[i]]
            
    def getCriticalActivities(self):
        '''
        Provides a list of critical activities
        '''
        result = []
        for act in self.__g.iterate():
            if self.__ES[act] == self.__LS[act] and act != "start" and act != "end":
                result.append(act)
        return result
