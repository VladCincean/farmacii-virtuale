'''
Created on 4 nov. 2015

@author: Vlad
'''
from controller.UndoableOperations import *
from domain.book import *
from domain.client import *
from domain.rental import *

from utils.lab10 import *

class Controller(object):
    '''
    Controller for controlling IOObject instances
    '''

    def __init__(self, repo, undoController, validator):
        '''
        Constructor for BookController class
        Input: repo (Repository) - the repository 
               undoController (UndoController)
        '''
        self._repo = repo
        self._undoController = undoController
        self._validator = validator
        self._operations = []
        self._index = 0
        
    def add(self, obj):
        '''
        Adds an object
        Input: obj (Object)
        '''
        self._validator.validate(obj)
        self._repo.add(obj)
        
        ''' record for undo/redo '''
        self._operations.append(AddOperation(obj))
        self._index += 1
        self._undoController.recordUpdatedControllers([self])
        
    def update(self, obj):
        '''
        Updates an object
        Input: obj (Object)
        '''
        oldObj = self._repo.getById(obj.getId())
        self._validator.validate(obj)
        self._repo.update(obj)
        
        ''' record for undo/redo '''
        self._operations.append(UpdateOperation(oldObj, obj))
        self._index += 1
        self._undoController.recordUpdatedControllers([self])
        
    def getById(self, ID):
        '''
        Returns the entity having the given ID
        Input: ID (integer)
        Output: entity (Object), if found
                None, otherwise
        '''
        return self._repo.getById(ID)
        
    def getAll(self):
        '''
        Returns all the repository's data
        '''
        return self._repo.getAll()
    
    def undo(self):
        '''
        Undo the last operation that changed the list of objects the controllers acts on
        Output: True, if operation was undone
                False, otherwise
        Raises Exception in case undo not performed
        '''
        if self._index == 0:
            return False
        
        self._index -= 1
        operation = self._operations[self._index]
        if isinstance(operation, AddOperation):
            self._repo.remove(operation.getObject().getId())
        elif isinstance(operation, RemoveOperation):
            self._repo.add(operation.getObject())
        elif isinstance(operation, UpdateOperation):
            self._repo.update(operation.getOldObject())
        else:
            self._index += 1
            raise Exception("Error! The last performed operation was NOT undone.")
    
    def redo(self):
        '''
        Redo the last undone change in the list of objects the controllers acts on
        Output: True, if operation was redone
                False, otherwise
        Raises Exception in case redo not performed
        '''
        if self._index >= len(self._operations):
            return False
        
        operation = self._operations[self._index]
        if isinstance(operation, AddOperation):
            self._repo.add(operation.getObject())
            self._index += 1
        elif isinstance(operation, RemoveOperation):
            self._repo.remove(operation.getObject().getId())
            self._index += 1
        elif isinstance(operation, UpdateOperation):
            self._repo.update(operation.getUpdatedObject())
            self._index += 1
        else:
            self._index -= 1
            raise Exception("Error! Cannot redo the last undone change!")
            
class BookController(Controller):
    def remove(self, ID):
        '''
        Removes the book having the given ID
        Input: objID (integer)
        '''
        book = Book(ID, self.getById(ID).getTitle(), self.getById(ID).getDescription(), self.getById(ID).getAuthor())
        self._repo.remove(ID)
        
        '''record for undo/redo '''
        self._operations.append(RemoveOperation(book))
        self._index += 1
        self._undoController.recordUpdatedControllers([self])
    
    def getByTitle(self, title):
        '''
        Returns the books having the given title
        Input: title (string)
        Output: res (list of Books), if found
                None, otherwise
        '''
        return self._repo.getByTitle(title)

    def getByAuthor(self, author):
        '''
        Returns the books having the given title
        Input: author (string)
        Output: res (list of Books), if found
                None, otherwise
        '''
        return self._repo.getByAuthor(author)
    
class ClientController(Controller):
    def remove(self, ID):
        '''
        Removes the client having the given ID
        Input: ID (integer)
        '''
        client = Client(ID, self.getById(ID).getName(), self.getById(ID).getCNP())
        self._repo.remove(ID)
        
        '''record for undo/redo '''
        self._operations.append(RemoveOperation(client))
        self._index += 1
        self._undoController.recordUpdatedControllers([self])
    
    def getByName(self, name):
        '''
        Returns the clients having the given name
        Input: name (string)
        Output: res (list of Clients), if found
                None, otherwise
        '''
        return self._repo.getByName(name)

    def getByCNP(self, CNP):
        '''
        Returns the clients having the given CNP
        Input: CNP (integer)
        Output: res (list of Clients), if found
                None, otherwise
        '''
        return self._repo.getByCNP(CNP)
        
