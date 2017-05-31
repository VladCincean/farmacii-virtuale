from random import random, randint
import math
from statistics import mean, stdev

W = 0.7
C1 = 1.5
C2 = 0.5

vmin = -5
vmax = 5

NUMBER_OF_RUNS = 30
DEBUG = False


class Particle:
    def __init__(self, n, vmin, vmax):
        '''

        :param n: particle size
        :param vmin: minimum possible value
        :param vmax: maximum possible value
        '''
        self.n = n
        self.vmin = vmin
        self.vmax = vmax
        self.position = [[(random() * (vmax - vmin) + vmin), (random() * (vmax - vmin) + vmin)] for _ in range(n)]
        self.velocity = [[random(), random()] for _ in range(n)]
        self.fitness = None
        self.evaluate()

        self.bestPosition = self.position[:]
        self.bestFitness = self.fitness

    def evaluate(self):
        f = 0
        for i in range(self.n):
            x = self.position[i][0]
            y = self.position[i][1]
            f += -20 * pow(math.e, -0.2 * math.sqrt(0.5 * (pow(x, 2) + pow(y, 2)))) \
                 - pow(math.e, 0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.e + 20
            f /= self.n

        self.fitness = f

    def update(self, best, t):
        '''

        :param best: (particle)
        :param t: iteration number
        :return:
        '''

        global W, C1, C2

        w = W / (t + 1)

        # update velocity
        for i in range(self.n):
            for comp in range(2):
                self.velocity[i][comp] = w * self.velocity[i][comp] \
                                   + C1 * (best.position[i][comp] - self.position[i][comp]) \
                                   + C2 * (self.bestPosition[i][comp] - self.position[i][comp])

        # update position
        for i in range(self.n):
            for comp in range(2):
                if self.velocity[i][comp] + self.position[i][comp] < self.vmin:
                    self.position[i][comp] = self.vmin
                elif self.velocity[i][comp] + self.position[i][comp] > self.vmax:
                    self.position[i][comp] = self.vmax
                else:
                    self.position[i][comp] = self.velocity[i][comp] + self.position[i][comp]

        # evaluate + update best position and fitness
        self.evaluate()
        if self.fitness < self.bestFitness:
            self.bestPosition = self.position[:]
            self.bestFitness = self.fitness


class Swarm:
    def __init__(self, nrOfParticles, particleSize):
        '''

        :param nrOfParticles: nr of particles
        :param particleSize: particle size
        '''
        global vmin, vmax

        self.nrOfParticles = nrOfParticles
        self.v = [Particle(particleSize, vmin, vmax) for _ in range(nrOfParticles)]

    def selectNeighbors(self, nr_neighbors):
        if nr_neighbors > len(self.v):
            nr_neighbors = len(self.v)
        neighbors = []
        for i in range(len(self.v)):
            aux = []
            for j in range(nr_neighbors):
                x = randint(0, len(self.v) - 1)
                while x in aux:
                    x = randint(0, len(self.v) - 1)
                aux.append(x)
            neighbors += aux[:]
        return neighbors

    def getBestParticles(self, n):
        self.v.sort(key=lambda particle: particle.bestFitness)
        return self.v[-n:]

    def getBestNeighbour(self, of):
        best_n = self.v[0]
        for i in range(1, len(self.v)):
            if best_n.bestFitness > self.v[i].bestFitness:
                best_n = self.v[i]
        return best_n


class Controller:
    def __init__(self):
        self.nrOfParticles = None
        self.particleSize = None
        self.nrIterations = None
        self.load_parameters('param.in')
        self.population = None

    def load_parameters(self, file='param.in'):
        f = open(file, 'r')
        for line in f:
            (k, v) = line.split('=')
            if k == 'nrOfParticles':
                self.nrOfParticles = int(v)
            elif k == 'particleSize':
                self.particleSize = int(v)
            elif k == 'nrIterations':
                self.nrIterations = int(v)
            else:
                raise KeyError('KeyError: Invalid param file format')
        f.close()

    def iteration(self):
        for i in range(self.nrOfParticles):
            part_i = self.population.v[i]
            best = self.population.getBestNeighbour(part_i)
            part_i.update(best, i)
            part_i.evaluate()

    def run_alg(self):
        self.population = Swarm(self.nrOfParticles, self.particleSize)
        for i in range(self.nrIterations):
            if DEBUG:
                print("iteration", i)
            self.iteration()
        return self.population.getBestParticles(1)


def main():
    ctrl = Controller()
    result = ctrl.run_alg()
    if DEBUG:
        print(str(result))
        for p in result:
            print(str(p.bestFitness) + " " + str(p.bestPosition))

    p = result[-1]
    print("\n\nf(%3.10f, %3.10f) = %3.10f" % (p.bestPosition[-1][0], p.bestPosition[-1][1], p.bestFitness))


def main_with_stat():
    results = []
    for i in range(NUMBER_OF_RUNS):
        print(str(i), 'th run')
        ctrl = Controller()
        results.append(ctrl.run_alg()[-1].bestFitness)

    xbar = mean(results)
    sigma = stdev(results, xbar)
    print('mean = ', xbar)
    print('stdev = ', sigma)

if __name__ == '__main__':
    main_with_stat()
