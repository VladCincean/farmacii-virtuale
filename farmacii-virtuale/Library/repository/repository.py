'''
Created on 10 nov. 2015

@author: Vlad
'''
from repository.RepositoryException import *

class Repository(object):
    '''
    Repository for storing IDObject instances
    '''


    def __init__(self):
        '''
        Constructor for Repository Class
        '''
        self._data=[]
        
    def __len__(self):
        '''
        Overrides the len() built-in function
        '''
        return len(self._data)
    
    def __str__(self):
        '''
        Overrides de str() built-in function
        '''
        r = "Repository:\n"
        for e in self._data:
            r += str(e)
            r += "\n"
        return r
        
    def find(self, ID):
        '''
        Returns the index of the object having the given ID
        Input: ID (integer)
        Output: e - the index of the object having the given ID in the repository, if found
                None, otherwise
        '''
        for i in range(0, len(self._data)):
            if self._data[i].getId() == ID:
                return i
        return None
        
    def add(self, obj):
        '''
        Adds an object to the repository
        Input: obj (object)
        Raises DuplicatedIDException in case of duplicated id
        '''
        if self.find(obj.getId()) != None:
            raise DuplicatedIDException("Error! ID - " + str(obj.getId()) + " already exists!")
        self._data.append(obj)
        
    def update(self, obj):
        '''
        Updates an object
        Input: obj (object)
        Raises RepositoryException in case the object is not contained in the repository
        '''
        done = False
        for i in range(len(self._data)):
            if self._data[i].getId() == obj.getId():
                self._data[i] = obj
                done = True
                break
        if not done:
            raise RepositoryException("Error! Updating not performed.")
        
    def remove(self, objID):
        '''
        Removes the object having the given ID from the repository
        Input: objID (integer)
        Output: obj (Object) - the object that just was removed
        Raises InexistentIDException in case the given ID does not exist
        '''
        obj = self.getById(objID)
        if obj == None:
            raise InexistentIDException("Error! ID - " + str(objID) + " not found!")
        return self._data.pop(self.find(obj.getId()))
        return obj
    
    def removeAll(self):
        '''
        Removes all data from the repository
        '''
        self._data.clear()
        
    def getById(self, ID):
        '''
        Returns the object having the given ID
        Input: ID (integer)
        Output: object (object), if found
                None, otherwise
        '''
        for el in self._data:
            if ID == el.getId():
                return el
        return None
        
    def getAll(self):
        '''
        Returns all the repository's data
        '''
        return self._data
    
    def getNextID(self):
        '''
        Returns the next valid available ID for storing new data
        '''
        nextID = 0
        for obj in self._data:
            if int(obj.getId()) > int(nextID):
                nextID = int(obj.getId())
        nextID += 1
        return nextID
    
class BookRepository(Repository):
    def getByTitle(self, title):
        '''
        Returns the books having the given title (no case sensitive)
        Input: title (string)
        Output: res (list of Books), if found
                None, otherwise
        '''
        res = []
        for entry in self._data:
            if entry.getTitle().lower() == title.lower():
                res.append(entry)
        return res
    
    def getByAuthor(self, author):
        '''
        Returns the books having the given author (no case sensitive)
        Input: author (string)
        Output: res (list of Books), if found
                None, otherwise
        '''
        res = []
        for entry in self._data:
            if entry.getAuthor().lower() == author.lower():
                res.append(entry)
        return res
    
class ClientRepository(Repository):
    def getByName(self, name):
        '''
        Returns the clients having the given name (no case sensitive)
        Input: name (string)
        Output: res (list of Clients), if found
                None, otherwise
        '''
        res = []
        for entry in self._data:
            if entry.getName().lower() == name.lower():
                res.append(entry)
        return res
    
    def getByCNP(self, CNP = ''):
        '''
        Returns the clients having the given CNP
        Input: CNP (string)
        Output: res (list of Clients), if found
                None, otherwise
        '''
        res = []
        for entry in self._data:
            if entry.getCNP() == CNP:
                res.append(entry)
        return res

                    
class RentalRepository(Repository):
    def __init__ (self, aClientRep, aBookRep):
        '''
        Constructor for RentalRepository class
        '''
        self._data = []
        self._clientRepo = aClientRep
        self._bookRepo = aBookRep

    def getAllActive(self):
        res = []
        for rental in self._data:
            if rental.getRentalStatus() == "active":
                res.append(rental)
        return res
    
    def getAllActiveForAClient(self, client):
        '''
        Returns all the active rentals for a given client
        Input: client (Client)
        Output: res (list of Rentals) - all the active rentals for 'client'
        '''
        res = []
        for rental in self._data:
            if rental.getClientId() == client.getId() and rental.getRentalStatus() == "active":
                res.append(rental)
        return res
        
