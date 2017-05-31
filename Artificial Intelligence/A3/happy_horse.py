from random import shuffle, random, randint
from statistics import mean, stdev

NUMBER_OF_RUNS = 30


class Problem:
    def __init__(self, fname='data12.in'):
        '''
        :param fname: input file
        '''
        self.n = 8
        self.m = 8
        self.file = fname
        self.load_from_file()

    def load_from_file(self):
        f = open(self.file, 'r')
        self.n, self.m = list(map(int, f.readline().split()))


class Individual:
    def __init__(self, problem=None):
        '''

        :param problem:
        '''
        if problem:
            self.problem = problem
            # self.L = [i for i in range(problem.n * problem.m)]
            self.L = [(i, j) for i in range(1, problem.n + 1) for j in range(1, problem.m + 1)]
            shuffle(self.L)
            # print(self.L)
        else:
            self.problem = None
            self.L = []

        self.f = 0

    @staticmethod
    def legal_moves(problem, i, j):
        ret = []
        for (x, y) in [
            (i - 2, j - 1), (i - 2, j + 1),
            (i - 1, j - 2), (i - 1, j + 2),
            (i + 1, j - 2), (i + 1, j + 2),
            (i + 2, j - 1), (i + 2, j + 1)
        ]:
            if x in range(1, problem.n + 1) and y in range(1, problem.m + 1):
                ret.append((x, y))
        return ret

    def number_legal_moves(self, problem):
        n = 0
        for k in range(len(self.L) - 1):
            if (self.L[k + 1][0], self.L[k + 1][1]) in self.legal_moves(problem, self.L[k][0], self.L[k][1]):
                n += 1
        return n

    def fitness(self, problem):
        self.f = problem.n * problem.m - 1 - self.number_legal_moves(problem)

    def mutate(self, probability):
        '''
        Swap mutation
        :param probability:
        '''
        if random() < probability:
            a = randint(0, len(self.L) - 1)
            b = randint(0, len(self.L) - 1)
            self.L[a], self.L[b] = self.L[b], self.L[a]

    @staticmethod
    def crossover(individual1, individual2):
        if individual1.problem != individual2.problem:
            return None

        ret = Individual()
        ret.problem = individual1.problem

        a = randint(0, len(individual1.L) - 1)
        b = randint(1, len(individual1.L))
        ret.L = individual1.L[a:b]

        count = 0
        i = 0
        while count < a and i < len(individual2.L):
            if individual2.L[i] not in ret.L:
                ret.L = [individual2.L[i]] + ret.L
                count += 1
            i += 1
        while i < len(individual2.L):
            if individual2.L[i] not in ret.L:
                ret.L += [individual2.L[i]]
            i += 1
        return ret


class Population:
    def __init__(self, nI, problem):
        '''
        Creates a population of nI individuals
        :param nI: number of individuals
        :param problem: the problem
        '''
        self.noIndividuals = nI
        self.problem = problem
        self.pop = [Individual(problem) for _ in range(nI)]

    def evaluate(self):
        for x in self.pop:
            x.fitness(self.problem)

    def selection(self, n):
        if n < self.noIndividuals:
            # self.noIndividuals = n
            self.pop = sorted(self.pop, key=lambda individual: individual.f)
        self.pop = self.pop[:n]

    def reunion(self, second):
        self.noIndividuals += second.noIndividuals
        self.pop += second.pop

    def best(self, n):
        return sorted(self.pop, key=lambda individual: individual.f)[:n]


class Algorithm:
    def __init__(self, paramFile='param.in', inputFile='data12.in'):
        '''

        :param paramFile: file with parameters (nI, nG, pM, pC)
        :param inputFile: file with problem input
        '''
        self.noIndividuals = 0
        self.noGenerations = 0
        self.probabilityMutation = 0
        self.probabilityCrossover = 0
        self.read_from_file(paramFile)
        self.problem = Problem(inputFile)
        self.population = Population(self.noIndividuals, self.problem)
        self.population.evaluate()s

    def read_from_file(self, file='param.in'):
        f = open(file, 'r')
        for line in f:
            (k, v) = line.split('=')
            if k == 'probabilityMutation':
                self.probabilityMutation = float(v)
            elif k == 'probabilityCrossover':
                self.probabilityCrossover = float(v)
            elif k == 'noIndividuals':
                self.noIndividuals = int(v)
            elif k == 'noGenerations':
                self.noGenerations = int(v)
            else:
                raise KeyError('KeyError: Invalid param file format')

    def iteration(self):
        shuffle(self.population.pop)
        offspring = Population(0, self.problem)
        nr = self.noIndividuals // 2
        for k in range(nr):
            offspring.pop.append(Individual.crossover(self.population.pop[2 * k], self.population.pop[2 * k + 1]))
            offspring.pop[k].mutate(self.probabilityMutation)
        offspring.evaluate()
        self.population.reunion(offspring)
        self.population.selection(self.noIndividuals)

    def run(self):
        for i in range(self.noGenerations):
            # print(str(i), 'th iteration')
            self.iteration()
        return self.population.best(1)

    def statistics(self):
        pass


class Application:
    def __init__(self):
        pass
        # self.p = Problem()

    @staticmethod
    def main():
        alg = Algorithm()
        res = alg.run()
        # print('1')
        print(res[0].L)
        print('fitness = ' + str(res[0].f))
        # print('2')

    @staticmethod
    def main_with_stat():
        results = []
        for i in range(NUMBER_OF_RUNS):
            print(str(i), 'th run')
            alg = Algorithm()
            results.append(alg.run()[0].f)

        xbar = mean(results)
        sigma = stdev(results, xbar)
        print('mean = ', xbar)
        print('stdev = ', sigma)


app = Application()
app.main()
