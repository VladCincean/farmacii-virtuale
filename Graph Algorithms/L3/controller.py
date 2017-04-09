from graph import DiGraphC # DiGraph with costs
from queue import PriorityQueue

class Controller:
    def __init__(self, file):
        '''
        Constructor for controller
        Input: f (string) filename to read a DiGraph from
        '''
        f = open(file, "r")
        n, m = f.readline().strip().split()
        n = int(n); m = int(m)
        self.__dg = DiGraphC(n)
        for i in range(m):
            x, y, cost = f.readline().strip().split()
            x = int(x); y = int(y); cost = int(cost)
            self.__dg.addEdge(x, y)
            self.__dg.setCost(x, y, cost)
        f.close()
            
    def getGraph(self):
        return self.__dg
        
    def getWalk(self, s, t):
        '''
        Finds the lowest cost walk between two given vertices
            by using a "backwards" Dijkstra algorithm
        Input: s - source vertex
               t - target vertex
        Output: a lowest cost walk between s and t (list of vertices)
        '''
    #Step 1. apply "backwards" Dijkstra algorithm
        q = PriorityQueue()
        pred = {}
        dist = {}
        q.put(s, 0) # second argument is priority
        dist[s] = 0
        found = False
        while not q.empty() and not found:
            x = q.get()
            for y in self.__dg.iterateOut(x):
                if y not in dist.keys() or dist[x] + self.__dg.getCost(x, y) < dist[y]:
                    dist[y] = dist[x] + self.__dg.getCost(x, y)
                    q.put(y, dist[y]) # second argument is priority
                    pred[y] = x
            if x == t:
                found = True
        
        #Step 2. get the walk
        walk = []
        walk.append(t)
        if t not in pred.keys():
            return None, None
        x = pred[t]
        while x != s:
            walk.append(x)
            x = pred[x]
        walk.append(s)
        
        #Step 3. return the walk
        return walk, dist[s]
    
