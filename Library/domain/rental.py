'''
Created on 16 nov. 2015

@author: Vlad
'''
from domain.IDObject import IDObject
from domain.book import *
from domain.client import *
from datetime import date, datetime, timedelta

start = date.today()
end = date.today() + timedelta(days = 14)

class Rental(object):
    '''
    classdocs
    '''

    def __init__(self, rentalId, clientId, bookId, start = start, end = end, active = 'active'):
        '''
        Constructor for Rental Class
        Input: rentalId (integer) - unique
               clientId (integer)
               bookId (integer)
               start (date) - today, by default
               end (date) - the deadline, 2 weeks from today, by default
        '''
        self._rentalId = rentalId
        self._clientId = clientId
        self._bookId = bookId
        self._startDate = start
        self._endDate = end
        if active == 'active':
            self._active = True #by default
        elif active == 'inactive':
            self._active = False
        
    '''
    Getting methods
    '''
    def getId(self):
        return self._rentalId
    def getClientId(self):
        return self._clientId
    def getBookId(self):
        return self._bookId
    def getStartDate(self):
        return self._startDate
    def getEndDate(self):
        return self._endDate
    def getRentalStatus(self):
        if self._active == True:
            return "active"
        else:
            return "inactive"
    
    '''
    Setting methods
    '''
    def setId(self, rentalId):
        self._rentalId = rentalId
    def setClientId(self, clientId):
        self._clientId = clientId
    def setBookId(self, bookId):
        self._bookId = bookId
    def setStartDate(self, start):
        self._startDate = start
    def setEndDate(self, end):
        self._endDate = end
    def setRentalStatus(self, st):
        if st == "active":
            self._active = True
        elif st == "inactive":
            self._active = False
        
    """
    def __str__(self):
        '''
        Overrieds the str() built-in function
        '''
        s = "Rental #" + str(self._rentalId) + ":\n"
        s += "    Client: " + self._clientId.getName() + " (ID " + str(self._clientId.getId()) + ")\n"
        s += "    Book: " + self._bookId.getTitle() + ", " + self._bookId.getAuthor() + " (ID " + str(self._bookId.getId()) + ")\n"
        #s += str(type(self._startDate))
        s += "    Start date: " + self._startDate.strftime("%A %d, %B %Y") + "\n"
        s += "    Deadline: " + self._endDate.strftime("%A %d, %B %Y") + "\n"
        return s
    """
    
class RentalValidator(object):
    
    def __init__(self):
        self._errors = []
        
    def validate(self, rental):
        if isinstance(rental, Rental) == False:
            raise TypeError("Error! The validator can validate only Rental objects.")
        self._errors = []
        #now = date.today()
        #if rental.getStartDate() < now:
        #    self._errors.append("Rental starts in the past.")
        if len(self._errors) != 0:
            raise ValidatorException(self._errors)
        return True
        