class RentalController(Controller):
    def __init__(self, aRentalRep, aClientRep, aBookRep, undoController, validator):
        '''
        Constructor for RentalController class
        '''
        self._cRepo = aClientRep
        self._bRepo = aBookRep
        self._repo = aRentalRep
        self._undoController = undoController
        self._operations = []
        self._index = 0
        self._validator = validator
    
    def setRentalStatus(self, rental, status):
        for r in self._repo:
            if self == rental:
                r.setStatus(status)
                return
    
    def getAllActive(self):
        return self._repo.getAllActive()
    
    def getAllActiveForAClient(self, client):
        '''
        Returns all the active rentals for a given client
        Input: client (Client)
        Output: res (list of Rentals) - all the active rentals for 'client'
        '''
        return self._repo.getAllActiveForAClient(client)
    
    def getRentalByBook(self, book):
        '''
        Returns the active rental for a given book
        Input: book (Book)
        Output: rental (Rental)
        Raises Exception if no rental found
        '''
        rental = None
        for r in self._repo.getAllActive():
            if r.getBookId() == book.getId():
                rental = r
                break
        if rental != None:
            return rental
        else:
            raise Exception("Error! No rental found!")
        
    def isBookRented(self, book):
        '''
        Checks if a book is rented; if so, returns the deadline of the rental
        Input: book (Book)
        Output: deadline (Date), in case the book is rented
                False, in case the book is available for rental
        '''
        for rental in self._repo.getAllActive():
            if rental.getBookId() == book.getId():
                return rental.getEndDate()
        return False
    
    @staticmethod
    def checkClient(rental, clientId):
        '''
        Check if the client with the id 'clientId' made the rental 'rental'
        Input: rental (Rental)
               clientId (integer)
        Output: True/False
        '''
        if rental.getClientId() == clientId:
            return True
        return False
    
    @staticmethod
    def checkBook(rental, bookId):
        '''
        Check if the book with the id 'bookId' was rented in the rental 'rental'
        Input: rental (Rental)
               bookId (integer)
        Output: True/False
        '''
        if rental.getBookId() == bookId:
            return True
        return False
    
    def filterRentals(self, client, book):
        '''
        Returns a list of rentals performed by the given client for the given book
        Input: client (Client) - the client performing the rental
                       None -> use all clients
               book (Book) - the rented book
                     None -> use all books
        Output: res (list) - the filtered list of rentals
        '''
        if client == None and book == None:
            return self._repo.getAll()
        elif book == None:
            return myFilter(self._repo.getAll(), self.checkClient, client.getId())
        elif client == None:
            return myFilter(self._repo.getAll(), self.checkBook, book.getId())
        
    @staticmethod
    def statUtil(tuple1, tuple2):
        '''
        Input: tuplei
                tuplei[0] - book or client
                tuplei[1] - number of times of rent
                    i=1,2
        ''' 
        if tuple1[1] - tuple2[1] < 0:
            return -1
        elif tuple1[1] - tuple2[1] == 0:
            return 0
        elif tuple1[1] - tuple2[1] > 0:
            return 1
    
    def mostRentedBooks(self, how_many):
        '''
        Returns an ordered list of the most rented books (by the number of times each book was rented)
        Input: how_many (integer) - the maximum lenght of the output list
        Output: res (list of tuples) - the ordered list  of the most rented books
                res[i][0] = the book
                res[i][1] = the number of times the book was rented
        '''
        res = []
        
        ''' 1. Building the DTO '''
        for book in self._bRepo.getAll():
            n = len(self.filterRentals(None, book))
            res.append((book, n))
        
        """
        ''' 2. Sorting the result (insertion sort) '''
        for i in range (len(res)-1):
            j = i+1
            aux = res[j]
            while j > 0 and aux[1] > res[j-1][1]:
                res[j] = res[j-1]
                j -= 1
            res[j] = aux
        """
        
        '''2. Sort the result using mySort '''
        mySort(L = res, cmpF = self.statUtil, reverse = True)
        
        return res[:how_many]
    
    def mostActiveClients(self, how_many):
        '''
        Returns an ordered list of the most active clients (by the number of rentals made)
        Input: how_many (integer) - the maximum lenght of the output list
        Output: res (list of tuples) - the ordered list  of the most active clients
                res[i][0] = the client
                res[i][1] = the number of rentals the client has made
        '''
        res = []
        
        ''' 1. Build the DTO '''
        for client in self._cRepo.getAll():
            n = len(self.filterRentals(client, None))
            res.append((client, n))
            
        """
        ''' 2. Sorting the result (insertion sort) '''
        for i in range (len(res)-1):
            j = i+1
            aux = res[j]
            while j > 0 and aux[1] > res[j-1][1]:
                res[j] = res[j-1]
                j -= 1
            res[j] = aux
        """
        '''2. Sort the result using mySort '''
        mySort(L = res, cmpF = self.statUtil, reverse = True)
        
        return res[:how_many]
    
    def removeAllForABook(self, book):
        for rental in self._repo.getAll():
            if rental.getBookId() == book.getId():
                self._repo.remove(rental.getId())
                
    def removeAllForAClient(self, client):
        for rental in self._repo.getAll():
            if rental.getClientId() == client.getId():
                self._repo.remove(rental.getId())
                
