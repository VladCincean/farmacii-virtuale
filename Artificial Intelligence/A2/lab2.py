

DEBUG = True
COLORS = ['blue', 'yellow', 'red']

class State:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return self.__str__()


class Problem:
    def __init__(self, input_file):
        self.input_file = input_file

        self.n, self.m, self.edges = None, None, None
        if not self.read_from_file():
            print('Error while reading from file. Aborting...')
            exit(1)

        self.initial_state = State([0] * self.n)  # all countries -> same color ('color 0' = no color)

        if DEBUG:
            print('Problem(): initial state = ' + str(self.initial_state))

    def get_nr_no_good(self, state):
        nr_no_good = 0

        # nr tari necolorate
        for i in state.values:
            if i == 0:
                nr_no_good += 1

        # nr vecini cu aceeasi culoare
        for i in range(len(self.edges)):
            if state.values[self.edges[i][0]] == state.values[self.edges[i][1]]:
                nr_no_good += 1

        return nr_no_good

    def least_used_color(self, vector):
        c0 = vector.count(COLORS[0])
        c1 = vector.count(COLORS[1])
        c2 = vector.count(COLORS[2])

        # print('luc: ', str({COLORS[0]: c0, COLORS[1]: c1, COLORS[2]: c2}))
        return {0: c0, 1: c1, 2: c2}

    def is_solution(self, state):
        return self.get_nr_no_good(state) == 0

    @staticmethod
    def expand(state):
        for i in range(len(state.values)):
            if state.values[i] == 0:
                new_states = []
                for j in COLORS:
                    st = state.values[:]
                    st[i] = j
                    new_states.append(State(st))
                return new_states
        return []

    def heuristic(self, state1, state2):
        n1 = self.get_nr_no_good(state1)
        n2 = self.get_nr_no_good(state2)
        if n1 == n2:
            return 0
        return (n2 - n1) / abs(n2 - n1)

    def heuristic_2(self, state1, state2):
        c1 = state1.values.count(0)
        c2 = state2.values.count(0)

        s1 = state1.values[:-c1]  # state1, mai putin 0-urile de la final
        s2 = state2.values[:-c2]  # state2, mai putin 0-urile de la final

        h1 = s1[:-1]
        vals = self.least_used_color(state1.values)
        if vals[s1[-1]] == vals[s2[-1]]:
            return 0
        return (vals[s2[-1]] - vals[s1[-1]]) / abs(vals[s2[-1]] - vals[s1[-1]])


    def read_from_file(self):
        try:
            fd = open(self.input_file, 'r')
            self.n = int(fd.readline().strip())  # nr countries
            self.m = int(fd.readline().strip())  # nr neighbours
            self.edges = []
            for i in range(self.m):
                x, y = fd.readline().strip().split(' ')
                x, y = int(x), int(y)
                self.edges.append((x, y))
        except IOError:
            return False

        if DEBUG:
            print('read_from_file ---->')
            print('n_countries = ' + str(self.n))
            print('n_neighbours = ' + str(self.m))
            print('edges = ' + str(self.edges))
            print('<---- read_from_file')

        return True


class Controller:
    def __init__(self, problem):
        self.problem = problem

    def order_states(self, states):
        sorted_states = sorted(states, cmp=self.problem.heuristic)
        return sorted_states

    def bfs(self):
        found = False
        the_solution = None
        visited = []
        to_visit = [self.problem.initial_state]

        while to_visit != [] and not found:
            node = to_visit.pop(0)

            if DEBUG:
                print('bfs: visiting ' + str(node))

            visited.append(node)
            if self.problem.is_solution(node):
                found = True
                the_solution = node
            else:
                aux = []
                for x in self.problem.expand(node):
                    if x not in visited:
                        aux.append(x)
                to_visit = to_visit + aux
        return the_solution

    def gbfs(self):
        found = False
        the_solution = None
        visited = []
        to_visit = [self.problem.initial_state]

        while to_visit != [] and not found:
            node = to_visit.pop(0)

            if DEBUG:
                print('gbfs: visiting ' + str(node))

            visited.append(node)
            if self.problem.is_solution(node):
                found = True
                the_solution = node
            else:
                aux = []
                for x in self.order_states(self.problem.expand(node)):
                    if x not in visited:
                        aux.append(x)
                to_visit = to_visit + aux
        return the_solution


class UI:
    def __init__(self, ctrl):
        self.ctrl = ctrl

    @staticmethod
    def print_menu():
        s = 'Please select an option.\n'
        s += '1 - solve using BFS\n'
        s += '2 - solve using GBFS\n'
        s += '0 - EXIT\n'
        print(s)

    def run(self):
        while True:
            self.print_menu()
            opt = str(input('Your option: ')).strip()
            if opt == '1':
                sol = self.ctrl.bfs()
                print('Solution found by BFS: ' + str(sol))
            elif opt == '2':
                sol = self.ctrl.gbfs()
                print('Solution found by GBFS: ' + str(sol))
            elif opt == '0':
                break
            else:
                print('Wrong command!')
        print('Bye!')

if __name__ == '__main__':
    p = Problem('18.in')
    c = Controller(p)
    ui = UI(c)
    ui.run()
