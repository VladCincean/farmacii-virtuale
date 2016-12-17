'''
Created on 3 dec. 2015

@author: Vlad
'''
import unittest
from domain.book import *
from domain.client import *
from domain.ValidatorException import ValidatorException
from repository.repository import *
from repository.RepositoryException import *
from controller.controller import *
from controller.UndoController import UndoController

class ClientValidatorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.val = ClientValidator()
        self.cl = Client(1, "Pop Vasile", "1950621390064")
        
    def tearDown(self):
        pass
   
    def testValidate(self):
        self.assertTrue(self.val.validate, self.cl)
        #invalid/empty name
        self.cl.setName("")
        self.assertRaises(ValidatorException, self.val.validate, self.cl)
        #empty CNP
        self.cl.setCNP("")
        self.assertRaises(ValidatorException, self.val.validate, self.cl)
        #invalid CNP
        self.cl.setCNP("1950621390060")
        self.assertRaises(ValidatorException, self.val.validate, self.cl)
        
class BookValidatorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.val = BookValidator()
        self.book = Book(1, "Alchimistul", "", "Paulo Coelho")
        
    def tearDown(self):
        pass
    
    def testValidate(self):
        self.assertTrue(self.val.validate, self.book)
        #empty/invalid title
        self.book.setTitle("")
        self.assertRaises(ValidatorException, self.val.validate, self.book)
        
class ClientControllerTestCase(unittest.TestCase):
    
    def setUp(self):
        self.val = ClientValidator()
        self.repo = ClientRepository()
        self.ctrl = ClientController(self.repo, UndoController(), self.val)
        self.cl = Client(1, "Pop Vasile", "1950621390064")
        
    def tearDown(self):
        pass
    
    def testCreate(self):
        self.assertTrue(len(self.ctrl.getAll()) == 0)
        #test for invalid client
        self.assertRaises(ValidatorException, self.ctrl.add, Client(1, "", ""))
        #test for duplicated ID
        self.ctrl.add(self.cl)
        self.assertRaises(DuplicatedIDException, self.ctrl.add, Client(1, "Pop Ioana", "2950203450504"))
    
    def testRemove(self):
        #test for invalid ID
        self.ctrl.add(self.cl)
        self.assertEquals(self.ctrl.getById(2), None)
        self.assertTrue(len(self.ctrl.getAll()) == 1)
        self.ctrl.remove(1)
        self.assertTrue(len(self.ctrl.getAll()) == 0)
        
class BookControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.val = BookValidator()
        self.repo = BookRepository()
        self.ctrl = BookController(self.repo, UndoController(), self.val)
        self.book = Book(1, "Alchimistul", "", "Paulo Coelho")
        
    def tearDown(self):
        pass
    
    def testCreate(self):
        self.assertTrue(len(self.ctrl.getAll()) == 0)
        #test for invalid client
        self.assertRaises(ValidatorException, self.ctrl.add, Book(1, "", "", ""))
        #test for duplicated ID
        self.ctrl.add(self.book)
        self.assertRaises(DuplicatedIDException, self.ctrl.add, Book(1, "A", "B", "C"))
        
    def testRemove(self):
        #test for invalid ID
        self.ctrl.add(self.book)
        self.assertEquals(self.ctrl.getById(2), None)
        self.assertTrue(len(self.ctrl.getAll()) == 1)
        self.ctrl.remove(1)
        self.assertTrue(len(self.ctrl.getAll()) == 0)
        
class ClientRepositoryTestCase(unittest.TestCase):
    
    def setUp(self):
        self.repo = ClientRepository()
        
    def tearDown(self):
        pass
    
    def testClientRepo(self):
        #tests for ADD
        self.assertEqual(len(self.repo), 0)
        c = Client(1, "Amalia", "2950203450504")
        self.repo.add(c)
        self.assertEqual(len(self.repo), 1)
        self.assertRaises(RepositoryException , self.repo.add, c)
        c = Client(2, "Ana Maria", "2960223514311")
        self.repo.add(c)
        self.assertEqual(len(self.repo), 2)
        
        #tests for UPDATE
        new = Client(self.repo.getById(1).getId(), "Ioana", self.repo.getById(1).getCNP())
        self.repo.update(new)
        self.assertTrue(self.repo.getById(1).getName() == "Ioana")
        
        #tests for REMOVE
        x = self.repo.remove(2)
        self.assertEquals(len(self.repo), 1)
        self.assertTrue(x.getId(), 2)
        self.assertTrue(x.getName(), "Ana Maria")
        self.repo.removeAll()
        self.assertEquals(len(self.repo), 0)
    
class BookRepositoryTestCase(unittest.TestCase):
    
    def setUp(self):
        self.repo = BookRepository()
        
    def tearDown(self):
        pass
    
    def testBookRepo(self):
        #tests for ADD
        self.assertEqual(len(self.repo), 0)
        b = Book(1, "Alchimistul", "", "Paulo Coelho")
        self.repo.add(b)
        self.assertEqual(len(self.repo), 1)
        self.assertRaises(RepositoryException , self.repo.add, b)
        b = Book(2, "Poemele luminii", "", "Lucian Blaga")
        self.repo.add(b)
        self.assertEqual(len(self.repo), 2)
        
        #tests for UPDATE
        new = Book(self.repo.getById(1).getId(), "New title", self.repo.getById(1).getAuthor(), self.repo.getById(1).getDescription())
        self.repo.update(new)
        self.assertTrue(self.repo.getById(1).getTitle() == "New title")
        
        #tests for REMOVE
        x = self.repo.remove(2)
        self.assertEquals(len(self.repo), 1)
        self.assertTrue(x.getId(), 2)
        self.assertTrue(x.getTitle(), "Poemele luminii")
        self.repo.removeAll()
        self.assertEquals(len(self.repo), 0)
    