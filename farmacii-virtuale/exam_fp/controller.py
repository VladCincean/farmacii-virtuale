'''
Created on 6 feb. 2016

@author: Vlad
'''
from domain import Product

class ProductController:
    def __init__(self, inventory, cart, validator):
        '''
        Constructor for ProductController class
        Input: inventory (ProductRepository)
               cart (ShoppingCart)
               validator (ProductValidator)
        '''
        self.__inventory = inventory
        self.__cart = cart
        self.__val = validator
        self.__totalIncome = 0
        
    def add(self, id, name, quantity, price):
        '''
        Adds a product to inventory
        Input: e (Product)
        '''
        e = Product(id, name, quantity, price)
        self.__inventory.add(e)
    
    def update(self, id, name, quantity, price, p = None):
        '''
        Updates a product
        Input: e (Product)
        '''
        if self.__inventory.getById(id) != None:
            if p == None:
                p = self.__inventory.getById(id).getPurchased()
            e = Product(id, name, quantity, price, p)
            self.__inventory.update(e)
        else:
            raise KeyError("Error. Product with the given id NOT found.")
        
    def getById(self, id):
        '''
        Gets the product having the given id
        Input: id (int)
        '''
        return self.__inventory.getById(id)
    
    def getCurrentCart(self):
        ''' returns the shopping cart '''
        return self.__cart.getAll()
    
    def addToCart(self, e):
        '''
        Adds a product to shopping cart
        Input: e (Product)
        '''
        self.__cart.add(e)

    def finalizeSale(self):
        ''' finalizes a sale'''
        for e in self.__cart.getAll():
            self.__totalIncome += e.getPrice()
            e = self.__inventory.getById(e.getId())
            nQ = e.getQuantity() - 1
            self.update(e.getId(), e.getName(), nQ, e.getPrice(), e.getPurchased()+1)
        self.__cart.clear()
        
    def clearCart(self):
        '''clears the shopping cart'''
        self.__cart.clear()
    
    def income(self):
        '''
        Display the total store income
        '''
        return str(self.__totalIncome)
    
    def report(self):
        '''
        Returns a report of purchased products in decreasing order w.r.t. the amount purchased for each
        Output: rep (list)
            e[0] - product id
            e[1] - quantity purchased
        '''
        rep = self.__inventory.getAll()[:]
        rep.sort(reverse = True)
        return rep
    
    
    
