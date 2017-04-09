'''
Created on 19 mar. 2016

@author: Vlad
'''
import os
from _ast import Str

class UI:
    def __init__(self, ctrl):
        self.__ctrl = ctrl
        
    def __wait(self):
        print("Press ENTER to continue ...")
        input()
    
    @staticmethod
    def __printMenu():
        s = "\t Available options:\n"
        s += "1 - Get n and m (the number of vertices and of edges, respectively)\n"
        s += "2 - Check is there is an edge between 2 vertices\n"
        s += "3 - Get in-degree and out-degree of a vertex\n"
        s += "4 - Out-bound edges of a given vertex\n"
        s += "5 - In-bound edges of a given vertex\n"
        s += "6 - Retrieve or modify the information attached to a specific edge\n"
        s += "7 - BONUS: add/remove edge\n"
        s += "8 - BONUS: add/remove vertex\n"
        #s += "9 - BONUS 3\n"
        s += "0 - EXIT\n"
        print(s)
        
    def __menu1(self):
        n = self.__ctrl.graph().getV()
        m = self.__ctrl.graph().getE()
        if n == 1:
            print("\tn = 1 vertex")
        else:
            print("\tn = " + str(n) + " vertices")
        if m == 1:
            print("\tm = 1 edge\n")
        else:
            print("\tm = " + str(m) + " edges\n")
        self.__wait()
    
    def __menu2(self):
        try:
            x = int(input("\tsource vertex: ").strip())
            y = int(input("\ttarget vertex: ").strip())
            if self.__ctrl.graph().isEdge(x, y):
                print("\tYes. There is an edge " + str(x) + "->" + str(y))
            else:
                print("\tNo. There is NO edge " + str(x) + "->" + str(y))
        except KeyError:
            print("\tKeyError! Invalid vertex (vertices).")
        except ValueError:
            print("\tValueError! Invalid vertex (vertices).")
        finally:
            self.__wait()
    
    def __menu3(self):
        try:
            x = int(input("\tvertex: ").strip())
            print("\tindeg(" + str(x) + ") = " + str(self.__ctrl.graph().inDegree(x)))
            print("\toutdeg(" + str(x) + ") = " + str(self.__ctrl.graph().outDegree(x)))
        except KeyError:
            print("\tKeyError! Invalid vertex.")
        except ValueError:
            print("\tValueError! Invalid vertex.")
        finally:
            self.__wait()
    
    def __menu4(self):
        try:
            x = int(input("\tvertex: ").strip())
            print("\tOutbound edges: ")
            for v in self.__ctrl.graph().iterateOut(x):
                print("\t\t" + str(x) + "->" + str(v) + ", cost " + str(self.__ctrl.graph().getCost(x, v)))
        except KeyError:
            print("\tKeyError! Invalid vertex.")
        except ValueError:
            print("\tValueError! Invalid vertex.")
        finally:
            self.__wait()
            
    def __menu5(self):
        try:
            x = int(input("\tvertex: ").strip())
            print("\tInbound edges: ")
            for v in self.__ctrl.graph().iterateIn(x):
                print("\t\t" + str(v) + "->" + str(x) + ", cost " + str(self.__ctrl.graph().getCost(v, x)))
        except KeyError:
            print("\tKeyError! Invalid vertex.")
        except ValueError:
            print("\tValueError! Invalid vertex.")
        finally:
            self.__wait()
    
    def __menu6(self):
        try:
            x = int(input("\tsource vertex: ").strip())
            y = int(input("\ttarget vertex: ").strip())
            if self.__ctrl.graph().isEdge(x, y):
                print("\tThe cost of the edge " + str(x) + "->" + str(y) + " is " + str(self.__ctrl.graph().getCost(x, y)))
                cmd = input("\tDo you want to modify it? (y/n): ").strip().lower()
                if cmd == "y" or cmd == "yes":
                    nc = input("\tnew cost: ")
                    try:
                        nc = int(nc)
                    finally:
                        self.__ctrl.graph().setCost(x, y, nc)
                        print("\tCost " + str(nc) + " successfully updated.")
                elif cmd == "n" or cmd == "no":
                    pass
                else:
                    print("\tThe cost was NOT changed.")
            else:
                print("\tThere is NO edge " + str(x) + "->" + str(y))
        except KeyError:
            print("\tKeyError! Invalid vertex (vertices).")
        except ValueError:
            print("\tValueError! Invalid vertex (vertices).")
        finally:
            self.__wait()
    
    def __menu7(self):
        s = "\tBONUS: add/remove edges\n"
        s += "1 - ADD an edge\n"
        s += "2 - REMOVE an edge\n"
        s += "0 - BACK to main menu\n"
        while True:
            print(s)
            cmd = str(input("Enter command: ")).strip()
            if cmd == '0':
                break
            elif cmd == '1':
                self.__menu71()
            elif cmd == '2':
                self.__menu72()
    
    def __menu71(self):
        try:
            x = int(input("\tsource vertex: ").strip())
            y = int(input("\ttarget vertex: ").strip())
            self.__ctrl.graph().addEdge(x, y)
            print("\tThe edge (" + str(x) + ", " + str(y) + ") was successfully added.")
            print("\tThe cost was set to 'None', by default.")
            yn = input("\tDo you want to change it? (y/n): ").strip().lower()
            if yn == 'y' or yn == 'yes':
                c = input("\tCost: ").strip()
                self.__ctrl.graph().setCost(x, y, int(c))
                print("\tcost(%d, %d) = %d", x, y, c)
            else:
                print("\tThe cost of the edge is still 'None'")
        except KeyError as ke:
            print("\tKeyError! " + str(ke))
        except ValueError as ve:
            print("\tValueError! " + str(ve))
        finally:
            self.__wait()
    
    def __menu72(self):
        try:
            x = int(input("\tsource vertex: ").strip())
            y = int(input("\ttarget vertex: ").strip())
            if self.__ctrl.graph().isEdge(x, y):
                print("You are going to remove the edge (" + str(x) + ", " + str(y) + ") This cannot be undone.")
                yn = input("Do you want to continue the operation? (y/n): ").strip().lower()
                if yn == 'y' or yn == 'yes':
                    self.__ctrl.graph().removeEdge(x, y)
                    print("\tEdge successfully removed.")
                else:
                    print("\tEdge removal canceled.")
            else:
                print("There is no edge (" + str(x) + ", " + str(y) + ").")
        except KeyError as ke:
            print("\tKeyError! " + str(ke))
        except ValueError as ve:
            print("\tValueError! " + str(ve))
        finally:
            self.__wait()
    
    def __menu8(self):
        s = "\tBONUS: add/remove vertices\n"
        s += "1 - ADD a vertex\n"
        s += "2 - REMOVE a vertex\n"
        s += "0 - BACK to main menu\n"
        while True:
            print(s)
            cmd = str(input("Enter command: ")).strip()
            if cmd == '0':
                break
            elif cmd == '1':
                self.__menu81()
            elif cmd == '2':
                self.__menu82()
    
    def __menu81(self):
        try:
            x = int(input("\tvertex: ").strip())
            self.__ctrl.graph().addVertex(x)
            print("\tThe vertex " + str(x) + " was successfully added.")
        except KeyError as ke:
            print("\tKeyError! " + str(ke))
        except ValueError as ve:
            print("\tValueError! " + str(ve))
        finally:
            self.__wait()
    
    def __menu82(self):
        try:
            x = int(input("\tvertex: ").strip())
            print("You are going to remove the vertex " + str(x) + " together with its incident edges. This cannot be undone.")
            yn = input("Do you want to continue the operation? (y/n): ").strip().lower()
            if yn == 'y' or yn == 'yes':
                self.__ctrl.graph().removeVertex(x)
                print("\tVertex successfully removed.")
            else:
                print("\tVertex removal canceled.")
        except KeyError as ke:
            print("\tKeyError! " + str(ke))
        except ValueError as ve:
            print("\tValueError! " + str(ve))
        finally:
            self.__wait()
    
    def __menu9(self):
        pass
    
    def run(self):
        print("\t\t\tPractical Work no. 1")
        print("\t\t\t---------------------")
        print("\t\t\tStudent: Cincean Vlad")
        print("\t\t\t           Group: 913\n\n")
        
        while True:
            self.__printMenu()
            cmd = str(input("Enter command: ")).strip()
            if cmd == '0':
                break
            elif cmd == '1':
                self.__menu1()
            elif cmd == '2':
                self.__menu2()
            elif cmd == '3':
                self.__menu3()
            elif cmd == '4':
                self.__menu4()
            elif cmd == '5':
                self.__menu5()
            elif cmd == '6':
                self.__menu6()
            elif cmd == '7':
                self.__menu7()
            elif cmd == '8':
                self.__menu8()
#             elif cmd == '9':
#                 self.__menu9()
            else:
                print("\tWrong command!")
        
        print("Thank you!")
        
        