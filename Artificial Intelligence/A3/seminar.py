from random import shuffle, random, randint, sample

class Problem:
    def __init__(self, fname):
        '''

        :param fname: file name
        '''
        self.n = 0
        self.A = []
        self.S = 0
        self.file = fname
        self.load_file()

    def load_file(self):
        f = open(self.file, 'r')
        self.n = int(f.readline())
        self.A = list(map(int, f.readline().split()))
        self.S = int(f.readline())


class Individ:
    def __init__(self, p):
        '''

        :param p: problem
        '''
        self.size = p.n
        self.v = [sample([0, 1], 1)[0] for k in range(self.size)]
        self.summ = 0
        self.f = 0

    def fitness(self, p):
        self.summ = sum([self.v[k] * p.A[k] for k in range(self.size)])
        self.f = abs(p.S - self.summ)


class Population:
    def __init__(self, p, no):
        self.noInd = no
        self.pop = [Individ(p) for k in range(self.noInd)]

    def evaluate(self, p):
        for x in self.pop:
            x.fitness(p)

    def reunion(self, toAdd):
        self.noInd = self.noInd + toAdd.noInd
        self.pop = self.pop + toAdd.pop

    def selection(self, n):
        if n < self.noInd:
            self.pop = sorted(self.pop, key = lambda Individ: Individ.f)
        self.pop = self.pop[:n]

    def best(self, n):
        aux = sorted(self.pop, key = lambda Individ: Individ.f)
        return aux[:n]


class Algorithm:
    def __init__(self, nI = 100, nG = 1000, file = "seminar.txt"):
        '''

        :param nI: nr indivizi
        :param nG: nr generatii
        :param file: fisier input
        '''
        self.problem = Problem(file)
        self.noInd = nI
        self.p = Population(self.problem, self.noInd)
        self.p.evaluate(self.problem)
        self.noGen = nG

    def run(self):
        for k in range(self.noGen):
            self.iteration()
        return self.p.best(1)

    def iteration(self):
        shuffle(self.p.pop)
        offspring = Population(self.problem, 0)
        no = self.noInd // 2
        for k in range(no):
            offspring.pop.append(self.crossover(self.p.pop[2 * k], self.p.pop[2 * k + 1]))
            self.mutate(offspring.pop[k])
        offspring.evaluate(self.problem)
        self.p.reunion(offspring)
        self.p.selection(self.noInd)

    def crossover(self, i1, i2):
        aux = Individ(self.problem)
        for k in range(i1.size):
            if random() < 0.5:
                aux.v[k] = i1.v[k]
            else:
                aux.v[k] = i2.v[k]
        return aux

    def mutate(self, ind):
        if random() < 0.1:
            k = randint(0, ind.size - 1)
            ind.v[k] = 1 - ind.v[k]


if __name__ == '__main__':
    alg = Algorithm()
    rez = alg.run()
    print(rez[0].v)