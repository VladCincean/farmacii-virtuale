class Queue:
    def __init__(self):
        self.__q = []
        
    def enqueue(self, x):
        self.__q.append(x)
        
    def dequeue(self):
        if len(self.__q) == 0:
            return None
        x = self.__q[0]
        self.__q = self.__q[1:]
        return x
        
    def isEmpty(self):
        return len(self.__q) == 0
    
    def __len__(self):
        return len(self.__q)
    
class Stack:
    def __init__(self):
        self.__s = []
        
    def push(self, x):
        self.__s.append(x)
        
    def pop(self):
        if len(self.__s) == 0:
            return None
        x = self.__s.pop()
        return x
    
    def isEmpty(self):
        return len(self.__s) == 0
    
    def __len__(self):
        return len(self.__s)
    
    