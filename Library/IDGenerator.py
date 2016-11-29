'''
Created on 21 nov. 2015

@author: Vlad
'''

class IDGenerator(object):
    '''
    Manages the allocation of unique IDs for objects
    '''


    def __init__(self, firstID):
        '''
        Constructor for IDGenerator class
        Input: firstID (integer) - The first valid ID. The following IDs are increased by 1 consequently
        '''
        self._nextID = firstID -1
        
    def getNextID(self):
        '''
        Returns the next valid and unique ID
        Output: the next valid and unique ID
        '''
        self._nextID += 1
        return self._nextID