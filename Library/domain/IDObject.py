'''
Created on 21 nov. 2015

@author: Vlad
'''

class IDObject(object):
    '''
    Base class for all objects having unique id within the application
    '''


    def __init__(self, objectID):
        '''
        Constructor for IDObject Class
        objectID - the unique objectID of the object in the application
        '''
        self._ID = objectID
        
    def getId(self):
        '''
        Return the object's unique id
        '''
        return self._ID
    
    def setId(self, ID):
        self._ID = ID
    