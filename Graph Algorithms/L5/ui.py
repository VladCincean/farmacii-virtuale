class UI:
    def __init__(self, ctrl):
        self.__ctrl = ctrl
        
    @staticmethod
    def __wait():
        print("Press ENTER to continue ...")
        input()
        
    @staticmethod
    def __printMenu():
        s = "1 - Read graph from keyboard\n"
        s += "2 - Load graph from file\n\n"
        s += "3 - Approximation algorithm\n"
        s += "4 - Clever Greedy algorithm\n"
        s += "5 - Alom's algorithm\n"
        s += "6 - Alom's extended algorithm\n"
        s += "7 - Generate and text\n"
        s += "8 - All algorithms\n"
        s += "0 - EXIT"
        print(s)
        
        
    def run(self):
        print("\t\t\tPractical Work no. 5")
        print("\t\t\t---------------------")
        
        while True:
            print(str(self.__ctrl.getGraph()))
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
            else:
                print("\tWrong command!")
        print("Thank you!")
        
    def __menu1(self):
        n = int(input("How many vertices?: "))
        if n < 1:
            print("Error! The number of vertices should be positive.")
            return
        V = [i for i in range(1, n + 1, 1)]     # 1..n
        m = int(input("How many edges?: "))
        if m < 0:
            print("Error! The number of vertices should be positive.")
            return
        print("Now enter the edges, one in a line..")
        E = []
        for i in range(m):
            t = input("Edge " + str(i) + ": ").split()
            t = [int(x) for x in t]
            if len(t) == 2:
                E.append(t)
        
        self.__ctrl.loadGraph(V, E)
        
        print("Vertices 1, ..., " + str(n) + " have been added to the graph.")
        print("Edges " + str(E) + " have been added to the graph.")
        print("Done!")
        self.__wait()
        
    def __menu2(self):
        file = input("Filename: ").strip()
        try:
            f = open(file, "r")
            n, m = f.readline().strip().split()
            n = int(n); m = int(m)
            V = [i for i in range(n)]       # 0..n-1
            E = []
            for i in range(m):
                t = f.readline().strip().split()
                x = int(t[0]); y = int(t[1]);
                E.append([x, y])
            f.close()
            self.__ctrl.loadGraph(V, E)
            print("Vertices 0, ..., " + str(n - 1) + " have been added to the graph.")
            print("Edges " + str(E) + " have been added to the graph.")
            print("Done!")
        except IOError as io:
            print("IOError! " + str(io))
        finally:
            self.__wait()
        
    def __menu3(self):
        S = self.__ctrl.approxVertexCover()
        print("Vertex cover: " + str(S) + ".")
        print("Size: " + str(len(S)))
        self.__wait()
    
    def __menu4(self):
        S = self.__ctrl.cleverGreedy()
        print("Vertex cover: " + str(S) + ".")
        print("Size: " + str(len(S)))
        self.__wait()
    
    def __menu5(self):
        S = self.__ctrl.Alom()
        print("Vertex cover: " + str(S) + ".")
        print("Size: " + str(len(S)))
        self.__wait()

    def __menu6(self):
        S = self.__ctrl.AlomExtended()
        print("Vertex cover: " + str(S) + ".")
        print("Size: " + str(len(S)))
        self.__wait()
        
    def __menu7(self):
        S = self.__ctrl.generateAndTest()
        print("Vertex cover: " + str(S) + ".")
        print("Size: " + str(len(S)))
        self.__wait()
    
    def __menu8(self):
        S1 = self.__ctrl.approxVertexCover()
        S2 = self.__ctrl.cleverGreedy()
        S3 = self.__ctrl.Alom()
        S4 = self.__ctrl.AlomExtended()
        S5 = self.__ctrl.generateAndTest()
        print("Approximation algorithm:")
        print(str(S1))
        print("Size: " + str(len(S1)) + "\n")
        print("Clever Greedy algorithm:")
        print(str(S2))
        print("Size: " + str(len(S2)) + "\n")
        print("Alom's algorithm:")
        print(str(S3))
        print("Size: " + str(len(S3)) + "\n")
        print("Alom's extended algorithm:")
        print(str(S4))
        print("Size: " + str(len(S4)) + "\n")
        print("Generate and test:")
        print(str(S5))
        print("Size: " + str(len(S5)) + "\n")
        self.__wait()