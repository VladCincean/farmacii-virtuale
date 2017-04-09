from graph import DiGraph
from utils import Queue

class Controller:
    def __init__(self, file):
        '''
        Constructor for controller
        Input: f (string) filename to read a DiGraph from
        '''
        f = open(file, "r")
        n, m = f.readline().strip().split()
        n = int(n); m = int(m)
        self.__dg = DiGraph(n)
        for i in range(m):
            x, y, cost = f.readline().strip().split()
            x = int(x); y = int(y); cost = int(cost)
            self.__dg.addEdge(x, y)
            #self.__dg.setCost(x, y, cost) #! do not
        f.close()
            
    def getGraph(self):
        return self.__dg
        
    def BFS(self, s):
        '''
        Breadth first search algorithm (BFS)
        Input:  s - start vertex
        Output: visited (set) - the set of accessible vertices from s
                prev (dictionary) - each key has as value the vertex
                    that is previous to the key in the BFS path
                dist (dictionary) - each key represent a vertex and has
                    as value the length of the shortest path from s to it
        '''
        visited = set() # set
        q = Queue()     # queue
        prev = {}       # dictionary
        dist = {}       # dictionary
        
        prev[s] = None
        dist[s] = 0
        
        q.enqueue(s)
        while len(q) > 0:
            x = q.dequeue() # get the next element from the queue
            for y in self.__dg.iterateOut(x):
                if y not in visited:
                    visited.add(y)
                    q.enqueue(y)
                    prev[y] = x
                    dist[y] = dist[x] + 1
        
        return visited, prev, dist
        
    def getPath(self, s, t):
        '''
        Finds a lowest length path between given vertices s and t
            by using a forward breadth-first search algorithm
        Input:  s - source vertex
                t - target vertex
        Output: a lowest length path between s and t (list of vertices)
        '''
        if s >= self.__dg.getV() or t >= self.__dg.getV():
            raise KeyError("Invalid vertices.")
        
        path = []
        
        #1. we perform a BFS starting at s (source vertex)
        visited, prev, dist = self.BFS(s)
        
        #2. we check if t (target vertex) is in visited
        #       i.e. there exists a (lowest length) path from s to t
        if t not in visited:
            return None         # there is no path from s to t
        
        #3. we compute the path
#         path.append(v)
#         while v != s:           # while the current vertex is not the start vertex
#             for x in self.__dg.iterateIn(v):
#                 if x in dist and dist[x] == dist[v] - 1:
#                     v = x       # we search in the inbounds of v for a vertex whose path length from s
#                     break       # to it is just 1 unit below the path length from s to the current v
#             path.append(v)      # then, v becomes that vertex and we add it to the path list
            
        v = t                   # we start at t
        path.append(t)
        while v!= s:
            v = prev[v]
            path.append(v)
        #4. we reverse the order of elements in the list 'path'
        path.reverse()
        
        #5. we return the result
        return path
    