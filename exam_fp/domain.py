'''
Created on 6 feb. 2016

@author: Vlad
'''

class Product:
    def __init__(self, id, name, quantity, price, purchased = 0):
        '''
        Constructor for Product class
        Input: id (int) - positive
               name (string) - nonempty
               quantity (int) - positive
               price (int) - positive
        '''
        self.__id = id
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__purchased = purchased
        
    '''getting methods '''
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getQuantity(self):
        return self.__quantity
    def getPrice(self):
        return self.__price
    def getPurchased(self):
        return self.__purchased
    
    '''setting methods '''
    def setId(self, id):
        self.__id = id
    def setName(self, name):
        self.__name = name
    def setQuantity(self, quantity):
        self.__quantity = quantity
    def setPrice(self, price):
        self.__price = price
    def setPurchased(self, n):
        self.__purchased = n
    def incrementPurchased(self):
        self.__purchased += 1
        
    def buy(self):
        self.__quantity -= 1
        self.__purchased += 1
        
    def __eq__(self, o):
        return type(self) == type(o) and self.__id == o.getId()
    
    def __lt__(self, o):
        if self.__purchased < o.getPurchased():
            return True
        return False
    
    def __str__(self):
        s = "Product id " + str(self.__id) + "\n"
        s +="    name: " + str(self.__name) + "\n"
        s +="    quantity: " + str(self.__quantity) + "\n"
        s +="    price: " + str(self.__price) + "\n"
        return s
    
    def __repr__(self):
        return str(self)
    
class ProductValidator:
    def __init__(self):
        self.__errors = []
    
    def validate(self, e):
        '''
        Validates a product
        Input: e (Product)
        '''
        self.__errors = []
        if e.getName() == '':
            self.__errors.append("Product must have a name.")
        if e.getQuantity() < 0:
            self.__errors.append("Negative quantity.")
        if e.getPrice() < 0:
            self.__errors.append("Negative price.")
        if len(self.__errors) > 0:
            raise ValueError(self.__errors)
        return True
    
    
