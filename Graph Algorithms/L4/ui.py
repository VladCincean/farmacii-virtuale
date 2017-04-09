'''
Created on 7 mai 2016

@author: Vlad
'''
class UI:
    def __init__(self, ctrl):
        self.__ctrl = ctrl
        
    @staticmethod
    def __wait():
        print("Press ENTER to continue ...")
        input()
        
    @staticmethod
    def __printMenu():
        s = "1 - Read the list of activities from keyboard\n"
        s += "2 - Load the list of activities from file\n"
        s += "3 - Verify if the corresponding graph is a DAG +- perform a topological sort\n"
        s += "4 - Print the earliest and the latest starting time for each activity and the total time of the project\n"
        s += "5 - Print the critical activities\n"
        s += "0 - EXIT\n"
        print(s)
        
    def run(self):
        print("\t\t\tPractical Work no. 4")
        print("\t\t\t---------------------")
        
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
            else:
                print("\tWrong command!")
        print("Thank you!")
        
    def __menu1(self):
        print("Warning! This operation will clear the all the previous activities.")
        a = input("Do you want to continue? (y/n): ").lower()
        if a != "y" and a != "yes" and a != "da":
            return
        
        n = int(input("How many activities?: "))
        if n == 0:
            print("Error! The number of activities cannot be zero.")
            return
            
        self.__ctrl.clear()
        self.__ctrl.addActivity("start", 0)
        self.__ctrl.addActivity("end", 0)
        print("Please enter the duration of each activity...")
        for i in range(1, n + 1, 1):
            d = int(input("Duration of activity #" + str(i) + ": "))
            self.__ctrl.addActivity(i, d)
        print("Now, enter the prerequisites of each activity separated be spaces..")
        for i in range(1, n + 1, 1):
            print("What are the prerequisites of activity #" + str(i) + " ?")
            P = input().split()
            P = [int(x) for x in P]
            self.__ctrl.setPrerequisites(i, P)
        P = [x for x in range(1, n + 1, 1)]
        self.__ctrl.setPrerequisites("end", P)
        print("Done!")
        self.__wait()
        
    def __menu2(self):
        file = input("Filename: ").strip()
        try:
            self.__ctrl.initFromFile(file)
            print("File successfully loaded.")
        except IOError as io:
            print("IOError! " + str(io))
        finally:
            self.__wait()
        
    def __menu3(self):
        TS = self.__ctrl.toposort()
        if TS == None:
            print("The corresponding activities graph is NOT a DAG.")
            print("There is NO topological sorting of the activities.")
            self.__wait()
            return
        
        print("The corresponding activities graph is a DAG.")
        print("The topological sorting of the activities:")
        s = str(TS[0])
        for i in range(1, len(TS), 1):
            s += " - " + str(TS[i])
        print(s)
        self.__wait()
    
    def __menu4(self):
        try:
            self.__ctrl.computeTiming()
            TS = self.__ctrl.toposort()
#             print(TS)
            for i in range(1, len(TS) - 1, 1):
                s = "Activity " + str(TS[i]) + ":\n"
                s += "\tearliest starting time: " + str(self.__ctrl.getES(TS[i])) + "\n"
                s += "\tlatest starting time: " + str(self.__ctrl.getLS(TS[i])) + "\n"
                print(s)
            print("----------------------------")
            print("\nTotal project time: " + str(self.__ctrl.getProjectTime()))
        except Exception:
            print("Error! The corresponding activities graph is NOT a DAG.")
        finally:
            self.__wait()
    
    def __menu5(self):
        try:
            self.__ctrl.computeTiming()
            CA = self.__ctrl.getCriticalActivities()
            if CA == None:
                print("There are NO critical activities.")
            else:
                s = "The critical activities are: "
                s += str(CA[0])
                for i in range(1, len(CA), 1):
                    s += ", " + str(CA[i])
                print(s)
        except Exception:
            print("Error! The corresponding activities graph is NOT a DAG.")
        finally:
            self.__wait()
