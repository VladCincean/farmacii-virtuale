'''
Created on 2 nov. 2015

@author: Vlad
'''
from repository.repository import *
from repository.FileRepository import *
from controller.controller import *
from controller.UndoController import *
from UI.console import *
from IDGenerator import IDGenerator

aBookValidator = BookValidator()
aClientValidator = ClientValidator()
aRentalValidator = RentalValidator()

prompt = "Do you want to use in-memory-repository or in-file-repository? \n"
prompt += "1 - in-MEMORY-repository \n"
prompt += "2 - in-FILE-repository \n"
print(prompt)
opt = None
while opt != '1' and opt != '2':
    opt = input("Your option: ").strip()
    if opt != '1' and opt != '2': 
        print("Wrong command! Please select 1 or 2!")

if opt == '1':
    aBookRepo = BookRepository()
    aClientRepo = ClientRepository()
    aRentalRepo = RentalRepository(aClientRepo, aBookRepo)
    bID = 1
    cID = 1
    rID = 1
elif opt == '2':
    aBookRepo = FileBookRepository("books.txt")
    aClientRepo = FileClientRepository("clients.txt")
    aRentalRepo = FileRentalRepository(aBookRepo, aClientRepo, "rentals.txt")
    bID = aBookRepo.getNextID()
    cID = aClientRepo.getNextID()
    rID = aRentalRepo.getNextID()

aUndoCtrl = UndoController()
aBookCtrl = BookController(aBookRepo, aUndoCtrl, aBookValidator)
aClientCtrl = ClientController(aClientRepo, aUndoCtrl, aClientValidator)
aRentalCtrl = RentalController(aRentalRepo, aClientRepo, aBookRepo, aUndoCtrl, aRentalValidator)

aUI = Console(aBookCtrl, aClientCtrl, aRentalCtrl, aUndoCtrl, bID, cID, rID)

aUI.mainMenu()
