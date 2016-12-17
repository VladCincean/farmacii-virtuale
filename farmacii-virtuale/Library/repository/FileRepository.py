'''
Created on 29 nov. 2015

@author: Vlad
'''

from repository.repository import *
from domain.book import Book
from domain.client import Client
from domain.rental import Rental
from datetime import *

class FileBookRepository(BookRepository):
    
    def __init__(self, filename = "books.txt"):
        '''
        Constructor for FileBookRepository Class
        '''
        self._fName = filename
        Repository.__init__(self)
        self._nextID = BookRepository.getNextID(self)
        self._loadFromFile()
        
    def add(self, book):
        Repository.add(self, book)
        self._storeToFile()

    def update(self, book):
        Repository.update(self, book)
        self._storeToFile()

    def remove(self, bookID):
        book = Repository.remove(self, bookID)
        self._storeToFile()
        return book
    
    def _storeToFile(self):
        f = open(self._fName, "w")
        self._nextID = BookRepository.getNextID(self)
        f.write(str(self._nextID) + "\n")
        books = BookRepository.getAll(self)
        for book in books:
            ln = str(book.getId()) + " @ " + book.getTitle() + " @ " + book.getAuthor() + " @ " + book.getDescription() + "\n"
            f.write(ln)
        f.close()
        
    def _loadFromFile(self):
        try:
            f = open(self._fName, "r")
        except IOError:
            print("ERROR while trying to open " + self._fName)
        ID = f.readline().strip()
        self._nextID = ID
        ln = f.readline().strip()
        while ln != "":
            t = ln.split(" @ ")
            book = Book(ID = int(t[0]), title = t[1], author = t[2], descr = t[3])
            BookRepository.add(self, book)
            ln = f.readline().strip()
        f.close

class FileClientRepository(ClientRepository):
    
    def __init__(self, filename = "clients.txt"):
        '''
        Constructor for FileClientRepository Class
        '''
        self._fName = filename
        Repository.__init__(self)
        self._nextID = ClientRepository.getNextID(self)
        self._loadFromFile()
        
    def add(self, client):
        Repository.add(self, client)
        self._storeToFile()

    def update(self, client):
        Repository.update(self, client)
        self._storeToFile()

    def remove(self, clientID):
        client = Repository.remove(self, clientID)
        self._storeToFile()
        return client
    
    def _storeToFile(self):
        f = open(self._fName, "w")
        self._nextID = BookRepository.getNextID(self)
        f.write(str(self._nextID) + "\n")
        clients = ClientRepository.getAll(self)
        for client in clients:
            ln = str(client.getId()) + " @ " + client.getName() + " @ " + client.getCNP() + "\n"
            f.write(ln)
        f.close()
        
    def _loadFromFile(self):
        try:
            f = open(self._fName, "r")
        except IOError:
            print("ERROR while trying to open " + self._fName)
        ID = f.readline().strip()
        self._nextID = ID
        ln = f.readline().strip()
        while ln != "":
            t = ln.split(" @ ")
            client = Client(ID = int(t[0]), name = t[1], CNP = str(t[2]))
            ClientRepository.add(self, client)
            ln = f.readline().strip()
        f.close
        
class FileRentalRepository(RentalRepository):
    
    def __init__(self, bookRepo, clientRepo, filename = "rentals.txt"):
        '''
        Constructor for FileClientRepository Class
        '''
        self._fName = filename
        Repository.__init__(self)
        self._nextID = RentalRepository.getNextID(self)
#         self._bRepo = bookRepo
#         self._cRepo = clientRepo
        self._loadFromFile()
        
    def add(self, rental):
        Repository.add(self, rental)
        self._storeToFile()

    def update(self, rental):
        Repository.update(self, rental)
        self._storeToFile()

    def remove(self, rentalID):
        client = Repository.remove(self, rentalID)
        self._storeToFile()
        return client
    
    def _storeToFile(self):
        f = open(self._fName, "w")
        self._nextID = BookRepository.getNextID(self)
        f.write(str(self._nextID) + "\n")
        rentals = RentalRepository.getAll(self)
        for rental in rentals:
            ln = str(rental.getId()) + " @ " + str(rental.getClientId()) + " @ " + str(rental.getBookId()) + " @ "
            ln += rental.getStartDate().strftime("%Y-%m-%d") + " @ " + rental.getEndDate().strftime("%Y-%m-%d") + " @ " + rental.getRentalStatus() + "\n"
            f.write(ln)
        f.close()
        
    def _loadFromFile(self):
        try:
            f = open(self._fName, "r")
        except IOError:
            print("ERROR while trying to open " + self._fName)
        ID = f.readline().strip()
        self._nextID = ID
        ln = f.readline().strip()
        while ln != "":
            t = ln.split(" @ ")
            st = datetime.strptime(t[3], "%Y-%m-%d").date()
            end = datetime.strptime(t[4], "%Y-%m-%d").date()
            rental = Rental(int(t[0]), int(t[1]), int(t[2]), st, end, active = t[5])
            RentalRepository.add(self, rental)
            ln = f.readline().strip()
        f.close()
