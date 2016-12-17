'''
Created on 2 nov. 2015

@author: Vlad
'''
from domain.book import *
from domain.client import *
from domain.rental import *
from domain.ValidatorException import ValidatorException
from repository.repository import *
from repository.RepositoryException import *
from UI.console import Console

def testAll():
    def test_IDObject():
        obj = IDObject(133)
        assert obj.getId() == 133
    test_IDObject()
    
    def test_Book():
        b = Book(1, "Poemele luminii", "", "Lucian Blaga")
        assert b.getId() == 1
        b.setId(2)
        assert b.getId() == 2
        assert b.getTitle() == "Poemele luminii"
        b.setTitle("Basme")
        assert b.getTitle() == "Basme"
        assert b.getDescription() == ""
        b.setDescription("No description")
        assert b.getDescription() == "No description"
        assert b.getAuthor() == "Lucian Blaga"
        b.setAuthor("Ion Creanga")
        assert b.getAuthor() == "Ion Creanga"
    test_Book()
    
    def test_BookValidator():
        ''' etc. '''
        pass
    test_BookValidator()
    
    def test_Client():
        client = Client(1, "Pop Vasile", "1950621390064")
        assert client.getId() == 1
        client.setId(2)
        assert client.getId() == 2
        assert client.getName() == "Pop Vasile"
        client.setName("Ion Popescu")
        assert client.getName() == "Ion Popescu"
        assert client.getCNP() == "1950621390064"
        client.setCNP("1941102036072")
        assert client.getCNP() == "1941102036072"
    test_Client()
    
    def test_ClientValidator():
        cv = ClientValidator()
        assert cv._validateCNP('25') == False
        assert cv._validateCNP('-1') == False
        assert cv._validateCNP("1920506226507") == True
        assert cv._validateCNP("1920506226503") == False
        c = Client(1, "Pop Vasile", "1950621390064")
        assert cv.validate(c) == True
        c = Client(1, "Pop Vasile", "-2") #invalid cnp
        try:
            cv.validate(c)
            assert False
        except ValidatorException:
            assert True
        c = Client(1, "Pop Vasile", "1950621390065") #invalid cnp
        try:
            cv.validate(c)
            assert False
        except ValidatorException:
            assert True
        c = Client(1, "", "1950621390064") #invalid name
        try:
            cv.validate(c)
            assert False
        except ValidatorException:
            assert True
    test_ClientValidator()
    
    def test_BookRepository():
        repo = BookRepository()
        
        b1 = Book(1, "Poemele luminii", "first book description", "Lucian Blaga")
        b2 = Book(1, "Basme", "second book description", "Ion Creanga")
        
        assert len(repo) == 0
        
        ###--- adding tests
        repo.add(b1)
        assert len(repo) == 1
        assert repo.getById(1) == b1
        try:
            repo.add(b1)
            assert False
        except DuplicatedIDException:
            assert True
        try:
            repo.add(b2)
            assert False
        except DuplicatedIDException:
            assert True
            
        b2 = Book(2, "Basme", "second book description", "Ion Creanga")
        repo.add(b2)
        
        ###--- getting tests
        assert len(repo) == 2
        assert repo.getById(1) == b1
        assert repo.getById(2) == b2
        assert repo.getByTitle("Basme") == [b2]
        assert repo.getByAuthor("Lucian Blaga") == [b1]
        assert repo.getAll() == [b1, b2]
   
        ###--- removing tests
        assert len(repo) == 2
        repo.remove(1)
        assert len(repo) == 1
        assert repo.getById(1) == None
        assert repo.getById(2) == b2
        try:
            repo.remove(1)
            assert False
        except InexistentIDException:
            assert True
        assert repo.remove(2) == b2
        assert len(repo) == 0
    test_BookRepository()
    
    def test_ClientRepository():
        repo = ClientRepository()
        
        c1 = Client(1, "Pop Vasile", "1950621390064")
        c2 = Client(1, "Ion Popescu", "1950621390065")
        
        assert len(repo) == 0
        
        ###--- adding tests
        repo.add(c1)
        assert len(repo) == 1
        assert repo.getById(1) == c1
        try:
            repo.add(c1)
            assert False
        except DuplicatedIDException:
            assert True
        try:
            repo.add(c2)
            assert False
        except DuplicatedIDException:
            assert True
            
        c2 = Client(2, "Ion Popescu", "1950621390065")
        repo.add(c2)
        
        ###--- getting tests
        assert len(repo) == 2
        assert repo.getById(1) == c1
        assert repo.getById(2) == c2
        assert repo.getByName("ioN PoPEScu") == [c2]
        assert repo.getByCNP("1950621390064") == [c1]
        assert repo.getByCNP("1950621390065") == [c2]
        assert repo.getAll() == [c1, c2]
        
        ###--- removing tests
        assert len(repo) == 2
        repo.remove(1)
        assert len(repo) == 1
        assert repo.getById(1) == None
        assert repo.getById(2) == c2
        try:
            repo.remove(1)
            assert False
        except InexistentIDException:
            assert True
        assert repo.remove(2) == c2
        assert len(repo) == 0
    test_ClientRepository()
    
    def test_RentalRepository():
        clRepo = ClientRepository()
        bkRepo = BookRepository()
        rentRepo = RentalRepository(clRepo, bkRepo)
        c1 = Client(1, "Pop Vasile", "1950621390064")
        c2 = Client(2, "Ion Popescu", '1890320183795')
        b1 = Book(1, "Poemele luminii", "", "Lucian Blaga")
        b2 = Book(2, "Basme", "", "Ion Creanga")
        b3 = Book(3, "Alchimistul", "", "Paulo Coelho")
        clRepo.add(c1)
        bkRepo.add(b1)
        bkRepo.add(b2)
        bkRepo.add(b3)
        assert len(rentRepo) == 0
        r1 = Rental(1, c1, b1)
        r2 = Rental(2, c1, b2)
        r3 = Rental(3, c2, b3)
        
        ###--- adding tests
        rentRepo.add(r1)
        assert len(rentRepo) == 1
        assert rentRepo.getById(1) == r1
        try:
            rentRepo.add(r1)
            assert False
        except DuplicatedIDException:
            assert True
        rentRepo.add(r2)
        rentRepo.add(r3)
        assert len(rentRepo) == 3
        
        ###--- removing tests
        rentRepo.remove(r1.getId())
        assert len(rentRepo) == 2
        try:
            rentRepo.remove(r1.getId())
            assert False
        except InexistentIDException:
            assert True
        rentRepo.removeAll()
        assert len(rentRepo) == 0
    test_RentalRepository()
        
    
    def test_Validator():
        pass
    test_Validator()
    
testAll()
print("All tests succeded")