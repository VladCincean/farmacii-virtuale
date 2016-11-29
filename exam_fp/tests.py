'''
Created on 6 feb. 2016

@author: Vlad
'''
import unittest
from repository import ProductRepository, ShoppingCart
from controller import ProductController
from domain import Product, ProductValidator


class RepositoryTest(unittest.TestCase):


    def setUp(self):
        self.rep = ProductRepository("products.txt")


    def tearDown(self):
        a = "1;red apples;100;10\n2;green apples;80;9\n3;bread 1lb;120;3\n4;bread 2lb;100;5\n5;soap;50;2\n"
        a += "6;milk;30;4\n7;sugar;25;8\n8;coffee 200ml;10;6\n9;cheese 1lb;10;15\n10;salt 1lb;30;4"
        f = open("products.txt", "w")
        f.write(a)
        f.close()

    def testLen(self):
        self.assertTrue(len(self.rep)>0)

    def testAdd(self):
        self.rep.clear()
        self.assertTrue(len(self.rep)==0)
        e = Product(1, "apples", 2, 2)
        self.rep.add(e)
        self.assertTrue(len(self.rep) == 1)
        self.assertRaises(KeyError, self.rep.add, e)
        
    def testUpdate(self):
        self.rep.clear()
        self.assertTrue(len(self.rep)==0)
        e = Product(1, "apples", 2, 2)
        self.rep.add(e)
        self.assertTrue(self.rep.getById(1).getName() == "apples")
        e = Product(1, "oranges", 2, 2)
        self.assertFalse(self.rep.getById(1).getName() == "oranges")
        self.rep.update(e)
        self.assertTrue(self.rep.getById(1).getName() == "oranges")
        
class ControllerTest(unittest.TestCase):
    def setUp(self):
        self.rep = ProductRepository("products.txt")
        self.cart = ShoppingCart()
        self.val = ProductValidator()
        self.ctrl = ProductController(self.rep, self.cart, self.val)

    def tearDown(self):
        a = "1;red apples;100;10\n2;green apples;80;9\n3;bread 1lb;120;3\n4;bread 2lb;100;5\n5;soap;50;2\n"
        a += "6;milk;30;4\n7;sugar;25;8\n8;coffee 200ml;10;6\n9;cheese 1lb;10;15\n10;salt 1lb;30;4"
        f = open("products.txt", "w")
        f.write(a)
        f.close()
        
    def testController(self):
        self.rep.clear()
        self.assertTrue(len(self.rep)==0)
        args = 1, "apples", 2, 2
        e = Product(1, "apples", 2, 2)
        self.assertTrue(self.ctrl.add, args)
        args2 = 1, "apples", 2, 3
        
if __name__ == "__main__":
    unittest.main()
