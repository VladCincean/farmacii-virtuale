'''
Created on 21 nov. 2015

@author: Vlad
'''

class RepositoryException(Exception):
    def __init__(self, message):
        self._message = message
    def getMessage(self):
        return self._message
    def __str__(self):
        return self._message
    
class DuplicatedIDException(RepositoryException):
    def __init__(self, message = "Error! Duplicated ID!"):
        RepositoryException.__init__(self, message)
        
class InexistentIDException(RepositoryException):
    def __init__(self, message = "Error! Inexistent ID!"):
        RepositoryException.__init__(self, message)

