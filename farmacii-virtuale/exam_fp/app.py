'''
Created on 6 feb. 2016

@author: Vlad
'''
from repository import ProductRepository, ShoppingCart
from domain import ProductValidator
from controller import ProductController
from UI import Console

repo = ProductRepository("products.txt")
cart = ShoppingCart()
val = ProductValidator()
ctrl = ProductController(repo, cart, val)
UI = Console(ctrl)

UI.run()