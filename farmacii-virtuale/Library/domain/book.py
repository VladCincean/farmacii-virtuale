'''
Created on 2 nov. 2015

@author: Vlad
'''
from domain.IDObject import IDObject
from domain.ValidatorException import ValidatorException

class Book(IDObject):
    '''
    classdocs
    '''

    def __init__(self, ID, title, descr, author):
        '''
        Constructor for Book class
        Input: ID (integer)
               title (string)
               descr (string) - description
               author (string)
        '''
        IDObject.__init__(self, ID)
        self._id = ID
        self._title = title
        self._descr = descr
        self._author = author
        
    '''
    Getting attribute methods
    '''
    def getTitle(self):
        return self._title
    def getDescription(self):
        return self._descr
    def getAuthor(self):
        return self._author
    '''
    Setting attribute methods
    '''
    def setTitle(self, title):
        self._title = title
    def setDescription(self, descr):
        self._descr = descr
    def setAuthor(self, author):
        self._author = author
    
    def __str__(self):
        '''
        Overrides the str() built-in function
        '''
        s = ""
        s += "    ID: " + str(self._id) + "\n"
        s += "    Title: " + self._title + "\n"
        s += "    Author: "
        if self._author == "":
            s += "(unknown)\n"
        else:
            s += self._author + "\n"
        s += "    Description: "
        if self._descr == "":
            s += "N/A"
        else:
            s += self._descr
        return s
    
    def __eq__(self, book):
        if isinstance(book, Book) == False:
            return False
        return self.getId() == book.getId()
    
class BookValidator(object):
    
    def __init__(self):
        self._errors = ""
    
    def validate(self, book):
        '''
        Validates the provided Book instance
        Output: - a list of validation errors
                None, if book is a valid Book
        '''
        if isinstance(book, Book) == False:
            raise TypeError("Error! The validator can validate only Book objects.")
        self._errors = []
        self.validateTitle(book.getTitle())
        if len(self._errors) != 0:
            raise ValidatorException(self._errors)
        return True
    
    def validateTitle(self, title):
        self._errors = []
        if len(title) == 0:
            self._errors.append("Error! The book must have a title.")
        if len(self._errors) != 0:
            raise ValidatorException(self._errors)
        return True
        
    