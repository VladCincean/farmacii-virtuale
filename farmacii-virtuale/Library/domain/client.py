'''
Created on 2 nov. 2015

@author: Vlad
'''
from domain.IDObject import IDObject
from domain.ValidatorException import ValidatorException

class Client(IDObject):
    '''
    classdocs
    '''

    def __init__(self, ID, name, CNP):
        '''
        Constructor for Client class
        Input: ID (integer)
               name (string)
               CNP (string)
        '''
        IDObject.__init__(self, ID)
        self._id = ID
        self._name = name
        self._CNP = CNP
        
    '''
    Getting attribute methods
    '''
    def getName(self):
        return self._name
    def getCNP(self):
        return self._CNP
    def getRentalList(self):
        return self._rentalList
    
    '''
    Setting attribute methods
    '''
    def setName(self, name):
        self._name = name
    def setCNP(self, CNP):
        self._CNP = CNP
        
    def __str__(self):
        '''
        Overrides the str() built-in function
        '''
        s = ""
        s += "ID: " + str(self._id) + "\n"
        s += "Name: " + self._name + "\n"
        s += "CNP: " + self._CNP + "\n"
        return s
    
    def __eq__(self, client):
        if isinstance(client, Client) == False:
            return False
        return self.getId() == client.getId()
    
class ClientValidator(object):
    
    def __init__(self):
        self._errors = ""
        
    def _validateCNP(self, CNP):
        '''
        Validates a CNP
        Input: CNP (string)
        Output: True, if CNP is valid
                False, otherwise
        '''
        if len(CNP) != 13:
            return False
        s = int(CNP[0])
        aa = 10*int(CNP[1]) + int(CNP[2])
        ll = 10*int(CNP[3]) + int(CNP[4])
        zz = 10*int(CNP[5]) + int(CNP[6])
        jj = 10*int(CNP[7]) + int(CNP[8])
        nnn = 100*int(CNP[9]) + 10*int(CNP[10]) + int(CNP[11])
        c = int(CNP[12])
        if s == 0:
            return False
        
        keys=[2,7,9,1,4,6,3,5,8,2,7,9]
        check_key = 0
        for i in range(len(keys)):
            check_key += int(CNP[i])*keys[i]
        check_key = check_key % 11
        
        if (check_key == 10 and c != 1) or check_key != c:
            return False
        if ll >= 13 or ll == 0 or zz == 0:
            return False
        if (ll == 1 or ll == 3 or ll == 5 or ll == 7 or ll == 8 or ll == 10 or ll == 12) and zz > 31:
            return False
        if (ll == 2 and aa % 4 == 0 and zz > 29) or (ll == 2 and aa % 4 != 0 and zz > 28):
            return False
        if jj == 0 or jj > 48 or nnn == 0:
            return False
        return True
        
    def validate(self, client):
        '''
        Validates the provided Client instance
        Output: - a list of validation errors
                None, if client is a valid Client
        '''
        if isinstance(client, Client) == False:
            raise TypeError("Error! The validator can validate only Client objects.")
        self._errors = []
        self.validateName(client.getName())
        self.validateCNP(client.getCNP())
        if len(self._errors) != 0:
            raise ValidatorException(self._errors)
        return True
    
    def validateName(self, name):
        self._errors = []
        if len(name) == 0:
            self._errors.append("The client must have a name.")
        if len(self._errors) != 0:
            raise ValidatorException(self._errors)
        return True
    
    def validateCNP(self, CNP):
        self._errors = []
        if self._validateCNP(CNP) == False:
            self._errors.append("Invalid CNP!")
        if len(self._errors) != 0:
            raise ValidatorException(self._errors)
        return True
    