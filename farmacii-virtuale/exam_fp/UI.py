'''
Created on 6 feb. 2016

@author: Vlad
'''

class Console:
    def __init__(self, ctrl):
        self.__ctrl = ctrl
        
    @staticmethod
    def printMenu():
        menu = "Please select an option:\n"
        menu += "    1 - ADD a product to inventory\n"
        menu += "    2 - UPDATE a product inventory\n"
        menu += "    3 - ADD a product to the SHOPPING CART\n"
        menu += "    4 - FINALIZE SALE\n"
        menu += "    5 - Show STORE INCOME\n"
        menu += "    6 - REPORT\n"
        menu += "    0 - EXIT application\n"
        print(menu)
        
    def run(self):
        print("Mom & Pop Store\n")
        while True:
            self.printMenu()
            cmd = str(input("Enter command: ")).strip()
            if cmd == '1':
                self.__add()
            elif cmd == '2':
                self.__update()
            elif cmd == '3':
                self.__addToCart()
            elif cmd == '4':
                self.__finalizeSale()
            elif cmd == '5':
                self.__income()
            elif cmd == '6':
                self.__report()
            elif cmd == '0':
                break
            else:
                print("Wrong command!")
        print("Thank you for using our application. Bye!")
        
    def __add(self):
        print("Add a product to inventory:")
        id = self.__readPositiveNumber("    product id: ")
        name = self.__readNonemptyString("    product name: ")
        quantity = self.__readPositiveNumber("    quantity: ")
        price = self.__readPositiveNumber("    price: ")
        try:
            self.__ctrl.add(id, name, quantity, price)
            print("The product was successfully added to product inventory.")
        except KeyError as ke:
            print(str(ke))
        
    
    def __update(self):
        print("Update a product:")
        id = self.__readPositiveNumber("    product id: ")
        e = self.__ctrl.getById(id)
        if e != None:
            name = e.getName()
            print("    "+e.getName())
            print("    the current quantity is " + str(e.getQuantity()))
            quantity = self.__readPositiveNumber("    quantity: ")
            print("    the current price is " + str(e.getPrice()))
            price = self.__readPositiveNumber("    price: ")
            try:
                self.__ctrl.update(id, name, quantity, price)
                print("The product was succesfully updated.")
            except KeyError:
                print("Inexistent id.")
    
    def __addToCart(self):
        print("Add a product to the shopping cart:")
        while True:
            id = self.__readPositiveNumber("    product id: ")
            if self.__ctrl.getById(id) != None:
                break
            else:
                print("Error! Invalid product id.")
        while True:
            e = self.__ctrl.getById(id)
            q = self.__readPositiveNumber("    quantity: ")
            if e.getQuantity() < q:
                print("Error! We do not have sufficent products in stock.")
            else:
                for i in range(q):
                    self.__ctrl.addToCart(e)
                print("Product successfully added to cart.")
                break
#         print("Shopping cart:")
#         if len(self.__ctrl.getCurrentCart()) == 0:
#             print("    -- nothing here")
#         else:
#             t = 0
#             for e in self.__ctrl.getCurrentCart():
#                 print("    "+e.getName())
#                 t += e.getPrice()
#             print("    --- TOTAL: " + str(t) + "RON")
            
    def __finalizeSale(self):
        print("Shopping cart:")
        if len(self.__ctrl.getCurrentCart()) == 0:
            print("    -- nothing here")
        else:
            t = 0
            for e in self.__ctrl.getCurrentCart():
                print("    "+e.getName())
                t += e.getPrice()
            print("    --- TOTAL: " + str(t) + " RON\n")
            while True:
                a = input("Finalize sale (yes or no)?").lower()
                if a == 'y' or a == 'yes' or a == 'da':
                    self.__ctrl.finalizeSale()
                    print("Thank you for buying from us.")
                    break
                if a == 'n' or a == 'no' or a == 'nu':
                    self.__ctrl.clearCart()
                    print("Thank you!")
                    break
            
    
    def __income(self):
        print("Total income:" + self.__ctrl.income())
    
    def __report(self):
        print("Report:")
        rep = self.__ctrl.report()
        if len(rep) == 0:
            print("    --nothing here")
        else:
            for e in rep:
                print("    "+str(e.getId())+" "+e.getName()+" - purchased "+str(e.getPurchased())+" times")
    
    @staticmethod
    def __readPositiveNumber(msg):
        while True:
            try:
                n = int(input(msg))
                if n > 0:
                    break
                else:
                    print("Error! A positive natural number must be provided.")
            except Exception:
                print("A positive natural number must be provided.")
        return n
    
    @staticmethod
    def __readNonemptyString(msg):
        s = ''
        while s == '':
            s = str(input(msg)).strip()
        return s
    