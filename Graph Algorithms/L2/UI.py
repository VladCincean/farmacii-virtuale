class UI:
    def __init__(self, ctrl):
        self.__ctrl = ctrl
        
    def __wait(self):
        print("Press ENTER to continue ...")
        input()
        
    @staticmethod
    def __printMenu():
        s = "\t Available options:\n"
        s += "1 - Find a lowest length path between two vertices (forward BFS)\n"
        s += "0 - EXIT\n"
        print(s)
        
    def __menu1(self):
        s = input("\tstarting vertex: ")
        t = input("\ttarget vertex: ")
        s = int(s); t = int(t)
        try:
            path = self.__ctrl.getPath(s, t)
            
            if path == None:
                print("There is no (lowest length) path from vertex "+str(s)+" to vertex "+str(t)+".\n")
                return
            out = str(s)
            for i in range(1, len(path), 1):
                out += " --> " + str(path[i])
            print("A lowest length path from vertex "+str(s)+" to vertex "+str(t)+" of length "+str(len(path)-1)+" is:\n")
            print(out)
        except KeyError as ke:
            print("KeyError: " + str(ke))
        finally:
            print("")
            self.__wait()
        
    def run(self):
        print("\t\t\tPractical Work no. 2")
        print("\t\t\t---------------------")
        print("\t\t\tStudent: Cincean Vlad")
        print("\t\t\t           Group: 913\n\n")
        
        while True:
            print(self.__ctrl.getGraph())
            print("")
            self.__printMenu()
            cmd = str(input("Enter command: ")).strip()
            if cmd == '0':
                break
            elif cmd == '1':
                self.__menu1()
            else:
                print("\tWrong command!")
        
        print("Thank you!")
    