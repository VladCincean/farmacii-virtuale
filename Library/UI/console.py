'''
Created on 2 nov. 2015

@author: Vlad
'''

from domain.book import *
from domain.client import *
from domain.rental import *
from domain.ValidatorException import ValidatorException
from repository.RepositoryException import *
from IDGenerator import IDGenerator
from datetime import date, timedelta

deadline = date.today() + timedelta(days = 14)

clientValidator = ClientValidator()
bookValidator = BookValidator()

class Console(object):
    '''
    Console-based User Interface
    '''

    def __init__(self, aBookCtrl, aClientCtrl, aRentalCtrl, aUndoCtrl, bID, cID, rID):
        '''
        Constructor for Console class
        Input: aBookCtrl (BookController)
               aClientCtrl (ClientController)
               aRentalCtrl (RentalController)
               aUndoCtrl (UndoController)
        '''
        self._bookCtrl = aBookCtrl
        self._clientCtrl= aClientCtrl
        self._rentalCtrl = aRentalCtrl
        self._undoCtrl = aUndoCtrl
        self._bookIDGenerator = IDGenerator(int(bID))
        self._clientIDGenerator = IDGenerator(int(cID))
        self._rentalIDGenerator = IDGenerator(int(rID))
        
    def _printMenu(self):
        menu = "\nWelcome! \n"
        menu += "1 - Book management \n"
        menu += "2 - Client management \n"
        menu += "3 - Library (rental manager) \n"
        menu += "4 - Statistics \n"
        if self._undoCtrl.undo():
            self._undoCtrl.redo()
            menu += "u - UNDO \n"
        if self._undoCtrl.redo():
            self._undoCtrl.undo()
            menu += "r - REDO \n"
        menu += "0 - EXIT \n"
        print(menu)
     
    def _printSubmenu12(self):
        menu = "\nAvailable commands: \n"
        menu += "1 - ADD \n"
        menu += "2 - REMOVE \n"
        menu += "3 - UPDATE \n"
        menu += "4 - LIST \n"
        menu += "5 - SEARCH \n"
        menu += "0 - EXIT \n"
        print(menu)
        
    def _printSubmenu3(self):
        menu = "\nAvailable commands: \n"
        menu += "1 - RENT \n"
        menu += "2 - RETURN \n"
        menu += "3 - print all RENTALS \n"
        menu += "4 - print all ACTIVE rentals \n"
        menu += "0 - EXIT \n"
        print(menu)
        
    def _printSubmenu4(self):
        menu = "\nAvailable commands: \n"
        menu += "1 - Most rented books \n"
        menu += "2 - Most active clients \n"
        menu += "0 - EXIT \n"
        print(menu)
        
    def _addBookMenu(self):
        book = self._readBook()
        self._bookCtrl.add(book)
        
    def _addClientMenu(self):
        client = self._readClient()
        self._clientCtrl.add(client)
        
    def _removeBookMenu(self):
        ID = self._readPositiveInteger("Book ID you want to remove:")
        if self._bookCtrl.getById(ID) != None:
            if not self._rentalCtrl.isBookRented(self._bookCtrl.getById(ID)):
                self._bookCtrl.remove(ID)
            else:
                print("Warning! You cannot remove a rented book!")
        else:
            raise InexistentIDException("Error! Invalid book ID.")
        
    def _removeClientMenu(self):
        ID = self._readPositiveInteger("Client ID you want to remove:")
        if self._clientCtrl.getById(ID) != None:
            if len(self._rentalCtrl.getAllActiveForAClient(self._clientCtrl.getById(ID))) == 0:
                self._clientCtrl.remove(ID)
            else:
                print("Warning! You cannot delete a client that has active rentals")
        else:
            raise InexistentIDException("Error! Invalid client ID.")
        
    def _updateBookMenu(self):
        if len(self._bookCtrl.getAll()) != 0:
            ID = Console._readPositiveInteger("ID of book you want to update: ")
            book = self._bookCtrl.getById(ID)
            if book != None:
                print("The selected book is: \n")
                print(book)
                if self._rentalCtrl.isBookRented(book):
                    print("Unfortunately, the selected book is rented and you cannot update it.")
                else:
                    print("Leave every field empty unless you want to update it")
                    title = input("New title: ").strip()
                    if len(title) == 0:
                        title = book.getTitle()
                    author = input("New author: ").strip()
                    if len(author) == 0:
                        author = book.getAuthor()
                    descr = input("New description: ").strip()
                    if len(descr) == 0:
                        descr = book.getDescription()
                    book2 = Book(ID, title, descr, author)
                    self._bookCtrl.update(book2)
            else:
                raise InexistentIDException("Invalid ID!")
        else:
            raise RepositoryException("Error! The book list is empty.")
        
    def _updateClientMenu(self):
        if len(self._clientCtrl.getAll()) != 0:
            ID = Console._readPositiveInteger("ID of client you want to update: ")
            client = self._clientCtrl.getById(ID)
            if client != None:
                print("The selected client is: \n")
                print(client)
                print("Leave every field empty unless you want to update it")
                name = input("New name: ").strip()
                if len(name) == 0:
                    name = client.getName()
                while True:
                    CNP = str(input("CNP: "))
                    if len(CNP) > 0:
                        try:
                            clientValidator.validateCNP(CNP)
                            break
                        except ValidatorException:
                            print("Wrong CNP!")
                    else:
                        CNP = client.getCNP()
                client2 = Client(ID, name, CNP)
                self._clientCtrl.update(client2)
            else:
                raise InexistentIDException("Invalid ID!")
        else:
            raise RepositoryException("Error! The client list is empty.")
            
    def _printList(self, lst):
        if len(lst) != 0:
            for entry in lst:    
                print(entry)
        else:
            print("Nothing here..")

    def _searchBookMenu(self):
        if len(self._bookCtrl.getAll()) != 0:
            menu = "SEARCH for a book: \n"
            menu += "1 - by id \n"
            menu += "2 - by title \n"
            menu += "3 - by author \n"
            menu += "0 - return \n"
            print(menu)
            while True:
                cmd = input("Enter command: ").strip()
                if cmd == '0':
                    return
                elif cmd == '1':
                    ID = Console._readPositiveInteger("ID: ")
                    book = self._bookCtrl.getById(ID)
                    if book != None:
                        print("Result: \n")
                        print(book)
                        if self._rentalCtrl.isBookRented(book):
                            print("    Status: Rented until " + self._rentalCtrl.isBookRented(book).strftime("%A %d, %B %Y"))
                        else:
                            print("    Status: Available")
                        return
                    else:
                        print("Nothing found..")
                        return
                elif cmd == '2':
                    title = input("Title: ").strip()
                    res = self._bookCtrl.getByTitle(title)
                    if res != None:
                        print("Result: \n")
                        if len(res) != 0:
                            for book in res:    
                                print(book)
                                if self._rentalCtrl.isBookRented(book):
                                    print("    Status: Rented until " + self._rentalCtrl.isBookRented(book).strftime("%A %d, %B %Y"))
                                else:
                                    print("    Status: Available")
                        else:
                            print("Nothing here..")
                        return
                    else:
                        print("Nothing found..")
                        return
                elif cmd == '3':
                    author = input("Author: ").strip()
                    res = self._bookCtrl.getByAuthor(author)
                    if res != None:
                        print("Result: \n")
                        if len(res) != 0:
                            for book in res:    
                                print(book)
                                if self._rentalCtrl.isBookRented(book):
                                    print("    Status: Rented until " + self._rentalCtrl.isBookRented(book).strftime("%A %d, %B %Y"))
                                else:
                                    print("    Status: Available")
                        else:
                            print("Nothing here..")
                        return
                    else:
                        print("Nothing found..")
                        return
                else:
                    print("Wrong command!")
        else:
            raise Exception("Error! The book list is empty.")
            
    def _searchClientMenu(self):
        if len(self._clientCtrl.getAll()) != 0:
            menu = "SEARCH for a client: \n"
            menu += "1 - by id \n"
            menu += "2 - by name \n"
            menu += "3 - by CNP \n"
            menu += "0 - return to client manager \n"
            print(menu)
            while True:
                cmd = input("Enter command: ").strip()
                if cmd == '0':
                    return
                elif cmd == '1':
                    ID = Console._readPositiveInteger("ID: ")
                    client = self._clientCtrl.getById(ID)
                    if client != None:
                        print("Result: \n")
                        print(client)
                        return
                    else:
                        print("Nothing found..")
                        return
                elif cmd == '2':
                    name = input("Name: ").strip()
                    res = self._clientCtrl.getByName(name)
                    if res != None:
                        print("Result: \n")
                        self._printList(res)
                        return
                    else:
                        print("Nothing found..")
                        return
                elif cmd == '3':
                    CNP = input("CNP: ").strip()
                    res = self._clientCtrl.getByCNP(CNP)
                    if res != None:
                        print("Result: \n")
                        self._printList(res)
                        return
                    else:
                        print("Nothing found..")
                        return
                else:
                    print("Wrong command!")
        else:
            raise Exception("Error! The client list is empty.")
    
    def _submenu1(self):
        ''' Book management menu '''
        print("Loading book manager...")
        close_mng = False
        while not close_mng:
            self._printSubmenu12()
            cmd = input("Enter command:").strip()
            if cmd == '0':
                print("Closing book manager...")
                close_mng = True
            elif cmd == '1':
                try:
                    self._addBookMenu()
                    print("The book was added.")
                except ValidatorException as msg:
                    print(msg)
            elif cmd == '2':
                try:
                    self._removeBookMenu()
                    print("The book was removed.")
                except InexistentIDException as msg:
                    print(msg)
            elif cmd == '3':
                try:
                    self._updateBookMenu()
                    print("The book was updated")
                except RepositoryException as msg:
                    print(msg)
            elif cmd == '4':
                print("Books: \n")
                if len(self._bookCtrl.getAll()) != 0:
                    for book in self._bookCtrl.getAll():    
                        print(book)
                        if self._rentalCtrl.isBookRented(book):
                            print("    Status: Rented until " + self._rentalCtrl.isBookRented(book).strftime("%A %d, %B %Y"))
                        else:
                            print("    Status: Available")
                else:
                    print("Nothing here..")
            elif cmd == '5':
                self._searchBookMenu()
            else:
                print("Wrong command!")

    def _submenu2(self):
        ''' Client management menu '''
        print("Loading client manager...")
        close_mng = False
        while not close_mng:
            self._printSubmenu12()
            cmd = input("Enter command:").strip()
            if cmd == '0':
                print("Closing client manager...")
                close_mng = True
            elif cmd == '1':
                try:
                    self._addClientMenu()
                    print("The client was added.")
                except ValidatorException as msg:
                    print(msg)
            elif cmd == '2':
                try:
                    self._removeClientMenu()
                    print("The client was removed.")
                except InexistentIDException as msg:
                    print(msg)
            elif cmd == '3':
                try:
                    self._updateClientMenu()
                    print("The client was updated")
                except RepositoryException as msg:
                    print(msg)
                except ValidatorException as msg:
                    print("Error! The client was NOT updated.")
                    print(msg)
            elif cmd == '4':
                print("Clients: \n")
                self._printList(self._clientCtrl.getAll())
            elif cmd == '5':
                self._searchClientMenu()
            else:
                print("Wrong command!")
    
    def _submenu3(self):
        ''' Rental manager submenu '''
        print("Loading library manager...")
        close_mng = False
        while not close_mng:
            self._printSubmenu3()
            cmd = input("Enter command:").strip()
            if cmd == '0':
                print("Closing library manager...")
                close_mng = True
            elif cmd == '1':
                self._submenu31()
            elif cmd == '2':
                self._submenu32()
            elif cmd == '3':
                print("All rentals: \n")
                L = self._rentalCtrl.getAll()
                for rental in L:
                    print("Rental #", rental.getId())
                    print("    Client ID ", rental.getClientId(), "-",  self._clientCtrl.getById(rental.getClientId()).getName())
                    print("    Book ID ", rental.getBookId(), "-", self._bookCtrl.getById(rental.getBookId()).getTitle() + ", " + self._bookCtrl.getById(rental.getBookId()).getAuthor())
                    print("    Start date: ", rental.getStartDate().strftime("%A %d, %B %Y"))
                    print("    Deadline: ", rental.getEndDate().strftime("%A %d, %B %Y"))
            elif cmd == '4':
                print("Active rentals: \n")
                L = self._rentalCtrl.getAllActive()
                for rental in L:
                    print("Rental #", rental.getId())
                    print("    Client ID ", rental.getClientId(), "-",  self._clientCtrl.getById(rental.getClientId()).getName())
                    print("    Book ID ", rental.getBookId(), "-", self._bookCtrl.getById(rental.getBookId()).getTitle() + ", " + self._bookCtrl.getById(rental.getBookId()).getAuthor())
                    print("    Start date: ", rental.getStartDate().strftime("%A %d, %B %Y"))
                    print("    Deadline: ", rental.getEndDate().strftime("%A %d, %B %Y"))
            else:
                print("Wrong command!")

    def _submenu31(self):
        executa = True
        while executa:
            print("Enter client ID or enter 0 (zero) to cancel")
            client = None
            while client == None:
                ID = Console._readPositiveInteger("Client ID: ")
                if ID != 0:
                    client = self._clientCtrl.getById(ID)
                    if client == None:
                        print("Error! Invalid client ID.")
                else:
                    break
            if ID == 0:
                executa = False
            else:
                print("Client: " + client.getName())
                terminate = False
                while not terminate:
                    found_book = False
                    while not found_book:
                        self._searchBookMenu()
                        while True:
                            a = input("Found the book you are searching for? (Y/N) ").lower().strip()
                            if a == 'y' or a == 'yes':
                                found_book = True
                                break
                            elif a == 'n' or a == 'no':
                                break
                            else:
                                print("Wrong command!")
                    if found_book:
                        print("Enter the book ID that the client want to rent or enter 0 (zero) to cancel")
                        book = None
                        while book == None:
                            ID = Console._readPositiveInteger("Book ID: ")
                            if ID != 0:
                                book = self._bookCtrl.getById(ID)
                                if book == None:
                                    print("Error! Invalid book ID.")
                                else:
                                    if self._rentalCtrl.isBookRented(book) != False:
                                        print("Error! The selected book CANNOT be rented.")
                                        book = None
                            else:
                                break
                    if ID == 0:
                        terminate = True
                    else:
                        try:
                            if len(self._rentalCtrl.getAllActiveForAClient(client)) < 4:
                                ID = self._rentalIDGenerator.getNextID()
                                rental = Rental(ID, client.getId(), book.getId(), date.today(), deadline)
                                if not self._rentalCtrl.isBookRented(book):
                                    self._rentalCtrl.add(rental)
                                    print("The book was rented until " + deadline.strftime("%A %d, %B %Y"))
                                else:
                                    print("Error! The selected book is already rented")
                            else:
                                print("Error! The client CANNOT rent any more books because (s)he already rented the maximum number of books (4).")
                                break
                        except RepositoryException as msg:
                            print(msg)
                        while True:
                            a = input("Rent another book? (Y/N) ").lower().strip()
                            if a == 'y' or a == 'yes':
                                #terminate = False
                                break
                            elif a == 'n' or a == 'no':
                                print("Thank you!")
                                terminate = True
                                executa = False
                                break
                            else:
                                print("Wrong command!")
    
    def _submenu32(self):
        executa = True
        while executa:
            print("Enter the book ID that the client want to return or enter 0 (zero) to cancel")
            book = None
            while book == None:
                ID = Console._readPositiveInteger("Book ID: ")
                if ID != 0:
                    book = self._bookCtrl.getById(ID)
                    if book == None:
                        print("Error! Invalid book ID.")
                    elif not self._rentalCtrl.isBookRented(book):
                        print("The book with the ID " + str(ID) + " was not rented.")
                        book = None
                else:
                    break
            if ID == 0:
                executa = False
            else:
                try:
                    rental = self._rentalCtrl.getRentalByBook(book)
                    rental.setRentalStatus("inactive")
                    self._rentalCtrl.update(rental)
                    print("The book with the ID " + str(ID) + " was succesfully returned.")
                except Exception as msg:
                    print(msg)
                while True:
                    a = input("Return another book? (Y/N) ").lower().strip()
                    if a == 'y' or a == 'yes':
                        #executa = True
                        break
                    elif a == 'n' or a == 'no':
                        executa = False
                        break
                    else:
                        print("Wrong command!")
    
    def _submenu4(self):
        ''' Statistics menu '''
        print("Loading statistics app...")
        close_stat = False
        while not close_stat:
            self._printSubmenu4()
            cmd = input("Enter command:").strip()
            if cmd == '0':
                print("Closing statistics app...")
                close_stat = True
            elif cmd == '1':
                how_many = self._readPositiveInteger("How many? ")
                print("\nMost rented books: \n")
                i = 1
                for entry in self._rentalCtrl.mostRentedBooks(how_many):
                    s = "    " + str(i) + "."
                    s += entry[0].getAuthor() + ", " + entry[0].getTitle()
                    s += " - rented " + str(entry[1]) + " times"
                    print(s)
                    i += 1
            elif cmd == '2':
                how_many = self._readPositiveInteger("How many? ")
                print("\nMost active clients: \n")
                i = 1
                for entry in self._rentalCtrl.mostActiveClients(how_many):
                    s = "    " + str(i) + "."
                    s += entry[0].getName() + " (ID: " + str(entry[0].getId()) + ") "
                    s += "has rented " + str(entry[1]) + " books so far"
                    print(s)
                    i += 1
            else:
                print("Wrong command!")

    def mainMenu(self):
        terminate = False
        while not terminate:
            self._printMenu()
            cmd = input("Enter command:").strip().lower()
            if cmd == '0':
                print("Bye!")
                terminate = True
            elif cmd == "u":
                self._undoCtrl.undo()
                print("Successfully undone.")
            elif cmd == "r":
                self._undoCtrl.redo()
                print("Successfully redone.")
            elif cmd == '1':
                self._submenu1()
            elif cmd == '2':
                self._submenu2()
            elif cmd == '3':
                self._submenu3()
            elif cmd == '4':
                self._submenu4()
            else:
                print("Wrong command!")
        
    def _genRentID(self):
        global rId
        rId += 1
        return rId
            
    @staticmethod
    def _readPositiveInteger(msg):
        '''
        Reads a positive integer
        Input: msg (string) - a message that is printed to the user
        Output: A positive integer
        Raises ValueError in case the integer read is a nonpositive number
        '''
        result = None
        while result == None:
            try:
                result = int(input(msg))
                if result < 0:
                    raise ValueError
            except ValueError:
                print("Please input a positive integer!")
                result = None
        return result
    
    def _readBook(self):
        '''
        Reads a book
        Output: book (Book)
        Raises ValidatorException in case of bad Book-object input
        '''
        #ID = Console._readPositiveInteger("Book ID: ")
        ID = self._bookIDGenerator.getNextID()
        title = None
        while not title:
            title = input("Title: ").strip()
            try:
                bookValidator.validateTitle(title)
            except ValidatorException as msg:
                print(msg)
                title = None
        author = input("Author: ").strip()
        descr = input("Description (leave empty if none): ")
        if len(descr) == 0:
            descr = "N/A"
        book = Book(ID, title, descr, author)
        bookValidator.validate(book)
        return book
    
    def _readClient(self):
        '''
        Reads and validates a client
        Output: client (Client)
        Raises ValidatorException in case of bad Client-object input
        '''
        #ID = Console._readPositiveInteger("Client ID: ")
        ID = self._clientIDGenerator.getNextID()
        name = None
        while not name:
            name = input("Name: ").strip()
            try:
                clientValidator.validateName(name)
            except ValidatorException as msg:
                print(msg)
                name = None
        CNP = None
        while not CNP:
            CNP = str(input("CNP: "))
            try:
                clientValidator.validateCNP(CNP)
            except ValidatorException as msg:
                print(msg)
                CNP = None
        client = Client(ID, name, CNP)
        clientValidator.validate(client)
        return client
