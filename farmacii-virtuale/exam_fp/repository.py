'''
Created on 6 feb. 2016

@author: Vlad
'''
from domain import Product

class ProductRepository:
    def __init__(self, filename = 'products.txt'):
        '''
        Constructor for ProductRepository class
        Input: filename (string)
        '''
        self.__fName = filename
        self.__data = []
        self.__loadFromFile()
        
    def __len__(self):
        return len(self.__data)
        
    def find(self, id):
        '''
        Returns the index of the product having the given id
        Input: id (int)
        Output: index (int), if element found
                None, otherwise
        '''
        for e in self.__data:
            if e.getId() == id:
                return self.__data.index(e)
        return None
    
    def getById(self, id):
        '''
        Returns the product from repository having the given id.
        Input: id (int)
        Output: e (Product)
                None, if not found
        '''
        for e in self.__data:
            if e.getId() == id:
                return e
        return None
    
    def add(self, e):
        '''
        Adds a product to repository
        Input: e (Product)
        Raises KeyError in case of duplicated id
        '''
        if self.find(e.getId()) != None:
            raise KeyError("Error! Duplicated id. The product was NOT added.")
        self.__data.append(e)
        self.__storeToFile()
        
    def update(self, e):
        '''
        Updates a product
        Input: e (Product)
        Raises KeyError in case the product is not in repository
        '''
        idx = self.find(e.getId())
        if idx == None:
            raise KeyError("Can not update. Product not found in repository.")
        self.__data.pop(self.find(e.getId()))
        self.__data.insert(idx, e)
        self.__storeToFile()
        
    def getAll(self):
        ''' returns the repository data '''
        return self.__data
    
    def clear(self):
        ''' clears the repository '''
        self.__data.clear()
    
    def __len__(self):
        '''returns the size of repository'''
        return len(self.__data)
    
    def __storeToFile(self):
        ''' saves repository to file '''
        f = open(self.__fName, "w")
        for e in self.__data:
            s = str(e.getId())+";"+str(e.getName())+";"+str(e.getQuantity())+";"+str(e.getPrice())+"\n"
            f.write(s)
        f.close()
            
    def __loadFromFile(self):
        ''' loads data from file in repository'''
        f = open(self.__fName, "r")
        for line in f:
            args = line.split(";")
            if len(args) == 4:
                id, name, quantity, price = args
                self.add(Product(int(id), name.strip(), int(quantity), int(price)))
        f.close()

class ShoppingCart:
    def __init__(self):
        '''
        Constructor for ShoppingCart class
        '''
        self.__cart = []
        self.__totalIncome = 0
        
    def add(self, e):
        '''
        Adds a product to shopping cart
        Input: e 
        '''
        self.__cart.append(e)
        
    def getAll(self):
        ''' returns the shopping cart'''
        return self.__cart
        
    def clear(self):
        ''' empty the shopping cart '''
        self.__cart.clear()
        
        
        
